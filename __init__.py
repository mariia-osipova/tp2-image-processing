from filters.mosaico import mosaico
from filters.voronoi import voronoi, generate_points
from distance.euclidean import euclidean
from distance.manhattan import manhattan
from PIL import Image
import numpy as np

def main():
    # ask user for image path
    path = input("Ingrese la ruta de la imagen: ")

    # open the Image to test
    # TODO: delete later
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print("No se encontró la imagen. Por favor, verifique la ruta e intente nuevamente. ")
        return

    width, height = img.size
    img = np.array(img)

    selected_filter = input("Seleccione el método (vitral/mosaico): ")

    while selected_filter not in ["vitral", "mosaico"]:
        selected_filter = input("Seleccione de vuelta el método (vitral/mosaico): ")

    if selected_filter == "vitral":

        # ask the user for the number of points (default n = 1000)
        n = input("Ingrese la cantidad de puntos (default=1000): ")
        if n == "":
            n = 1000
        else:
            n = int(n) # should we check if n is int?

        d = input("Seleccione la métrica de distancia (euclidean/manhattan): ")
        while d not in ["euclidean", "manhattan"]:
            d = input("Seleccione la métrica de distancia de vuelta (euclidean/manhattan): ")
        if d == "euclidean":
            d = euclidean
        else:
            d = manhattan

        # for voronoi: generate random points
        points = generate_points(n, height, width)
        
        path_result = input("Seleccione la ruta para guardar la imagen procesada: ")
        
        img_p = voronoi(path, img, points, d)
        return img_p.save(path_result)

    elif selected_filter == "mosaico":

        variance_threshold = input("Ingrese el umbral de varianza (default=150): ")
        if variance_threshold == "":
            variance_threshold = 150
        else:
            while True:
                try:
                    variance_threshold = int(variance_threshold)
                    if variance_threshold <= 0:
                        variance_threshold = input("El umbral debe ser un número positivo. Intente de nuevo: ")
                    else:
                        break
                except ValueError:
                    variance_threshold = input("Por favor, ingrese un número válido: ")

        min_size = input("Ingrese el tamaño mínimo de bloque (default=20): ")
        if min_size == "":
            min_size = 20
        else:
            while True:
                try:
                    min_size = int(min_size)
                    if min_size <= 0:
                        min_size = input("El tamaño mínimo debe ser un número positivo. Intente de nuevo: ")
                    else:
                        break
                except ValueError:
                    min_size = input("Por favor, ingrese un número válido: ")

        max_passes = input("Ingrese el número máximo de subdivisiones (default=10): ")
        if max_passes == "":
            max_passes = 10
        else:
            while True:
                try:
                    max_passes = int(max_passes)
                    if max_passes <= 0:
                        max_passes = input("El número máximo debe ser un número positivo. Intente de nuevo: ")
                    else:
                        break
                except ValueError:
                    max_passes = input("Por favor, ingrese un número válido: ")

        bordes = input("¿Dibujar bordes en los bloques? (si/no): ").strip().lower()
        while bordes not in ["si", "no"]:
            bordes = input("Por favor, escriba 'si' o 'no': ").strip().lower()
        bordes = bordes == "si"

        path_result = input("Seleccione la ruta para guardar la imagen procesada (por ejemplo, resultado.png): ")

        if not (path_result.lower().endswith(".png") or path_result.lower().endswith(
                ".jpg") or path_result.lower().endswith(".jpeg")):
            path_result += ".png"

        img_p = mosaico(img, variance_threshold, min_size, max_passes, bordes, height, width)
        img_pillow = Image.fromarray(img_p)

        img_pillow.save(path_result)
        print(f"Imagen guardada en: {path_result}")
        return path_result

if __name__ == "__main__":
    main()