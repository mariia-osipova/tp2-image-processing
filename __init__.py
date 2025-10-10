from filters.mosaico import mosaico
from filters.voronoi import voronoi


def main():
    path = input("Ingrese la ruta de la imagen: ")
    return path

mosaico(path=main())
voronoi(path=main())

if __name__ == "__main__":
    main()