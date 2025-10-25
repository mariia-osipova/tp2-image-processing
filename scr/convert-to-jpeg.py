from PIL import Image

input_image_path = '/Users/maria/PycharmProjects/PythonProject/tp2-image-processing/data/img_0.png'
img = Image.open(input_image_path)
output_image_path = '/Users/maria/PycharmProjects/PythonProject/tp2-image-processing/data/img_0.jpg'
img.convert('RGB').save(output_image_path, 'JPEG')

print(f'saved as {output_image_path}')