import os
from PIL import Image
import numpy as np
import time
from filters.mosaico import mosaico
from filters.voronoi import voronoi, generate_points
from distance.euclidean import euclidean
from distance.manhattan import manhattan

input_dir = "test_images"
output_dir = "out"

# filter_type = "vitral"
# n = 200
# d = euclidean

filter_type = "mosaico"
variance_threshold = 150
min_size = 20
max_passes = 10
bordes = False

os.makedirs(output_dir, exist_ok=True)
exts = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".pgm")

files = sorted(
    [f for f in os.listdir(input_dir) if f.lower().endswith(exts)],
    key=lambda x: x.lower()
)

for filename in files:
    # if not filename.lower().endswith((".png", ".jpg", ".jpeg", "")):
    #     continue

    input_path = os.path.join(input_dir, filename)
    print(f"process {filename}...")

    start_time = time.time()

    try:
        with Image.open(input_path) as im:
            if getattr(im, "n_frames", 1) > 1:
                im.seek(0)
            im = im.convert("RGB")

            img = np.array(im)
            height, width = img.shape[:2]

        # if filter_type == "vitral":
        #     points = generate_points(n, height, width)
        #     result = voronoi(img, points, height, width, d)
        #
        # else:
        result = mosaico(img, variance_threshold, min_size, max_passes, bordes, height, width)
        result = Image.fromarray(result)

        output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{filter_type}.png")
        result.save(output_path)
        elapsed = time.time() - start_time
        print(f" {filename} saved as {output_path} ({elapsed:.2f} sec)")

        # TODO: save the report as .md

    except Exception as e:
        print(f"an error occurred with {filename}: {e}")