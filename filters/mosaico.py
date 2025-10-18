import numpy
from PIL import Image

def mosaico(path):
    print("mosaico jeje")
    try:
        img = Image.open(path)
        width, height = img.size
        img.show()
    except (IOError, FileNotFoundError):
        print("wtf")
        pass