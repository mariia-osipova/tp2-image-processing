import numpy as np
import random
from distance import euclidean
from distance import manhattan
from PIL import Image
# n = 400
# height = 150
# width = 100
# data sample

def generate_points(n, height, width):
    points = []

    for _ in range(n):
        '''
        Generate n random points on the image (coordinates (y, x)).
        n — number of points (should be received from __init__.py)
        height, width - the size of the image (should be received from __init__.py)

        return: list of points (y, x)
        '''

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

    points.sort(key=lambda p: p[0] + p[1])
    return points

def voronoi(img, points, height, width, d):

    arr = np.array(img)

    
    asignaciones = []
    for i in range(height):
        fila = []
        for j in range(width):
            fila.append(0)  
        asignaciones.append(fila)
    
    for i in range(height):
        for j in range(width):
            p1 = (i, j)
            menor_distancia = 999999
            punto_mas_cercano = 0

            for k in range(len(points)):
                p2 = (points[k][0], points[k][1])
                distancia = d(p1, p2)

                if distancia < menor_distancia:
                    menor_distancia = distancia
                    punto_mas_cercano = k

            asignaciones[i][j] = punto_mas_cercano
    
    promedios = []
    for k in range(len(points)):
        pixeles_celda = []
        
        for i in range(height):
            for j in range(width):
                if asignaciones[i][j] == k:
                    pixeles_celda.append(arr[i, j])
        
        if len(pixeles_celda) > 0:

            array_pixeles = np.array(pixeles_celda)
            promedio = np.mean(array_pixeles, axis=0)
            

            promedio = [int(promedio[0]), int(promedio[1]), int(promedio[2])]
            promedios.append(promedio)
        else:
 
            color_original = arr[points[k][0], points[k][1]]
            promedios.append([int(color_original[0]), int(color_original[1]), int(color_original[2])])

    imagen_resultado = []
    for i in range(height):
        fila = []
        for j in range(width):
            celda = asignaciones[i][j]
            color_promedio = promedios[celda]
            fila.append(color_promedio)
        imagen_resultado.append(fila)
    
    array_final = np.array(imagen_resultado)

    return Image.fromarray(array_final.astype(np.uint8))