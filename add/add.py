from PIL import Image, UnidentifiedImageError, ImageFile
import tifffile as tiff
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
import io
import numpy as np

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