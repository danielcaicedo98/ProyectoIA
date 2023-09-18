def encontrar_posicion(matriz, numero):
    # Encuentra la posición actual del número en la matriz
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == numero:
                return fila, columna
    return None

def mover_numero(matriz, numero, direccion):
    # Encuentra la posición actual del número
    posicion_actual = encontrar_posicion(matriz, numero)

    if not posicion_actual:
        return matriz  # Si no se encuentra el número, no se realiza ningún movimiento

    fila, columna = posicion_actual

    # Definir los desplazamientos para las cuatro direcciones
    desplazamientos = {
        "arriba": (-1, 0),
        "abajo": (1, 0),
        "izquierda": (0, -1),
        "derecha": (0, 1),
    }

    # Calcular la nueva posición
    desplazamiento = desplazamientos.get(direccion)
    if desplazamiento:
        nueva_fila = fila + desplazamiento[0]
        nueva_columna = columna + desplazamiento[1]

        # Verificar si la nueva posición está dentro de la matriz
        if (
            0 <= nueva_fila < len(matriz) and
            0 <= nueva_columna < len(matriz[nueva_fila]) and
            matriz[nueva_fila][nueva_columna] != 1

        ):
            # Mover el número a la nueva posición            
            matriz[fila][columna] = 0
            matriz[nueva_fila][nueva_columna] = numero
        else:
          print("Movimiento no permitido")
    return matriz

# Ejemplo de uso:
matriz = [
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 2, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
    [5, 0, 0, 6, 4, 0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [3, 0, 0, 0, 2, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 1, 0, 0, 0, 0]
]

# Mover el número 5 hacia la derecha
matriz = mover_numero(matriz, 5, "derecha")
matriz = mover_numero(matriz, 5, "arriba")
# Imprimir la matriz después del movimiento
for fila in matriz:
    print(fila)

