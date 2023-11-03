import copy
import time
from Reader import get_matriz
tiempo_inicio = time.time()
def agente_avara():
    
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

    posicion_actual = encontrar_posicion(matriz_inicial, 5)
    agente = matriz_inicial[posicion_actual[0]][posicion_actual[1]]
    pos_hidrante = encontrar_posicion(matriz_inicial,hidrante) 



    def calcular_distancia_manhattan(punto1, punto2):
        return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])

    def aplicar_heuristica(matriz, primer_numero, segundo_numero):
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
        
        
        distancia_extra=0
        for i in range(len(posiciones_primer_numero) - 1):
            for j in range(i + 1, len(posiciones_primer_numero)):
                distancia_extra = calcular_distancia_manhattan(posiciones_primer_numero[i], posiciones_primer_numero[j])
                

        # print("tot: ", distancia_minima + distancia_extra)
        # print("minima: ", distancia_minima)   
        return distancia_minima + distancia_extra

    nodos.append({"padre":{
                    "pos":None,
                    "estado":None,
                    "nodo":0,
                    },
                "costo": 0,
                "heuristica": aplicar_heuristica(matriz_inicial,2,5),
                "estado":{
                    "cubeta": None,
                    "llena":False},
                    "desplazamiento":None,
                    "posicion":posicion_actual,
                    "profundidad":0
                })

#INICIO MOVER_NUMERO

    def mover_numero(_cola, padre,n, direccion):

        matriz = _cola["matriz"]
        padre= copy.deepcopy(padre)
        posicion_actual = encontrar_posicion(matriz, 5)
        posicion_padre = padre["padre"]["pos"]
        costo_actual =  padre["costo"]
        estado_padre = padre["estado"]
        estado_actual = copy.deepcopy(estado_padre)
        estado_abuelo = padre["padre"]["estado"]
        profundidad = padre["profundidad"]
        heuristica_actual = aplicar_heuristica(matriz,fuego,agente)        
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
        minimo =  cola[0]["heuristica"] #+ cola[0]["costo"]        
        index_cola = 0
        
        while True:

            matriz_abajo = mover_numero(copy.deepcopy(m), nodos[n], n, "abajo")
            if not matriz_abajo:
                return {"camino":encontrar_camino(n), "index":n}

            matriz_arriba = mover_numero(copy.deepcopy(m), nodos[n], n, "derecha")
            if not matriz_arriba:
                return {"camino":encontrar_camino(n), "index":n}

            matriz_izquierda = mover_numero(copy.deepcopy(m), nodos[n], n, "arriba")
            if not matriz_izquierda:
                return {"camino":encontrar_camino(n), "index":n}

            matriz_derecha = mover_numero(copy.deepcopy(m), nodos[n], n, "izquierda")
            if not matriz_derecha:
                return {"camino":encontrar_camino(n), "index":n}

            cola.pop(index_cola)
            n = cola[0]["nodo_actual"]
            m = cola[0]
            minimo =  cola[0]["heuristica"] #+ cola[0]["costo"]
            index_cola = 0

            #print("minimo: ", minimo)

            for i in range(len(cola)):                              
                if ( cola[i]["heuristica"] )< minimo:
                    #minimo = cola[i]["costo"]
                    n = cola[i]["nodo_actual"]
                    m = cola[i]
                    minimo = ( cola[i]["heuristica"] )
                    index_cola = i
                    # print(minimo)
                   
    
    respuesta = llenar_cola(1,cola)  
    ultimo_nodo = nodos[respuesta["index"]]    
    tiempo_fin = time.time()
    tiempo_ejecucion = (tiempo_fin - tiempo_inicio)    
    minutos = int(tiempo_ejecucion // 60)
    segundos = int(tiempo_ejecucion % 60)
    reporte = {
       "nodos_expandidos": len(nodos),
       "profundidad_arbol": ultimo_nodo["profundidad"],
       "tiempo_computo": str( minutos) +":"+str(segundos)  + " minutos"
    }    
    return {"camino":respuesta["camino"],"reporte":reporte}
agente_avara()
