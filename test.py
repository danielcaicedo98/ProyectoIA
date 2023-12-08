import random

def encontrar_posicion_vacia(matriz):
    posiciones_vacias = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                posiciones_vacias.append((i, j))
    return posiciones_vacias

def colocar_tres_cuatro(matriz):
    posiciones_vacias = encontrar_posicion_vacia(matriz)
    
    random.shuffle(posiciones_vacias)
    
    posicion_tres = None
    posicion_cuatro = None
    
    for pos in posiciones_vacias:
        i, j = pos
        if i > 0 and matriz[i - 1][j] != 1 and matriz[i - 1][j] != 2:
            posicion_tres = pos
            break
    
    for pos in posiciones_vacias:
        i, j = pos
        if i > 0 and matriz[i - 1][j] != 1 and matriz[i - 1][j] != 2 and pos != posicion_tres:
            posicion_cuatro = pos
            break
    
    if posicion_tres is not None and posicion_cuatro is not None:
        matriz[posicion_tres[0]][posicion_tres[1]] = 3
        matriz[posicion_cuatro[0]][posicion_cuatro[1]] = 4
    
    return matriz

def escribir_matriz_en_archivo(matriz, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for fila in matriz:
            fila_texto = ' '.join(map(str, fila)) + '\n'
            archivo.write(fila_texto)

matriz = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1]
]

resultado = colocar_tres_cuatro(matriz)
escribir_matriz_en_archivo(resultado, 'Prueba1.txt')


# import random

# def encontrar_posicion_vacia(matriz):
#     posiciones_vacias = []
#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if matriz[i][j] == 0:
#                 posiciones_vacias.append((i, j))
#     return posiciones_vacias

# def colocar_tres_cuatro(matriz):
#     posiciones_vacias = encontrar_posicion_vacia(matriz)
    
#     random.shuffle(posiciones_vacias)
    
#     posicion_tres = None
#     posicion_cuatro = None
    
#     for pos in posiciones_vacias:
#         i, j = pos
#         if i > 0 and matriz[i - 1][j] != 1 and matriz[i - 1][j] != 2:
#             posicion_tres = pos
#             break
    
#     for pos in posiciones_vacias:
#         i, j = pos
#         if i > 0 and matriz[i - 1][j] != 1 and matriz[i - 1][j] != 2 and pos != posicion_tres:
#             posicion_cuatro = pos
#             break
    
#     if posicion_tres is not None and posicion_cuatro is not None:
#         matriz[posicion_tres[0]][posicion_tres[1]] = 3
#         matriz[posicion_cuatro[0]][posicion_cuatro[1]] = 4
    
#     return matriz

# matriz = [
#     [1, 3, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 4, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1]
# ]

# resultado = colocar_tres_cuatro(matriz)
# for fila in resultado:
#     print(fila)


# def distancia_manhattan(p1, p2):
#     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# def encontrar_posicion_mas_cercana(matriz, fila, columna):
#     uno_o_dos_encontrado = False
#     distancia_mas_cercana = float('inf')
#     posicion_mas_cercana = None

#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if matriz[i][j] == 1 or matriz[i][j] == 2:
#                 uno_o_dos_encontrado = True
#                 dist = distancia_manhattan((fila, columna), (i, j))
#                 if dist < distancia_mas_cercana:
#                     distancia_mas_cercana = dist
#                     posicion_mas_cercana = (i, j)

#     return uno_o_dos_encontrado, posicion_mas_cercana

# def encontrar_mejor_movimiento_en_L(matriz, fila, columna, fila_previa, columna_previa, visitados):
#     movimientos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
#     uno_o_dos_cercano, posicion_mas_cercana = encontrar_posicion_mas_cercana(matriz, fila, columna)

#     if not uno_o_dos_cercano:
#         return None

#     mejor_movimiento = None
#     mejor_distancia = float('inf')

#     for mov in movimientos:
#         nueva_fila = fila + mov[0]
#         nueva_columna = columna + mov[1]

#         if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]) and (nueva_fila, nueva_columna) != (fila_previa, columna_previa) and (nueva_fila, nueva_columna) not in visitados:
#             dist = distancia_manhattan((nueva_fila, nueva_columna), posicion_mas_cercana)
#             if dist < mejor_distancia:
#                 mejor_distancia = dist
#                 mejor_movimiento = (nueva_fila, nueva_columna)

#     return mejor_movimiento

