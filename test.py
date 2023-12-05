def sumatoria_beneficio(pocision, columna):
    fila,columna = pocision
    movimientos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
    suma = 0

    for mov in movimientos:
        nueva_fila = fila + mov[0]
        nueva_columna = columna + mov[1]

        if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]):
            if matriz[nueva_fila][nueva_columna] == 1 or matriz[nueva_fila][nueva_columna] == 2:
                suma += matriz[nueva_fila][nueva_columna]

    return suma

# Ejemplo de uso
# Matriz de ejemplo
matriz = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1]
]

# Punto de ejemplo (2, 2)
fila_ejemplo = 3
columna_ejemplo = 3
pos = (3,3)
resultado = suma_uno_dos_alrededor(pos, columna_ejemplo)
print(f"La suma de los valores 1 y 2 alrededor de la posición ({fila_ejemplo}, {columna_ejemplo}) es: {resultado}")



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
