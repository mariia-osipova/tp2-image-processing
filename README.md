## Image Processing — Practical Assignment

### Objective

The goal of this project is to develop an image processing system capable of applying different visual filters in a configurable way.  
The user can choose between two main filters:

- **Voronoi**: generates a representation of the image based on regions (cells) created from randomly distributed seed points.
- **Mosaic**: transforms the image into blocks (tiles), assigning each tile the average color of the pixels it contains.

Each filter includes adjustable input parameters, allowing the user to experiment with different configurations and visual results. However, during the development process, we encountered performance issues with the Voronoi filter, as it required significant processing time for larger images. To address this, we introduced an additional parameter called `speed`, which lets the user decide between higher processing speed or better image quality. When speed = True, the algorithm prioritizes faster computation, resulting in a lower-quality but quicker output. 

# Usage Example 
### Voronoi Filter

Using the following input parameters:

```python
n_puntos = 1000
metrica = euclidean
```

| Original Image                                                                                            | Processed Result, speed = False                                                                                                            | Processed Result, speed = True                                                                                                     |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| ![alonso.jpeg](https://mariia-osipova.github.io/tp2-image-processing/test_images/alonso.jpeg)             | ![alonso_false_euclidean.png](https://mariia-osipova.github.io/tp2-image-processing/data/data6-eucl-1000-f/alonso_false_euclidean.png)     |  ![alonso_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/data3-eucl-1000/alonso_voronoi.png)              |
| ![barbara_color.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/barbara_color.bmp) | ![barbara_false_euclidean.png](https://mariia-osipova.github.io/tp2-image-processing/data/data6-eucl-1000-f/barbara_false_euclidean.png)   | ![barbara_color_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/data3-eucl-1000/barbara_color_voronoi.png) |
| ![goldhill.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/goldhill.bmp)           | ![goldhill_false_euclidean.png](https://mariia-osipova.github.io/tp2-image-processing/data/data6-eucl-1000-f/goldhill_false_euclidean.png) | ![goldhill_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/data3-eucl-1000/goldhill_voronoi.png)           |
| ![house.png](https://mariia-osipova.github.io/tp2-image-processing/test_images/house.png)                 | ![house_false_euclidean.png](https://mariia-osipova.github.io/tp2-image-processing/data/data6-eucl-1000-f/house_false_euclidean.png)       | ![img.png](https://mariia-osipova.github.io/tp2-image-processing/data/data3-eucl-1000/img.png)                                     |

```python
n_puntos = 700
metrica = manhattan
```

| Original Image                                                                                | Processed Result, speed = False                                                                                | Processed Result, speed = True                                                                                |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![rainier.jpg](https://mariia-osipova.github.io/tp2-image-processing/data/rainier.jpg)        | ![rainier_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/d5m700f/rainier_voronoi.png) | ![rainier_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/d4m700/rainier_voronoi.png) |
| ![flowers.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/flowers.bmp) | ![flowers_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/d5m700f/flowers_voronoi.png) | ![flowers_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/d4m700/flowers_voronoi.png) |
| ![fruits.png](https://mariia-osipova.github.io/tp2-image-processing/test_images/fruits.png)   | ![fruits_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/d4m700/fruits_voronoi.png)    | ![fruits_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/d4m700/fruits_voronoi.png)   |
| ![barbara.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/barbara.bmp) | ![barbara_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/d5m700f/barbara_voronoi.png) | ![barbara_voronoi.png](https://mariia-osipova.github.io/tp2-image-processing/data/d4m700/barbara_voronoi.png) |

### Mosaic Filter

Using the following input parameters:

```python
variance_threshold = 150
min_size = 20
max_passes = 10
bordes = False
```

| Original Image                                                                                     | Processed Result                                                                                            |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![cablecar.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/cablecar.bmp)    | ![cablecar_mosaico.png](https://mariia-osipova.github.io/tp2-image-processing/data/cablecar_mosaico.png)    |
| ![cornfield.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/cornfield.bmp)  | ![cornfield_mosaico.png](https://mariia-osipova.github.io/tp2-image-processing/data/cornfield_mosaico.png)  |
| ![flowers.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/flowers.bmp)      | ![flowers_mosaico.png](https://mariia-osipova.github.io/tp2-image-processing/data/flowers_mosaico.png)      |
| ![boat.png](https://mariia-osipova.github.io/tp2-image-processing/test_images/boat.png)            | ![boat_mosaico.png](https://mariia-osipova.github.io/tp2-image-processing/data/boat_mosaico.png)            |

```python
variance_threshold = 100
min_size = 30
max_passes = 5
bordes = True
```

| Original Image                                                                                      | Processed Result                                                                                              |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![tulips.png](https://mariia-osipova.github.io/tp2-image-processing/test_images/tulips.png)         | ![tulips_mosaico.png](https://mariia-osipova.github.io/tp2-image-processing/data/tulips_mosaico.png)          |
| ![boat_color.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/boat_color.bmp) | ![boat_color_mosaico.png](https://mariia-osipova.github.io/tp2-image-processing/data/boat_color_mosaico.png)  |
| ![goldhill.bmp](https://mariia-osipova.github.io/tp2-image-processing/test_images/goldhill.bmp)     | ![goldhill_mosaico.png](https://mariia-osipova.github.io/tp2-image-processing/data/goldhill_mosaico.png)      |
| ![arc2.png](https://mariia-osipova.github.io/tp2-image-processing/test_images/arc2.png)             | ![arc2_mosaico.png](https://mariia-osipova.github.io/tp2-image-processing/data/arc2_mosaico.png)              |

# Project Setup

Follow these steps to get your project up and running:

## 1. Clone the project

Copy the project from the `main` branch.

![img.png](data/img_00.png)

## 2. Install requirements

Run the following command to install the necessary dependencies:

```bash
python3 -m pip install -r requirements.txt
```

## 3. Run the project

Execute the project from the console with the metrics you need.

![img.png](data/img_0.png)

## 4. Video example

Here is a video to demonstrate how to use the project:

[![Video Example](https://img.youtube.com/vi/7DSI2kXDgLM/0.jpg)](https://youtu.be/7DSI2kXDgLM?si=lGnbNni_57aXiv25)

----

#### GitHub Pages

Visit the GitHub Pages site for this project: [https://mariia-osipova.github.io/tp2-image-processing/](https://mariia-osipova.github.io/tp2-image-processing/).