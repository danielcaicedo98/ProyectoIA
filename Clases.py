class Casilla:
    def __init__(self, tieneHidrante, tieneFuego, solido, litros, posicion):
        self.tieneHidrante = tieneHidrante
        self.tieneFuego = tieneFuego
        self.solido = solido
        self.litros = litros
        self.posicion = posicion
        

    def imprimirAtributos(self):
        print("Tiene Hidrante:", self.tieneHidrante)
        print("Tiene Fuego:", self.tieneFuego)
        print("Es Sólido:", self.solido)
        print("Litros:", self.litros)
        print("Posición:", self.posicion)

    def getPosiciones(self):
        fila,columna = self.posicion
        return fila,columna;


class Bombero:
    def __init__(self, litrosCargados, posicion, cubeta):
        self.litrosCargados = litrosCargados
        self.posicion = posicion
        self.cubeta = cubeta

    def apagarFuego(self):
        if self.litrosCargados > 0:
            self.litrosCargados -= 1

    def imprimirPosicion(self):
        x, y = self.posicion
        print(f"Posición X: {x}, Posición Y: {y}")

    def getPosiciones(self):
        fila,columna = self.posicion
        return fila,columna;

    def setPosiciones(self, newPosicion):
        self.posicion = newPosicion

    def setLitros(self, cantidad):
        self.litrosCargados = cantidad

    def getLitros(self):
        return self.litrosCargados
    
    def getCubeta(self):
        return self.cubeta
    
    def setCubeta(self, newCubeta):
        self.cubeta = newCubeta

    def quitarLitro(self):
        if self.litrosCargados == 0:
            print("Debe buscar más Agua")
        else:
            self.litrosCargados -= 1

    def cuboVacio(self):
        if self.getCubeta()[0] == True and self.litrosCargados == 0:
            return True
        else:
            return False
        

class Nodo:
    def __init__(self, posicion, padre, operador, profundidad, costo):
        self.posicion = posicion
        self.padre = padre
        self.operador = operador
        self.profundidad = profundidad
        self.costo = costo

    def getProfundidad(self):
        self.profundidad = self.calcular_profundidad(self)
        print(f"La profundidad del nodo es {self.profundidad}")

    def operador(self):
        print(f"El operador usado para llegar a este nodo fue {self.operador}")

    def calcular_profundidad(self):
        profundidad = 0
        actual = self
        while actual.padre is not None:
            profundidad += 1
            actual = actual.padre
        return profundidad
    
    def recorrerCamino(self):
        camino = [self.posicion]
        nodo_actual = self

        while nodo_actual.padre is not None:
            nodo_actual = nodo_actual.padre
            camino.append(nodo_actual.posicion)

        camino.reverse()
        return camino
    

    def getPosicion(self):
        return self.posicion
    
    def getMovimiento(self):
        return self.operador

