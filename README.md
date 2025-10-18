## Trabajo Práctico - Image Processing

### Objetivo

El objetivo del proyecto es desarrollar un sistema de procesamiento de imágenes que permita aplicar distintos filtros visuales de manera configurable.  
El usuario puede elegir entre dos filtros principales:

- **Voronoi**: genera una representación de la imagen mediante celdas construidas a partir de puntos semilla.
- **Mosaico**: transforma la imagen en bloques (tiles) tomando el color promedio de cada región.

Cada filtro cuenta con sus propios parámetros de entrada, los cuales el usuario puede ajustar para experimentar con diferentes configuraciones y resultados.

### Ejemplo de uso — Filtro Mosaico

Con los siguientes parámetros de entrada:

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
| ![tulips.png](test_images/tulips.png)         | ![tulips_mosaico.png](data1/tulips_mosaico.png)  |
| ![boat_color.bmp](test_images/boat_color.bmp) | ![boat_color_mosaico.png](data1/boat_color_mosaico.png)   |
| ![goldhill.bmp](test_images/goldhill.bmp)     | ![goldhill_mosaico.png](data1/goldhill_mosaico.png)         |
| ![arc2.png](test_images/arc2.png)             | ![arc2_mosaico.png](data1/arc2_mosaico.png) |