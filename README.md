## Image Processing — Practical Assignment

### Objective

The goal of this project is to develop an image processing system capable of applying different visual filters in a configurable way.  
The user can choose between two main filters:

- **Voronoi**: generates a representation of the image based on regions (cells) created from randomly distributed seed points.
- **Mosaic**: transforms the image into blocks (tiles), assigning each tile the average color of the pixels it contains.

Each filter includes adjustable input parameters, allowing the user to experiment with different configurations and visual results.

### Usage Example — Voronoi Filter

Using the following input parameters:

```python
n_puntos = 1000
metrica = euclidean
speed = False
```

```python
n_puntos = 1000
metrica = euclidean
speed = True
```

| Original Image                                      | Processed Result                                     |
|-----------------------------------------------------|------------------------------------------------------|
| ![alonso.jpeg](test_images/alonso.jpeg)             | ![alonso_voronoi.png](data3%28eucl-1000%29/alonso_voronoi.png)   |
| ![barbara_color.bmp](test_images/barbara_color.bmp) | ![barbara_color_voronoi.png](data3%28eucl-1000%29/barbara_color_voronoi.png) |
| ![goldhill.bmp](test_images/goldhill.bmp)           | ![goldhill_voronoi.png](data3%28eucl-1000%29/goldhill_voronoi.png)    |
| ![house.png](test_images/house.png)        | ![img.png](data3%28eucl-1000%29/img.png)        |

```python
n_puntos = 700
metrica = manhatten
speed = True
```
| Original Image                           | Processed Result                                                 |
|------------------------------------------|------------------------------------------------------------------|
| ![rainier.bmp](test_images/rainier.bmp)  | ![rainier_voronoi.png](data4%28manh-700%29/rainier_voronoi.png)  |
| ![flowers.bmp](test_images/flowers.bmp)  | ![flowers_voronoi.png](data4%28manh-700%29/flowers_voronoi.png)  |
| ![fruits.bmp](test_images/fruits.bmp)    | ![fruits_voronoi.png](data4%28manh-700%29/fruits_voronoi.png)    |
| ![barbara.bmp](test_images/barbara.bmp)  | ![barbara_voronoi.png](data4%28manh-700%29/barbara_voronoi.png)                       |


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
| ![cablecar.bmp](test_images/cablecar.bmp)   | ![cablecar_mosaico.png](data/cablecar_mosaico.png)   |
| ![cornfield.bmp](test_images/cornfield.bmp) | ![cornfield_mosaico.png](data/cornfield_mosaico.png) |
| ![flowers.bmp](test_images/flowers.bmp)     | ![flowers_mosaico.png](data/flowers_mosaico.png)     |
| ![boat.png](test_images/boat.png)           | ![boat_mosaico.png](data/boat_mosaico.png)           |

```python
variance_threshold = 100
min_size = 30
max_passes = 5
bordes = True
```

| Original Image                                | Processed Result                                       |
|-----------------------------------------------|--------------------------------------------------------|
| ![tulips.png](test_images/tulips.png)         | ![tulips_mosaico.png](data/tulips_mosaico.png)         |
| ![boat_color.bmp](test_images/boat_color.bmp) | ![boat_color_mosaico.png](data/boat_color_mosaico.png) |
| ![goldhill.bmp](test_images/goldhill.bmp)     | ![goldhill_mosaico.png](data/goldhill_mosaico.png)     |
| ![arc2.png](test_images/arc2.png)             | ![arc2_mosaico.png](data/arc2_mosaico.png)             |