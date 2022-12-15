from diferencias import *

def main():
    # Leemos el tamaño de la ventana
    ventana = int(input('Tamaño de la ventana: '))
    # Leemos la secuencia de referencia
    secuencia_referencia = input('Secuencia de referencia: ')
    # Leemos la secuencia de la variante
    secuencia_variante = input('Secuencia de la variante: ')
    # Obtenemos las diferencias entre las secuencias
    diferencias = identificar_diferencias(secuencia_variante, secuencia_referencia, ventana)
    # Mostramos las diferencias
    for i, diferencia in enumerate(diferencias):
        # Convertimos el índice en entero para poder sumarle 1 y obtener la posición
        diferencia['posicion'] = int(diferencia['posicion']) + 1
        # Mostramos la diferencia actual en pantalla con un formato legible para el usuario final (1-based)
        print(f"Diferencia {i + 1}:")
        print(f"Posición: {diferencia['posicion']}")
        print(f"Referencia: {diferencia['referencia']}")
        print(f"Variante: {diferencia['variante']}")
        print(f"Distancia: {diferencia['distancia']}")
        print()
        
main()