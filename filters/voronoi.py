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
    colores=[]

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
    for i in height:
        for j in width:
            p1_x = j
            p1_y = i

            menor_distancia = 999999
            punto_mas_cercano = 0 
    for k in range(len(points)):
        punto_x = points[k][0]  
        punto_y= points [k][1]

        dx = p1_x - punto_x
        dy = p1_y - punto_y
        distancia = dx*dx + dy*dy

       
        if distancia < menor_distancia:
            menor_distancia = distancia
            punto_mas_cercano = k

    color = colores[punto_mas_cercano]

    return points

# points = generate_points(n, height, width)
# print(points)

def voronoi(path, points):
    print("voronoi jeje")