from PIL import Image
import random

# n = 400
# height = 150
# width = 100
# data sample

def generate_points(n, height, width):
    '''
    Generate n random points on the image (coordinates (y, x)).
    n — number of points (should be received from __init__.py)
    height, width - the size of the image (should be received from __init__.py)

    return: list of points (y, x)
    '''

    points = []

    for _ in range(n):
        (y, x) = (
            random.randint(0, height - 1),
            random.randint(0, width - 1)
        )

        if (y, x) not in points:
            points.append((y, x))
        else:
            while (y, x) in points:
                (y, x) = (
                    random.randint(0, height - 1),
                    random.randint(0, width - 1)
                )
            points.append((y, x))

    points.sort(key=lambda p: p[0] + p[1])  # sort points by diagonal (increasing sum of y + x)

    return points

# points = generate_points(n, height, width)
# print(points)

def voronoi(path, img, points):
    img_p = img.copy()
    return img_p