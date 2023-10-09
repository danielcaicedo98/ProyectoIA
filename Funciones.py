from Clases import Bombero
from Clases import Casilla
from Clases import Nodo



def mostrarMapa(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")  
        print()
    print("\n")

def crearPosiciones(matriz):
    listaObjetos = []
    bombero =0
    for fila, lista in enumerate(matriz):
        for columna, elemento in enumerate(lista):
            objetoActual = crearObjetos(elemento,fila, columna)[0]

            if elemento == 5:
                bombero = Bombero(0, (fila, columna), [False,0])

            listaObjetos.append(objetoActual)

    return(listaObjetos, bombero)



#tieneHidrante, tieneFuego, solido litros, posición
def crearObjetos(tipoCasilla, fila, columna):
    configuraciones = {
        0: (False, False, False, 0, [fila, columna]),
        1: (False, False, True, 0, [fila, columna]),
        2: (False, True, False, 0, [fila, columna]),
        3: (False, False, False, 1, [fila, columna]),
        4: (False, False, False, 2, [fila, columna]),
        5: (False, False, False, 0, [fila, columna]),
        6: (True, False, False, 0, [fila, columna])
    }

    listaDePosiciones = []
    bombero = 0

    if tipoCasilla in configuraciones:
        argumentosCasilla = configuraciones[tipoCasilla]
        casilla = Casilla(*argumentosCasilla)
        listaDePosiciones.append(casilla)
    return listaDePosiciones;


def actualizarMapa(mapaAntiguo, posicion, bombero: Bombero):
    filaB, columnaB = posicion

    for fila_idx, fila in enumerate(mapaAntiguo):
        for columna_idx, elemento in enumerate(fila):
            if(elemento == 5 and [filaB, columnaB] != [fila_idx,columna_idx]):
                mapaAntiguo[fila_idx][columna_idx] = 0     
            elif(mapaAntiguo[filaB][columnaB] in (6,4,2,3)):
                nuevoBombero = asignarLitrosAguaBombero(mapaAntiguo[filaB][columnaB],bombero)
                mapaAntiguo[filaB][columnaB] = 5
                nuevoBombero.setPosiciones(posicion)

    return mapaAntiguo, nuevoBombero



def asignarLitrosAguaBombero(casilla,bombero: Bombero):
    if (casilla == 3):
        bombero.setCubeta([True,1])
        return bombero
    elif (casilla == 4):
        bombero.setCubeta([True,2])
        return bombero
    elif(casilla == 2):
        bombero.quitarLitro()
        return bombero
    elif(casilla == 6):
        bombero.setLitros(bombero.getCubeta()[1])
        return bombero

    return bombero

def encontrarNodo(lista, posicion):
    for nodo in lista:
        if nodo.getPosicion() == posicion:
            return nodo
    return None  # Retorna None si no se encuentra el nodo



def preguntarPorCasillasCercanas(posicion, mapa):
    direcciones = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # Izquierda, Abajo, Derecha, Arriba
    listaDisponible = []
    listaCords = []

    for direccion in direcciones:
        fila, columna = posicion[0] + direccion[0], posicion[1] + direccion[1]
        listaCords.append((fila, columna))

        if 0 <= fila < len(mapa) and 0 <= columna < len(mapa[0]):
            listaDisponible.append(mapa[fila][columna])
        else:
            listaDisponible.append(1)  # Valor para posiciones fuera de rango

    return listaDisponible, listaCords


def posicionDisponible(matriz, fila, columna):
    if 0 <= fila < len(matriz) and 0 <= columna < len(matriz[0]):
        return matriz[fila][columna]
    else:
        return 1
    

def obtenerElementosDelPrimero(cola):
    if cola:
        primer_elemento = cola[0]
        if isinstance(primer_elemento, tuple) and len(primer_elemento) == 2:
            return list(primer_elemento)
    return None



def encuentraPosicion(cola, destinos):
    if cola and cola[0] in destinos:
        return True
    return False


def posicionesDelObjeto(objeto,casillas: Casilla):

    if(objeto == "Cubetas"):
        seleccionadas = [casilla for casilla in casillas if casilla.litros in (1, 2)]
    elif(objeto == "Hidrante"):
        seleccionadas = [casilla for casilla in casillas if casilla.tieneHidrante == True]
    elif(objeto == "Fuego"):
        seleccionadas = [casilla for casilla in casillas if casilla.tieneFuego == True]
    posiciones = []

    # Recorremos la lista de casillas y agregamos las posiciones a la lista
    for casilla in seleccionadas:
        posiciones.append((casilla.getPosiciones()))

    return posiciones



def agregarElementosCola(cola, elementos):
    cola.popleft()
    elementos_agregados = set()
    for elemento in elementos:
        if elemento not in elementos_agregados:
            cola.append(elemento)
            elementos_agregados.add(elemento)