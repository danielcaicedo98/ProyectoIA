#import numpy as np

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")  
        print()
    print("\n")


def encontrar2(matriz):
    for fila, lista in enumerate(matriz):
        for columna, elemento in enumerate(lista):
            if elemento == 5:
                #print("Fila: ", fila, " Columna: ", columna)
                return(fila, columna)

    return None 

def posicionDisponible(matriz, fila, columna):
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
        return matriz[fila][columna]
    else:
        return 1


def preguntarPorCasillasCercanas(posicion, mapa):
    arriba = posicionDisponible(mapa,posicion[0] - 1,posicion[1])
    abajo = posicionDisponible(mapa,posicion[0] + 1,posicion[1])
    izquierda = posicionDisponible(mapa,posicion[0],posicion[1] - 1)
    derecha = posicionDisponible(mapa,posicion[0],posicion[1] + 1)

    return([izquierda,arriba,derecha,abajo])

def conocerDireccion(condiciones, raton):
    coincidencias = []
    for subarray in condiciones:
        if subarray[:4] == raton:
            coincidencias.append(subarray)

    if(coincidencias == []):
        coincidencias = [[0,0,0,0,1,5]]

    #print("Posición Raton: ", raton)
    #print("Coincidencias: ", coincidencias)
    return coincidencias[0]


def cambiarPosicionRaton(mapa,condicionActualRaton, posicionRaton):
    fila = posicionRaton[0]
    columna = posicionRaton[1]

    #print("Posición Raton: ", posicionRaton)
    imprimir_matriz(mapa)
    #print("Condicion Actual Raton: ", condicionActualRaton)

    if(condicionActualRaton[5] == 1):
        mapa[fila][columna] = 0
        mapa[fila - 1][columna] = 2
    elif(condicionActualRaton[5] == 2):
        mapa[fila][columna] = 0
        mapa[fila][columna - 1] = 2
    elif(condicionActualRaton[5] == 3):
        mapa[fila][columna] = 0
        mapa[fila][columna + 1] = 2
    elif(condicionActualRaton[5] == 5):
        print("Hola")
    else:
        mapa[fila][columna] = 0
        mapa[fila + 1][columna] = 2

    imprimir_matriz(mapa)
    return mapa


def cicloDelRaton(mapa):

    fila, columna = encontrar2(mapa)
    posicionRaton = [fila, columna]

    casillasCercanas = preguntarPorCasillasCercanas(posicionRaton,mapa)

    condiciones = "./Condiciones.txt"
    with open(condiciones, "r") as condiciones:
        ambiente = []
        for linea in condiciones:
            condicionActual = [int(numero) for numero in linea.split()]
            ambiente.append(condicionActual)

        condicionActualRaton = conocerDireccion(ambiente,casillasCercanas)

        if(condicionActualRaton[4] == 1):
            print("Haz encontrado el Quezo")
        
        else:
            print("----------Nuevo Ciclo-----------")
            nuevoMapa = cambiarPosicionRaton(mapa, condicionActualRaton, posicionRaton)
            cicloDelRaton(nuevoMapa)


mapaTXT = "./Prueba1.txt"


print(" SOLUCIÓN PROGRAMA RATON ")

    


with open(mapaTXT, "r") as archivo:
    mapa = []
    for linea in archivo:
        lista_de_numeros = [int(numero) for numero in linea.split()]
        mapa.append(lista_de_numeros)

    print("\n\nMAPA INICIAL\n")
    imprimir_matriz(mapa)
    
    cicloDelRaton(mapa)







