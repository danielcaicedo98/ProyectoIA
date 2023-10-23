import copy
import time
from Reader import get_matriz
tiempo_inicio = time.time()
def agente_a_estrella():
    
    matriz_inicial = get_matriz()

    cola_inicial = {
        "matriz":matriz_inicial,
        "costo": 0
    }
    cola = []
    nodos = []


    def encontrar_camino(ultimo_nodo):
        camino = []
        index = ultimo_nodo        
        while (index > 0):
            camino.append(nodos[index]["posicion"])
            index = nodos[index]["padre"]["nodo"]
        camino.append(nodos[index]["posicion"])
        camino.reverse()
        return camino


    def encontrar_posiciones_ordenadas(matriz, numero, objetivo):
        posiciones = []
        
        # Buscar todas las ocurrencias del número en la matriz y guardar sus posiciones
        for fila in range(len(matriz)):
            for columna in range(len(matriz[fila])):
                if matriz[fila][columna] == numero:
                    posiciones.append((fila, columna))
        
        if not posiciones:
            return None  # El número no está en la matriz

    # Ordenar las posiciones por cercanía al objetivo
        posiciones_ordenadas = sorted(posiciones, key=lambda pos: abs(pos[1] - objetivo))

        return posiciones_ordenadas


    def encontrar_posicion(matriz, numero):
        # Encuentra la posición actual del número en la matriz
        for fila in range(len(matriz)):
            for columna in range(len(matriz[fila])):
                if matriz[fila][columna] == numero:
                    return fila, columna
        return None

    muro = 1
    fuego = 2
    cubeta_uno = 3
    cubeta_dos = 4
    hidrante = 6

    def encontrar_posicion_mas_cercana(matriz, numero, objetivo):
        posiciones = []
        
        # Buscar todas las ocurrencias del número en la matriz y guardar sus posiciones
        for fila in range(len(matriz)):
            for columna in range(len(matriz[fila])):
                if matriz[fila][columna] == numero:
                    posiciones.append((fila, columna))
        
        if not posiciones:
            return None  # El número no está en la matriz

        # Calcular la distancia entre el objetivo y cada posición
        distancias = [abs((fila, columna)[1] - objetivo) for (fila, columna) in posiciones]

        # Encontrar la posición más cercana
        posicion_cercana = posiciones[distancias.index(min(distancias))]

        return posicion_cercana




    
    posicion_actual = encontrar_posicion(matriz_inicial, 5)
    agente = matriz_inicial[posicion_actual[0]][posicion_actual[1]]
    pos_hidrante = encontrar_posicion(matriz_inicial,hidrante)
    pos_fuegos = encontrar_posiciones_ordenadas(matriz_inicial,fuego,agente)
    print(pos_fuegos)

    def distancia_manhattan(posicion1, posicion2):
        """
        Calcula la distancia Manhattan entre dos posiciones en una matriz.
        
        Args:
        posicion1: Tupla (fila1, columna1) que representa la primera posición.
        posicion2: Tupla (fila2, columna2) que representa la segunda posición.
        
        Returns:
        La distancia Manhattan entre las dos posiciones.
        """
        fila1, columna1 = posicion1
        fila2, columna2 = posicion2
        distancia = abs(fila1 - fila2) + abs(columna1 - columna2)
        return distancia
    
    



    def calcular_distancia_manhattan(punto1, punto2):
        return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])

    def manhattan(matriz, primer_numero, segundo_numero):
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

    nodos.append({"padre":{
                    "pos":None,
                    "estado":None,
                    "nodo":0,
                    },
                "costo": 0,
                "heuristica": manhattan(matriz_inicial,2,5),
                "estado":{
                    "cubeta": None,
                    "llena":False},
                    "desplazamiento":None,
                    "posicion":posicion_actual,
                    "profundidad":0
                })
    print(manhattan(matriz_inicial,8,5))



