import numpy as np

def mosaico(img, variance_threshold, min_size, max_passes, bordes, height, width):

    """ Aplica el filtro mosaico subdividiendo iterativamente.
    """
    area_a_procesar = [(0,0,height,width)] #lista de areas a chequear, que seria el area total de la img

    area_final = [] #las areas que ya no se van a dividir mas

    for _ in range(max_passes): #subdividir segun los max_passes
        area_aca = area_a_procesar 
        area_a_procesar = [] #vaciar para llenarla con los nuevos cuadrantes

        for y0, x0, y1, x1 in area_aca: #para calcular las areas
            height_area = y1 - y0
            width_area = x1 - x0
            area_actual = img[y0:y1, x0:x1] #esta seria la matriz de pixeles del area actual
            varianza = calcular_varianza_rgb(area_actual)
            subdividir = (varianza > variance_threshold and min(height_area, width_area) > min_size) #criterio para dividir o no

            if subdividir: #si divido calculo el punto medio y agregamos 4 nuevos cuadrantes a la lista para la proxima iteracion
                mitad_width = x0 + width_area // 2
                mitad_height = y0 + height_area // 2
                area_a_procesar.append((y0, x0, mitad_height, mitad_width)) #NW
                area_a_procesar.append((y0, mitad_width, mitad_height, x1)) #NE
                area_a_procesar.append((mitad_height, x0, y1, mitad_width)) #SW
                area_a_procesar.append((mitad_height, mitad_width, y1, x1)) #SE

            else: #si no divido entonces es un area final y lo guardo
                area_final.append((y0, x0, y1, x1, area_actual))

        if not area_a_procesar: #si ya no hay mas para dividir termino!
            break

    for y0, x0, y1, x1 in area_a_procesar: #si terminaron los max_passes hay que rellenar lo que conseguimos y lo que fheight
        area_actual = img[y0: y1, x0: x1]
        area_final.append((y0, x0, y1, x1, area_actual))

    resultado_img = img.copy() #hacer una copia para que el resultado quede por encima

    for y0, x0, y1, x1, area_actual in area_final:
        color = color_promedio(area_actual)
        resultado_img[y0: y1, x0: x1] = color #relleno el area con el color promedio
        if bordes: #para dibujar los contornos (?
            negro = np.array([0,0,0], dtype = np.uint8)
            #bordes horizontales (y)
            resultado_img[y0: y0 +1, x0: x1] = negro #arriba
            resultado_img[y1 -1: y1, x0: x1] = negro #abajo
            #bordes verticales (x)
            resultado_img[y0: y1, x0: x0 +1] = negro #izquierda
            resultado_img[y0: y1, x1 -1: x1] = negro #derecha

    return resultado_img

def calcular_varianza_rgb(area):
    """ Calcula el RGB promedio de un area de pixeles. El area es un array tridimensional: filas
    de la img, columnas de la img, 3 colores (rojo, verde, azul).
    """
    if area.size == 0:
        return 0
    #uso np.var para calcular la varianza de cada fila, columna y color por separado
    varianzas_de_area = np.var(area, axis = (0,1)) #el eje 0 es el height (filas) y el 1 es el width (columnas)
    return np.mean(varianzas_de_area) #retornar el promedio de esas varianzas
    #si este número es height el área tiene MUCHO detalle y hay que dividirla

def color_promedio(area):
    """ Calcula el color promedio de un area de pixeles.
    """
    if area.size == 0:
        return np.array([0, 0, 0], dtype = np.uint8) #si el area esta vacia devuelve negro
    color_promedio = np.mean(area, axis = (0,1)).astype(np.uint8) #calcular el promedio del rgb y que se cumpla el color 0 a 255
    return color_promedio