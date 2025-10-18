import os
import time
import numpy as np
import warnings
import tifffile as tiff
from pathlib import Path
import io
from contextlib import redirect_stdout, redirect_stderr
from PIL import Image, UnidentifiedImageError, ImageFile
from filters.mosaico import mosaico
from filters.voronoi import voronoi, generate_points
from distance.euclidean import euclidean
from distance.manhattan import manhattan

warnings.filterwarnings("ignore", category=UserWarning, module="tifffile")
ImageFile.LOAD_TRUNCATED_IMAGES = True

input_dir = "test_images"
output_dir = "out"

filter_type = "mosaico"
variance_threshold = 100
min_size = 30
max_passes = 5
bordes = True

def _to_uint8(a: np.ndarray) -> np.ndarray:
    if a.dtype == np.uint8:
        return a
    a = a.astype(np.float32)
    if a.max() <= 1.0:
        a *= 255
    return np.clip(a, 0, 255).astype(np.uint8)

def _read_tiff_quiet(path: str) -> np.ndarray:
    buf = io.StringIO()
    with redirect_stdout(buf), redirect_stderr(buf):
        try:
            return tiff.imread(path)
        except:
            with tiff.TiffFile(path) as tf:
                return tf.pages[0].asarray()

def safe_open(path: str) -> Image.Image:
    try:
        im = Image.open(path)
        im.load()
        return im
    except (UnidentifiedImageError, OSError, ValueError):
        pass
    if Path(path).suffix.lower() not in (".tif", ".tiff"):
        raise
    arr = _read_tiff_quiet(path)
    arr = _to_uint8(arr)
    if arr.ndim == 2:
        return Image.fromarray(arr, "L")
    if arr.ndim == 3 and arr.shape[-1] > 3:
        arr = arr[..., :3]
    return Image.fromarray(arr).convert("RGB")

os.makedirs(output_dir, exist_ok=True)
exts = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".pgm")

files = sorted([f for f in os.listdir(input_dir) if f.lower().endswith(exts)], key=lambda x: x.lower())

ok = 0
fail = 0

for filename in files:
    input_path = os.path.join(input_dir, filename)
    print(f"process {filename}...")
    start_time = time.time()
    try:
        im = safe_open(input_path).convert("RGB")
        img = np.array(im)
        h, w = img.shape[:2]
        result = mosaico(img, variance_threshold, min_size, max_passes, bordes, h, w)
        result = Image.fromarray(result.astype("uint8")).convert("RGB")
        out = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{filter_type}.png")
        result.save(out)
        print(f" {filename} saved as {out} ({time.time() - start_time:.2f} sec)")
        ok += 1
    except Exception as e:
        print(f"an error occurred with {filename}: {e}")
        fail += 1

print(f"\nprocessed: {ok} OK, {fail} failed")