#INICIO MOVER_NUMERO

    def mover_numero(_cola, padre,n, direccion):

        matriz = _cola["matriz"]
        padre= copy.deepcopy(padre)
        posicion_actual = encontrar_posicion(matriz, 5)
        posicion_padre = padre["padre"]["pos"]
        costo_actual =    0  #padre["costo"]
        estado_padre = padre["estado"]
        estado_actual = copy.deepcopy(estado_padre)
        estado_abuelo = padre["padre"]["estado"]
        profundidad = padre["profundidad"]
        heuristica_actual = manhattan(matriz,fuego,agente)
        # print(heuristica_actual)
        #print(profundidad)

        # Variables que manejan el costo de cada paso de acuerdo a lo llena
        # que vaya la cubeta

        costo = 1
        if( estado_actual["cubeta"] == "1L" and
            estado_actual["llena"] == True): costo = 2

        elif(estado_actual["cubeta"] == "2L" and
            estado_actual["llena"] == True): costo = 3
        elif(estado_actual["cubeta"] == "2L" and
           estado_actual["llena"] == "Mitad"): costo = 2
        else: 
          costo = 1

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

            if( 0 <= nueva_fila < len(matriz) and
                0 <= nueva_columna < len(matriz[nueva_fila]) and
                matriz[nueva_fila][nueva_columna] != muro ):

                if (encontrar_posicion(matriz, 2) == None):
                    print(matriz)
                    print(padre)
                    return False

                if(
                    estado_actual["llena"] == True and
                    estado_abuelo["llena"] == False
                ):

                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":
                                    {
                                        "pos":posicion_actual
                                        ,"estado":estado_padre
                                        ,"nodo":n
                                    }
                                ,"costo":costo_actual + costo
                                ,"estado":estado_actual
                                ,"heuristica":heuristica_actual
                                ,"desplazamiento":direccion,
                                "posicion":(nueva_fila,nueva_columna)
                                ,"profundidad":profundidad + 1})
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)

                if(
                    (nueva_fila,nueva_columna) == pos_hidrante and
                    estado_actual["llena"] == False and
                    estado_actual["cubeta"] != None
                    #and (nueva_fila,nueva_columna) != posicion_padre
                ):

                    estado_actual["llena"] = True
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{
                                           "pos":posicion_actual,
                                           "estado":estado_padre,
                                           "nodo":n
                                           }
                                    ,"costo":costo_actual + costo
                                    ,"heuristica":heuristica_actual
                                    , "estado":estado_actual
                                    ,"desplazamiento":direccion
                                    ,"posicion":(nueva_fila,nueva_columna)
                                    ,"profundidad":profundidad + 1
                                    })
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return True#(nueva_fila,nueva_columna)

                if(
                    matriz[nueva_fila][nueva_columna] == fuego and
                    estado_actual["cubeta"] == "2L" and
                    estado_actual["llena"] == True
                ):
                    estado_actual["llena"] = "Mitad"
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":(nueva_fila,nueva_columna),"estado":estado_padre,"nodo":n}
                                    ,"costo":costo_actual + costo
                                    ,"heuristica":heuristica_actual
                                    ,"estado":estado_actual
                                    ,"desplazamiento":direccion
                                    ,"posicion":(nueva_fila,nueva_columna)
                                    ,"profundidad":profundidad + 1
                                    })
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)
                elif(
                    matriz[nueva_fila][nueva_columna] == fuego and
                    estado_actual["cubeta"] == "2L" and
                    estado_actual["llena"] == "Mitad"
                ):
                    estado_actual["llena"] = False
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":(nueva_fila,nueva_columna),"estado":estado_padre,"nodo":n}
                                    ,"costo":costo_actual + costo
                                    ,"heuristica":heuristica_actual
                                    ,"estado":estado_actual,
                                    "desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)
                                    ,"profundidad":profundidad + 1
                                    })
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)
                if(
                    matriz[nueva_fila][nueva_columna] == fuego and
                    estado_actual["cubeta"] == "1L" and
                    estado_actual["llena"] == True
                ):

                    estado_actual["llena"] = False
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":(nueva_fila,nueva_columna),"estado":estado_padre,"nodo":n}
                                    ,"costo":costo_actual + costo
                                    ,"heuristica":heuristica_actual
                                    ,"estado":estado_actual,
                                    "desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)
                                    ,"profundidad":profundidad + 1})
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)



                if(
                    matriz[nueva_fila][nueva_columna] == cubeta_uno and
                    estado_actual["cubeta"] == None #and (nueva_fila,nueva_columna) != fuego
                ):
                    estado_actual = {"cubeta": "1L","llena":False}
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n}
                                  ,"costo":costo_actual + costo 
                                  ,"heuristica":heuristica_actual
                                  ,"estado":estado_actual
                                  ,"desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)
                                    ,"profundidad":profundidad + 1})
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)
            # Verificar si la nueva posición está dentro de la matriz
                if(
                    matriz[nueva_fila][nueva_columna] == cubeta_dos and
                    estado_actual["cubeta"] == None
                ):

                    estado_actual = {"cubeta": "2L","llena":False}
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n}
                                  ,"costo":costo_actual + costo
                                  ,"heuristica":heuristica_actual
                                  , "estado":estado_actual
                                  , "desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)
                                    ,"profundidad":profundidad + 1})
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)


                if (
                    (nueva_fila,nueva_columna) != posicion_padre and
                    matriz[nueva_fila][nueva_columna] != fuego
                ):
                    # Mover el número a la nueva posición

                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n}
                                  ,"costo":costo_actual + costo
                                  ,"heuristica":heuristica_actual
                                  , "estado":estado_actual,
                                "desplazamiento":direccion,
                                "posicion":(nueva_fila,nueva_columna)
                                ,"profundidad":profundidad + 1})
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)

                if(

                    estado_actual["cubeta"] == "1L" and
                    estado_abuelo["cubeta"] == None and
                    matriz[nueva_fila][nueva_columna] != fuego
                ):
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n}
                                  ,"costo":costo_actual + costo
                                  ,"heuristica":heuristica_actual
                                  , "estado":estado_actual,
                                "desplazamiento":direccion,
                                "posicion":(nueva_fila,nueva_columna)
                                ,"profundidad":profundidad + 1})
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)
                elif(
                    estado_actual["cubeta"] == "2L" and
                    estado_abuelo["cubeta"] == None
                ):

                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n}
                                ,"costo":costo_actual + costo
                                ,"heuristica":heuristica_actual
                                , "estado":estado_actual,
                                "desplazamiento":direccion,
                                "posicion":(nueva_fila,nueva_columna)
                                ,"profundidad":profundidad + 1})
                    cola.append({"matriz":matriz,"costo":costo_actual + costo,"heuristica":heuristica_actual,"nodo_actual":len(nodos)-1})
                    return (nueva_fila,nueva_columna)
            return (nueva_fila,nueva_columna)


    matriz_abajo = mover_numero(copy.deepcopy(cola_inicial), nodos[0], 0,"abajo")
    matriz_arriba = mover_numero(copy.deepcopy(cola_inicial), nodos[0], 0, "derecha")
    matriz_izquierda = mover_numero(copy.deepcopy(cola_inicial), nodos[0],0, "arriba")
    matriz_derecha = mover_numero(copy.deepcopy(cola_inicial),nodos[0], 0, "izquierda")


    def llenar_cola(n, cola):

        m = cola[0]
        minimo = cola[0]["costo"] + cola[0]["heuristica"]
        index_cola = 0
        index = 0
        while True:


            matriz_abajo = mover_numero(copy.deepcopy(m), nodos[n], n, "abajo")

            if not matriz_abajo:
                return encontrar_camino(n)

            matriz_arriba = mover_numero(copy.deepcopy(m), nodos[n], n, "derecha")
            if not matriz_arriba:
                return encontrar_camino(n)

            matriz_izquierda = mover_numero(copy.deepcopy(m), nodos[n], n, "arriba")
            if not matriz_izquierda:
                return encontrar_camino(n)

            matriz_derecha = mover_numero(copy.deepcopy(m), nodos[n], n, "izquierda")
            if not matriz_derecha:
                return encontrar_camino(n)

            cola.pop(index_cola)
            n = cola[0]["nodo_actual"]
            m = cola[0]
            minimo = cola[0]["costo"] + cola[0]["heuristica"]
            index_cola = 0

            for i in range(len(cola)):                
                if (cola[i]["costo"] + cola[i]["heuristica"] )< minimo:
                    minimo = cola[i]["costo"]
                    n = cola[i]["nodo_actual"]
                    m = cola[i]
                    minimo = (cola[i]["costo"] + cola[i]["heuristica"] )
                    index_cola = i
    
    camino = llenar_cola(1,cola)  
    ultimo_nodo = nodos[len(nodos)-1]
    tiempo_fin = time.time()
    tiempo_ejecucion = (tiempo_fin - tiempo_inicio)    
    minutos = int(tiempo_ejecucion // 60)
    segundos = int(tiempo_ejecucion % 60)
    reporte = {
       "nodos_expandidos": len(nodos),
       "profundidad_arbol": ultimo_nodo["profundidad"],
       "tiempo_computo": str( minutos) +":"+str(segundos)  + " minutos"
    }
    # print(reporte)   
    # print(nodos[len(nodos)-1])   
    return {"camino":camino,"reporte":reporte}

agente_a_estrella()

