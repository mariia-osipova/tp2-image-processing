## Image Processing — Practical Assignment

### Objective

The goal of this project is to develop an image processing system capable of applying different visual filters in a configurable way.  
The user can choose between two main filters:

- **Voronoi**: generates a representation of the image based on regions (cells) created from randomly distributed seed points.
- **Mosaic**: transforms the image into blocks (tiles), assigning each tile the average color of the pixels it contains.

Each filter includes adjustable input parameters, allowing the user to experiment with different configurations and visual results.

### Usage Example — Mosaic Filter

Using the following input parameters:

```python
variance_threshold = 150
min_size = 20
max_passes = 10
bordes = False
```

| Imagen original                    | Resultado procesado                                   |
|------------------------------------|-------------------------------------------------------|
| ![cablecar.bmp](test_images/cablecar.bmp) | ![cablecar_mosaico.png](data/cablecar_mosaico.png)    |
| ![cornfield.bmp](test_images/cornfield.bmp)  | ![cornfield_mosaico.png](data/cornfield_mosaico.png)  |
| ![flowers.bmp](test_images/flowers.bmp)  | ![flowers_mosaico.png](data/flowers_mosaico.png)      |
| ![boat.png](test_images/boat.png)  | ![boat_mosaico.png](data/boat_mosaico.png)            |

```python
variance_threshold = 100
min_size = 30
max_passes = 5
bordes = True
```

| Imagen original                               | Resultado procesado                                   |
|-----------------------------------------------|-------------------------------------------------------|
| ![tulips.png](test_images/tulips.png)         | ![tulips_mosaico.png](data/tulips_mosaico.png)  |
| ![boat_color.bmp](test_images/boat_color.bmp) | ![boat_color_mosaico.png](data/boat_color_mosaico.png)   |
| ![goldhill.bmp](test_images/goldhill.bmp)     | ![goldhill_mosaico.png](data/goldhill_mosaico.png)         |
| ![arc2.png](test_images/arc2.png)             | ![arc2_mosaico.png](data/arc2_mosaico.png) |