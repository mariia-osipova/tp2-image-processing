import os
import time
from PIL import Image
import tifffile as tiff
import numpy as np
from filters.voronoi import voronoi, generate_points
from distance.euclidean import euclidean
from distance.manhattan import manhattan

def safe_open(path):
    try:
        return Image.open(path)
    except:
        arr = tiff.imread(path)
        return Image.fromarray(arr)
input_dir = "../test_images"
output_dir = "../out"

filter_type = "voronoi"
n_puntos = 1500
metrica = manhattan

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
        im_orig = safe_open(input_path).convert("RGB")
        orig_w, orig_h = im_orig.size

        if max(orig_w, orig_h) > 200:
            if orig_w >= orig_h:
                small_w = 200
                small_h = max(1, int(orig_h * 200 / orig_w))
            else:
                small_h = 200
                small_w = max(1, int(orig_w * 200 / orig_h))

            im_small = im_orig.resize((small_w, small_h), Image.BILINEAR)
            width, height = small_w, small_h
            print(f"  Redimensionada a: {width}x{height}")

            points = generate_points(n_puntos, height, width)
            result_small = voronoi(im_small, points, height, width, metrica)

            result = result_small.resize((orig_w, orig_h), Image.NEAREST)
        else:
            width, height = orig_w, orig_h
            points = generate_points(n_puntos, height, width)
            result = voronoi(im_orig, points, height, width, metrica)

        out = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{filter_type}.png")
        result.save(out)
        print(f"  {filename} saved as {out} ({time.time() - start_time:.2f} sec)")
        ok += 1
    except Exception as e:
        print(f"an error occurred with {filename}: {e}")
        fail += 1

print(f"\nprocessed: {ok} OK, {fail} failed")