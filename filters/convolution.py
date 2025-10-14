import numpy as np
from PIL import Image
import random

kernel = np.array([[-1, -1, -1],
                   [-1, -1, -1],
                   [-1, -1, -1]])

path = "/Users/maria/PycharmProjects/PythonProject/tp2-image-processing/test_images/alonso.jpeg"

img = Image.open(path)

def convolution(path, img, kernel):
    img_c = img.copy()

    # flip the matrix
    kernel = np.flipud(np.fliplr(kernel))

    # Add zero padding to the input image
    img_padded = np.zeros((img.shape[0] + 2, img.shape[1] + 2))
    img_padded[1:-1, 1:-1] = img

    # Loop over every pixel of the image
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            # element-wise multiplication of the kernel and the image
            output[y, x] = (kernel * image_padded[y: y + 3, x: x + 3]).sum()

    return output

output = convolution(path, img, kernel)
img.show()