from PIL import Image

input_image_path = '/Users/maria/PycharmProjects/PythonProject/tp2-image-processing/test_images/rainier.bmp'
img = Image.open(input_image_path)
output_image_path = '/Users/maria/PycharmProjects/PythonProject/tp2-image-processing/data/rainier.jpg'
img.convert('RGB').save(output_image_path, 'JPEG')

print(f'saved as {output_image_path}')