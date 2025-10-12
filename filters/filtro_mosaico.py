
#juli filtro mosaico

import numpy as np

def filtro_mosaico(imagen, variance_threshold = 150.0, min_size = 20, max_passes = 10, bordes = True):
    """ Aplica el filtro mosaico subdividiendo iterativamente.
    """
    alto, ancho, _ = imagen.shape #uso funciones de numpy para tener las dimensiones alto (y) y ancho (x) de la imagen
    area_a_procesar = [(0,0,alto,ancho)] #lista de areas a chequear, que seria el area total de la imagen
    area_final = [] #las areas que ya no se van a dividir mas
    for _ in range(max_passes): #subdividir segun los max_passes
        area_aca = area_a_procesar 
        area_a_procesar = [] #vaciar para llenarla con los nuevos cuadrantes
        for alto_inicio, ancho_inicio, alto_final, ancho_final in area_aca: #para calcular las areas
            alto_area = alto_final - alto_inicio
            ancho_area = ancho_final - ancho_inicio
            area_actual = imagen[alto_inicio:alto_final, ancho_inicio:ancho_final] #esta seria la matriz de pixeles del area actual
            varianza = calcular_varianza_rgb(area_actual)
            subdividir = (varianza > variance_threshold and min(alto_area, ancho_area) > min_size) #criterio para dividir o no
            if subdividir: #si divido calculo el punto medio y agregamos 4 nuevos cuadrantes a la lista para la proxima iteracion
                mitad_ancho = ancho_inicio + ancho_area // 2
                mitad_alto = alto_inicio + alto_area // 2
                area_a_procesar.append((alto_inicio, ancho_inicio, mitad_alto, mitad_ancho)) #NW
                area_a_procesar.append((alto_inicio, mitad_ancho, mitad_alto, ancho_final)) #NE
                area_a_procesar.append((mitad_alto, ancho_inicio, alto_final, mitad_ancho)) #SW
                area_a_procesar.append((mitad_alto, mitad_ancho, alto_final, ancho_final)) #SE
            else: #si no divido entonces es un area final y lo guardo
                area_final.append((alto_inicio, ancho_inicio, alto_final, ancho_final, area_actual))
        if not area_a_procesar: #si ya no hay mas para dividir termino!
            break
    for alto_inicio, ancho_inicio, alto_final, ancho_final in area_a_procesar: #si terminaron los max_passes hay que rellenar lo que conseguimos y lo que falto
        area_actual = imagen[alto_inicio: alto_final, ancho_inicio: ancho_final]
        area_final.append((alto_inicio, ancho_inicio, alto_final, ancho_final, area_actual))
    resultado_imagen = imagen.copy() #hacer una copia para que el resultado quede por encima
    for alto_inicio, ancho_inicio, alto_final, ancho_final, area_actual in area_final:
        color = color_promedio(area_actual)
        resultado_imagen[alto_inicio: alto_final, ancho_inicio: ancho_final] = color #relleno el area con el color promedio
        if bordes: #para dibujar los contornos (?
            negro = np.array([0,0,0], dtype = np.uint8)
            #bordes horizontales (y)
            resultado_imagen[alto_inicio: alto_inicio +1, ancho_inicio: ancho_final] = negro #arriba
            resultado_imagen[alto_final -1: alto_final, ancho_inicio: ancho_final] = negro #abajo
            #bordes verticales (x)
            resultado_imagen[alto_inicio: alto_final, ancho_inicio: ancho_inicio +1] = negro #izquierda
            resultado_imagen[alto_inicio: alto_final, ancho_final -1: ancho_final] = negro #derecha
    return resultado_imagen


def calcular_varianza_rgb(area):
    """ Calcula el RGB promedio de un area de pixeles. El area es un array tridimensional: filas
    de la imagen, columnas de la imagen, 3 colores (rojo, verde, azul).
    """
    if area.size == 0:
        return 0
    #uso np.var para calcular la varianza de cada fila, columna y color por separado
    varianzas_de_area = np.var(area, axis = (0,1)) #el eje 0 es el alto (filas) y el 1 es el ancho (columnas)
    return np.mean(varianzas_de_area) #retornar el promedio de esas varianzas
    #si este número es alto el área tiene MUCHO detalle y hay que dividirla

def color_promedio(area):
    """ Calcula el color promedio de un area de pixeles.
    """
    if area.size == 0:
        return np.array([0, 0, 0], dtype = np.uint8) #si el area esta vacia devuelve negro
    color_promedio = np.mean(area, axis = (0,1)).astype(np.uint8) #calcular el promedio del rgb y que se cumpla el color 0 a 255
    return color_promedio


