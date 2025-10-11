from filters.mosaico import mosaico
from filters.voronoi import voronoi, generate_points
from distance.euclidean import euclidian
from distance.manhattan import manhattan
from PIL import Image

def main():
    # ask user for image path
    path = input("Ingrese la ruta de la imagen: ")

    # open the Image to test
    # TODO: delete later
    img = Image.open(path)

    width, height = img.size

    # TODO: ask the user which filter to apply (mosaico or voronoi)

    # for voronoi: generate random points
    # TODO: ask the user for the number of points (default n = 800)
    n = 800
    points = generate_points(n, height, width)
    # run filters
    mosaico(path, img)
    voronoi(path, img, points)

if __name__ == "__main__":
    main()