# def encontrar_camino_hacia_1_o_2(matriz, fila_inicial, columna_inicial, posiciones_evitar):
#     visitados = set(posiciones_evitar)
#     camino = [(fila_inicial, columna_inicial)]

#     fila_previa = None
#     columna_previa = None

#     while True:
#         movimiento = encontrar_mejor_movimiento_en_L(matriz, camino[-1][0], camino[-1][1], fila_previa, columna_previa, visitados)
#         if movimiento is None:
#             break
#         visitados.add(movimiento)
#         camino.append(movimiento)
#         fila_previa, columna_previa = camino[-2]

#         if matriz[movimiento[0]][movimiento[1]] == 1 or matriz[movimiento[0]][movimiento[1]] == 2:
#             break

#     return camino

# # Ejemplo de uso
# # Matriz de ejemplo
# matriz = [
#     [1, 3, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 4, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1]
# ]

# # Punto de inicio y búsqueda del mejor camino en L hacia un 1 o un 2 evitando ciertas posiciones
# fila_inicial = 0
# columna_inicial = 1

# posiciones_a_evitar = [(1, 2), (2, 3)]  # Lista de posiciones que deben ser evitadas

# mejor_camino_hacia_1_o_2 = encontrar_camino_hacia_1_o_2(matriz, fila_inicial, columna_inicial, posiciones_a_evitar)
# print(f"El mejor camino hacia un 1 o un 2 evitando ciertas posiciones es: {mejor_camino_hacia_1_o_2}")


# def distancia_manhattan(p1, p2):
#     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# def encontrar_posicion_mas_cercana(matriz, fila, columna):
#     uno_o_dos_encontrado = False
#     distancia_mas_cercana = float('inf')
#     posicion_mas_cercana = None

#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if matriz[i][j] == 1 or matriz[i][j] == 2:
#                 uno_o_dos_encontrado = True
#                 dist = distancia_manhattan((fila, columna), (i, j))
#                 if dist < distancia_mas_cercana:
#                     distancia_mas_cercana = dist
#                     posicion_mas_cercana = (i, j)

#     return uno_o_dos_encontrado, posicion_mas_cercana

# def encontrar_mejor_movimiento_en_L(matriz, fila, columna, fila_previa, columna_previa, visitados):
#     movimientos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
#     uno_o_dos_cercano, posicion_mas_cercana = encontrar_posicion_mas_cercana(matriz, fila, columna)

#     if not uno_o_dos_cercano:
#         return None

#     mejor_movimiento = None
#     mejor_distancia = float('inf')

#     for mov in movimientos:
#         nueva_fila = fila + mov[0]
#         nueva_columna = columna + mov[1]

#         if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]) and (nueva_fila, nueva_columna) != (fila_previa, columna_previa) and (nueva_fila, nueva_columna) not in visitados:
#             dist = distancia_manhattan((nueva_fila, nueva_columna), posicion_mas_cercana)
#             if dist < mejor_distancia:
#                 mejor_distancia = dist
#                 mejor_movimiento = (nueva_fila, nueva_columna)

#     return mejor_movimiento

# def encontrar_camino_hacia_1_o_2(matriz, fila_inicial, columna_inicial):
#     visitados = set()
#     camino = [(fila_inicial, columna_inicial)]

#     fila_previa = None
#     columna_previa = None

#     while True:
#         movimiento = encontrar_mejor_movimiento_en_L(matriz, camino[-1][0], camino[-1][1], fila_previa, columna_previa, visitados)
#         if movimiento is None:
#             break
#         visitados.add(movimiento)
#         camino.append(movimiento)
#         fila_previa, columna_previa = camino[-2]

#         if matriz[movimiento[0]][movimiento[1]] == 1 or matriz[movimiento[0]][movimiento[1]] == 2:
#             break

#     return camino

# # Ejemplo de uso
# # Matriz de ejemplo
# matriz = [
#     [0, 3, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1]
# ]

# # Punto de inicio y búsqueda del mejor camino en L hacia un 1 o un 2
# fila_inicial = 0
# columna_inicial = 1

# mejor_camino_hacia_1_o_2 = encontrar_camino_hacia_1_o_2(matriz, fila_inicial, columna_inicial)
# print(f"El mejor camino hacia un 1 o un 2 es: {mejor_camino_hacia_1_o_2}")

