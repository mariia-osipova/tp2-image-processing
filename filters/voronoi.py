import numpy as np
import random
from distance import euclidean
from distance import manhattan

# n = 400
# height = 150
# width = 100
# data sample

def generate_points(n, height, width, d):
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

def voronoi(img, points, height, width, d):

    arr = np.array(img)
    none_matrix = np.full_like(arr, None, dtype=object)

    seed_colors = []
    for (y, x) in points:
        seed_colors.append(arr[y, x])

    for i in range(height):
        for j in range(width):
            p1 = (i, j)

            menor_distancia = 999999
            punto_mas_cercano = None

            for k in range(len(points)):
                p2 = (points[k][0], points[k][1])

                distancia = d(p1, p2)

                if distancia < menor_distancia:
                    menor_distancia = distancia
                    punto_mas_cercano = k

            none_matrix[i, j] = seed_colors[punto_mas_cercano]
    print("voronoi jeje")
    return none_matrix