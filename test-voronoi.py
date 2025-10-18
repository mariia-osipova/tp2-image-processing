import os
import time
from PIL import Image
from filters.voronoi import voronoi, generate_points
from distance.euclidean import euclidean
from distance.manhattan import manhattan

input_dir = "test_images"
output_dir = "out"

filter_type = "voronoi"
n_puntos = 1000
metrica = euclidean

os.makedirs(output_dir, exist_ok=True)
exts = (".png", ".jpg", ".jpeg", ".bmp", ".pgm")

files = sorted([f for f in os.listdir(input_dir) if f.lower().endswith(exts)], key=lambda x: x.lower())

ok = 0
fail = 0

for filename in files:
    input_path = os.path.join(input_dir, filename)
    print(f"process {filename}...")
    start_time = time.time()
    try:
        im = Image.open(input_path).convert("RGB")
        h, w = im.size
        points = generate_points(n_puntos, h, w, metrica)
        result = voronoi(im, points, h, w, metrica)
        out = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{filter_type}.png")
        result.save(out)
        print(f" {filename} saved as {out} ({time.time() - start_time:.2f} sec)")
        ok += 1
    except Exception as e:
        print(f"an error occurred with {filename}: {e}")
        fail += 1

print(f"\nprocessed: {ok} OK, {fail} failed")