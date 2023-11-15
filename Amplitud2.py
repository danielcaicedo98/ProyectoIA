from collections import deque
from Clases import *
from Funciones import *

global posHidrante
global nodoPadreActual
global nodoCreado
global nodoDestino
global listaNodos
global listaMovimientosAmplitud

def getListaMovimientos():
    return listaMovimientosAmplitud

listaMovimientosAmplitud = []
#Esta función lee el mapa y me genera las casillas y el bombero
def cicloBombero(mapa):
    global nodoPadreActual
    global listaNodos
    casillas, bombero = crearPosiciones(mapa)
    reiniciarListaNodos(bombero)

    algoritmoAmplitud(casillas,bombero,mapa)

def algoritmoAmplitud(casillas, bombero: Bombero, mapa):

    global posHidrante
    global nodoDestino
    global listaNodos
    global nodoPadreActual
    global listaMovimientosAmplitud

    if(len(listaNodos) > 1):
        listaNodos = []

    fila,columna = bombero.getPosiciones()
    tuplaPosicionBombero = [(fila, columna)]
    cola = deque(tuplaPosicionBombero)
    colaDespuesBusqueda = busqueda(cola, mapa)

    posicionesFuegos = posicionesDelObjeto("Fuego", casillas)
    posicionesHidrantes = posicionesDelObjeto("Hidrante", casillas)
    posicionesCubetas = posicionesDelObjeto("Cubetas", casillas)

    if not bombero.getCubeta()[0]:
        posicionBalde = buscarCelda(mapa,colaDespuesBusqueda, posicionesCubetas)
        nodoDestino = encontrarNodo(listaNodos,tuple(posicionBalde))
        nuevoMapa, bomberoCambiado = actualizarMapa(mapa, posicionBalde, bombero)
        casillas, _ = crearPosiciones(nuevoMapa)
        print("MAPA")
        mostrarMapa(nuevoMapa)

        print("Camino Cubeta: ", nodoDestino.recorrerCamino())

        listaMovimientosAmplitud.append(nodoDestino.recorrerCamino())

        listaNodos = []
        nodoPadreActual = Nodo(bomberoCambiado.getPosiciones(),None, None, 0, 1)
        listaNodos.append(nodoPadreActual)
        algoritmoAmplitud(casillas,bomberoCambiado,nuevoMapa)

    elif(bombero.getLitros() > 0):
        nodoPadreActual = Nodo(bombero.getPosiciones(),None, None, 0, 1)
        listaNodos.append(nodoPadreActual)

        posicionFuego = buscarCelda(mapa,colaDespuesBusqueda, posicionesFuegos)

        nodoDestino = encontrarNodo(listaNodos,tuple(posicionFuego))

        nuevoMapa, bomberoCambiado = actualizarMapa(mapa, posicionFuego, bombero)
        nuevoMapa[posHidrante[0]][posHidrante[1]] = 6
        casillas, _ = crearPosiciones(nuevoMapa)

        if(len(posicionesFuegos) == 0):
            print("FINALICÉ TODO")
            mostrarMapa(nuevoMapa)  
        else:
            print("Camino Fuegos: ", nodoDestino.recorrerCamino())
            listaMovimientosAmplitud.append(nodoDestino.recorrerCamino())
            print("\nLista movimientos 1: ", listaMovimientosAmplitud)
            reiniciarListaNodos(bomberoCambiado)
            algoritmoAmplitud(casillas,bomberoCambiado,nuevoMapa)
    else:
        nodoPadreActual = Nodo(bombero.getPosiciones(),None, None, 0, 1)
        listaNodos.append(nodoPadreActual)


        posHidrante = posicionesHidrantes[0]
        posicionHidrante = buscarCelda(mapa,colaDespuesBusqueda, posicionesHidrantes)
        nodoDestino = encontrarNodo(listaNodos,tuple(posicionHidrante))
        nuevoMapa, bomberoCambiado = actualizarMapa(mapa, posicionHidrante, bombero)
        casillas, _ = crearPosiciones(nuevoMapa)



        if(len(posicionesFuegos) == 0):
            print("Camino Hidrante: ", nodoDestino.recorrerCamino())
            listaMovimientosAmplitud.append(nodoDestino.recorrerCamino())
            print("FINALICÉ TODO")
            mostrarMapa(nuevoMapa)    
        else:
            print("Camino Hidrante: ", nodoDestino.recorrerCamino())
            listaMovimientosAmplitud.append(nodoDestino.recorrerCamino())
            print("\nLista movimientos 1: ", listaMovimientosAmplitud)
            reiniciarListaNodos(bomberoCambiado)
            algoritmoAmplitud(casillas,bomberoCambiado,nuevoMapa)

    return 0
    

#Esta funciones se pueden usar en todos los metodos

def reiniciarListaNodos(bomberoCambiado: Bombero):
    global listaNodos
    listaNodos = []
    nodoPadreActual = Nodo(bomberoCambiado.getPosiciones(),None, None, 0, 1)
    listaNodos.append(nodoPadreActual)


def busqueda(cola, mapa):
    global nodoPadreActual
    global nodoCreado
    global listaNodos

    elementosPrimero = obtenerElementosDelPrimero(cola)
    nodoPadreActual = encontrarNodo(listaNodos,tuple(elementosPrimero))
    listaDisponible, listaCords = preguntarPorCasillasCercanas(elementosPrimero, mapa)
    resultadoFiltrado = filtrarDisponibles(listaDisponible, listaCords)
    agregarElementosCola(cola, resultadoFiltrado)

    return cola;
    

def filtrarDisponibles(disponible,posiciones):
    resultado = []
    for tupla in posiciones:
        posicion = posiciones.index(tupla)  
        if disponible[posicion] in [0, 3, 2, 6]:
            resultado.append(tupla)
            crearNodo(tupla, posicion)
    return resultado


def crearNodo(posicion, direccion):
    global nodoCreado
    global nodoPadreActual
    global listaNodos

    movimiento= ""
    if(direccion == 0):
        movimiento = "←←←←←←"
    if(direccion == 1):
        movimiento = "↓↓↓↓↓↓"
    if(direccion == 2):
        movimiento = "→→→→→→"
    if(direccion == 3):
        movimiento = "↑↑↑↑↑↑"

    nodoCreado = Nodo(posicion,nodoPadreActual, movimiento, 0, 1)
    listaNodos.append(nodoCreado)


def buscarCelda(mapa, posiciones, destino):
    global nodoDestino 
    global nodoCreado
    global nodoPadreActual
    global listaNodos
    colaDespuesBusqueda = busqueda(posiciones, mapa)

    if encuentraPosicion(posiciones,destino):
        posicionesActual = posiciones[0]
        nodoDestino = Nodo(posicionesActual,nodoPadreActual, "Llegada", 0, 1)
        return posicionesActual
    else:
        posicionesActual = buscarCelda(mapa, colaDespuesBusqueda,destino)
        return posicionesActual





