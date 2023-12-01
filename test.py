# Función para comparar las matrices y reemplazar 0 por 5 si difiere de la primera matriz
def comparar_matrices(matriz_modelo, segunda_matriz):
    for i in range(len(matriz_modelo)):
        for j in range(len(matriz_modelo[0])):
            if matriz_modelo[i][j] in [1, 2] and segunda_matriz[i][j] == 0:
                segunda_matriz[i][j] = 5

# Matrices modelo
matriz_modelo = [
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1]
]

# Segunda matriz
segunda_matriz = [
    [1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 2, 0, 0, 0],
    [0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 4, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0]
]

# Llamada a la función para comparar las matrices y reemplazar los 0 por 5 si es necesario
comparar_matrices(matriz_modelo, segunda_matriz)
def imprimir_matriz(matriz):
        for fila in matriz:
            for elemento in fila:
                print(elemento, end=" ")  # Imprimir el elemento seguido de un espacio en la misma línea
            print()  

# Imprimir la segunda matriz actualizada
print("Segunda matriz actualizada:")
imprimir_matriz(segunda_matriz)
