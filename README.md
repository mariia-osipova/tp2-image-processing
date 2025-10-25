## Image Processing — Practical Assignment

### Objective

The goal of this project is to develop an image processing system capable of applying different visual filters in a configurable way.  
The user can choose between two main filters:

- **Voronoi**: generates a representation of the image based on regions (cells) created from randomly distributed seed points.
- **Mosaic**: transforms the image into blocks (tiles), assigning each tile the average color of the pixels it contains.

Each filter includes adjustable input parameters, allowing the user to experiment with different configurations and visual results. However, during the development process, we encountered performance issues with the Voronoi filter, as it required significant processing time for larger images. To address this, we introduced an additional parameter called `speed`, which lets the user decide between higher processing speed or better image quality. When speed = True, the algorithm prioritizes faster computation, resulting in a lower-quality but quicker output. 

### Usage Example — Voronoi Filter

Using the following input parameters:

```python
n_puntos = 1000
metrica = euclidean
```

| Original Image                                      | Processed Result, speed = False                                                      |  Processed Result, speed = True                                               |
|-----------------------------------------------------|--------------------------------------------------------------------------------------| ------------------------------------------------------------------------------|
| ![alonso.jpeg](docs/img/alonso.jpeg)             | ![alonso_false_euclidean.png](docs/img/alonso_false_euclidean.png)     | ![alonso_voronoi.png](docs/img/alonso_voronoi.png)               |
| ![barbara_color.bmp](docs/img/barbara_color.bmp) | ![barbara_false_euclidean.png](docs/img/barbara_false_euclidean.png)   |![barbara_color_voronoi.png](docs/img/barbara_color_voronoi.png) |
| ![goldhill.bmp](docs/img/goldhill.bmp)           | ![goldhill_false_euclidean.png](docs/img/goldhill_false_euclidean.png) | ![goldhill_voronoi.png](docs/img/goldhill_voronoi.png) |
| ![house.png](docs/img/house.png)                 | ![house_false_euclidean.png](docs/img/house_false_euclidean.png)       | ![img.png](docs/img/img.png) |

```python
n_puntos = 700
metrica = manhattan
```
| Original Image                           | Processed Result, speed = False                                   | Processed Result, speed = True                                  |
|------------------------------------------|-------------------------------------------------------------------|-----------------------------------------------------------------|
| ![rainier.bmp](docs/img/rainier.bmp)     | ![rainier_voronoi.png](data/data5-manh-700-f/rainier_voronoi.png) | ![rainier_voronoi.png](data/data4-manh-700/rainier_voronoi.png) |
| ![flowers.bmp](docs/img/flowers.bmp)     | ![flowers_voronoi.png](data/data5-manh-700-f/flowers_voronoi.png) | ![flowers_voronoi.png](data/data4-manh-700/flowers_voronoi.png) |
| ![fruits.png](docs/img/fruits.png)       | ![fruits_voronoi.png](data/data5-manh-700-f/fruits_voronoi.png)   | ![fruits_voronoi.png](data/data4-manh-700/fruits_voronoi.png)   |
| ![barbara.bmp](docs/img/barbara.bmp)     | ![barbara_voronoi.png](data/data5-manh-700-f/barbara_voronoi.png) | ![barbara_voronoi.png](data/data4-manh-700/barbara_voronoi.png) |

### Usage Example — Mosaic Filter

Using the following input parameters:

```python
variance_threshold = 150
min_size = 20
max_passes = 10
bordes = False
```

| Original Image                              | Processed Result                                     |
|---------------------------------------------|------------------------------------------------------|
| ![cablecar.bmp](docs/img/cablecar.bmp)   | ![cablecar_mosaico.png](docs/img/cablecar_mosaico.png)   |
| ![cornfield.bmp](docs/img/cornfield.bmp) | ![cornfield_mosaico.png](docs/img/cornfield_mosaico.png) |
| ![flowers.bmp](docs/img/flowers.bmp)     | ![flowers_mosaico.png](docs/img/flowers_mosaico.png)   |
| ![boat.png](docs/img/boat.png)           | ![boat_mosaico.png](docs/img/boat_mosaico.png)         |

```python
variance_threshold = 100
min_size = 30
max_passes = 5
bordes = True
```

| Original Image                                | Processed Result                                       |
|-----------------------------------------------|--------------------------------------------------------|
| ![tulips.png](docs/img/tulips.png)         | ![tulips_mosaico.png](docs/img/tulips_mosaico.png)         |
| ![boat_color.bmp](docs/img/boat_color.bmp) | ![boat_color_mosaico.png](docs/img/boat_color_mosaico.png) |
| ![goldhill.bmp](docs/img/goldhill.bmp)     | ![goldhill_mosaico.png](docs/img/goldhill_mosaico.png)     |
| ![arc2.png](docs/img/arc2.png)             | ![arc2_mosaico.png](docs/img/arc2_mosaico.png)             |