# def distancia_manhattan(p1, p2):
#     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# def encontrar_posicion_mas_cercana(matriz, fila, columna):
#     uno_o_dos_encontrado = False
#     distancia_mas_cercana = float('inf')
#     posicion_mas_cercana = None

#     for i in range(len(matriz)):
#         for j in range(len(matriz[0])):
#             if matriz[i][j] == 1 or matriz[i][j] == 2:
#                 uno_o_dos_encontrado = True
#                 dist = distancia_manhattan((fila, columna), (i, j))
#                 if dist < distancia_mas_cercana:
#                     distancia_mas_cercana = dist
#                     posicion_mas_cercana = (i, j)

#     return uno_o_dos_encontrado, posicion_mas_cercana

# def encontrar_mejor_movimiento_en_L(matriz, fila, columna, fila_previa, columna_previa):
#     movimientos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
#     uno_o_dos_cercano, posicion_mas_cercana = encontrar_posicion_mas_cercana(matriz, fila, columna)

#     if not uno_o_dos_cercano:
#         return None

#     mejor_movimiento = None
#     mejor_distancia = float('inf')

#     for mov in movimientos:
#         nueva_fila = fila + mov[0]
#         nueva_columna = columna + mov[1]

#         if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]) and (nueva_fila, nueva_columna) != (fila_previa, columna_previa):
#             dist = distancia_manhattan((nueva_fila, nueva_columna), posicion_mas_cercana)
#             if dist < mejor_distancia:
#                 mejor_distancia = dist
#                 mejor_movimiento = (nueva_fila, nueva_columna)

#     return mejor_movimiento

# # Ejemplo de uso
# # Matriz de ejemplo
# matriz = [
#     [1, 3, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1]
# ]

# # Punto de inicio y búsqueda del mejor movimiento en L
# fila_inicial = 2
# columna_inicial = 0

# fila_previa = 0
# columna_previa = 1

# mejor_movimiento = encontrar_mejor_movimiento_en_L(matriz, fila_inicial, columna_inicial, fila_previa, columna_previa)
# print(f"El mejor movimiento en L hacia el uno o dos más cercano es: {mejor_movimiento}")


# def sumatoria_beneficio(pocision, columna):
#     fila,columna = pocision
#     movimientos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
#     suma = 0

#     for mov in movimientos:
#         nueva_fila = fila + mov[0]
#         nueva_columna = columna + mov[1]

#         if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]):
#             if matriz[nueva_fila][nueva_columna] == 1 or matriz[nueva_fila][nueva_columna] == 2:
#                 suma += matriz[nueva_fila][nueva_columna]

#     return suma

# # Ejemplo de uso
# # Matriz de ejemplo
# matriz = [
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [3, 0, 0, 2, 2, 0, 0, 0],
#     [0, 0, 0, 2, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0, 4, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1]
# ]

# # Punto de ejemplo (2, 2)
# fila_ejemplo = 3
# columna_ejemplo = 3
# pos = (3,3)
# resultado = suma_uno_dos_alrededor(pos, columna_ejemplo)
# print(f"La suma de los valores 1 y 2 alrededor de la posición ({fila_ejemplo}, {columna_ejemplo}) es: {resultado}")



# # Función para comparar las matrices y reemplazar 0 por 5 si difiere de la primera matriz
# def comparar_matrices(matriz_modelo, segunda_matriz):
#     for i in range(len(matriz_modelo)):
#         for j in range(len(matriz_modelo[0])):
#             if matriz_modelo[i][j] in [1, 2] and segunda_matriz[i][j] == 0:
#                 segunda_matriz[i][j] = 5

# # Matrices modelo
# matriz_modelo = [
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [3, 0, 0, 2, 2, 0, 0, 0],
#     [0, 0, 0, 2, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0, 4, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1]
# ]

# # Segunda matriz
# segunda_matriz = [
#     [1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 3, 2, 0, 0, 0],
#     [0, 0, 0, 2, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0, 4, 0, 0],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 0, 0, 0, 0, 1, 0]
# ]

# # Llamada a la función para comparar las matrices y reemplazar los 0 por 5 si es necesario
# comparar_matrices(matriz_modelo, segunda_matriz)
# def imprimir_matriz(matriz):
#         for fila in matriz:
#             for elemento in fila:
#                 print(elemento, end=" ")  # Imprimir el elemento seguido de un espacio en la misma línea
#             print()  

# # Imprimir la segunda matriz actualizada
# print("Segunda matriz actualizada:")
# imprimir_matriz(segunda_matriz)
