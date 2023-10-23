# def encontrar_posiciones_ordenadas(matriz, numero, objetivo):
#     posiciones = []
    
#     # Buscar todas las ocurrencias del número en la matriz y guardar sus posiciones
#     for fila in range(len(matriz)):
#         for columna in range(len(matriz[fila])):
#             if matriz[fila][columna] == numero:
#                 posiciones.append((fila, columna))
    
#     if not posiciones:
#         return None  # El número no está en la matriz

#     # Ordenar las posiciones por cercanía al objetivo
#     posiciones_ordenadas = sorted(posiciones, key=lambda pos: abs(pos[1] - objetivo))

#     return posiciones_ordenadas

# # Ejemplo de uso
# matriz = [
#     [1, 2, 3],
#     [4, 5, 2],
#     [2, 7, 8]
# ]

# numero_a_buscar = 2
# posicion_objetivo = 1

# posiciones_ordenadas = encontrar_posiciones_ordenadas(matriz, numero_a_buscar, posicion_objetivo)
# print("Las posiciones de", numero_a_buscar, "ordenadas por cercanía a", posicion_objetivo, "son:", posiciones_ordenadas)


def calcular_distancia_manhattan(punto1, punto2):
    return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])

def encontrar_distancia_manhattan_al_mas_cercano(matriz, primer_numero, segundo_numero):
    posiciones_primer_numero = []
    posiciones_segundo_numero = []
    
    # Buscar todas las ocurrencias de los números en la matriz y guardar sus posiciones
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == primer_numero:
                posiciones_primer_numero.append((fila, columna))
            elif matriz[fila][columna] == segundo_numero:
                posiciones_segundo_numero.append((fila, columna))
    
    if not posiciones_primer_numero or not posiciones_segundo_numero:
        return None  # Uno de los números no está en la matriz

    distancia_minima = float('inf')

    # Calcular la distancia Manhattan entre el primer número y los segundos números
    for posicion_primer_numero in posiciones_primer_numero:
        for posicion_segundo_numero in posiciones_segundo_numero:
            distancia = calcular_distancia_manhattan(posicion_primer_numero, posicion_segundo_numero)
            distancia_minima = min(distancia, distancia_minima)

    return distancia_minima

# Ejemplo de uso
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [3, 1, 8],
    [3, 7, 8],
    [3, 7, 9]
]

primer_numero = 1
segundo_numero = 9

distancia_manhattan_mas_cercana = encontrar_distancia_manhattan_al_mas_cercano(matriz, primer_numero, segundo_numero)
print("La distancia Manhattan desde", primer_numero, "hasta el segundo número más cercano es:", distancia_manhattan_mas_cercana)
