import copy
import time
from Reader import get_matriz
tiempo_inicio = time.time()
def agente_amplitud():
    matriz_inicial = get_matriz()

    pila_inicial = {
        "matriz":matriz_inicial,
        "costo": 0
    }
    pila = []
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
    pos_hidrante = encontrar_posicion(matriz_inicial,6)



    nodos.append({"padre":{
                        "pos":None,
                        "estado":None,
                        "nodo":0 
                        },
                    "costo": 0,
                    "estado":{
                        "cubeta": None,
                        "llena":False},
                        "desplazamiento":None,
                        "posicion":posicion_actual
                    })

    def mover_numero(_pila, padre,n, direccion):   

        matriz = _pila["matriz"]

        padre= copy.deepcopy(padre)
        posicion_actual = encontrar_posicion(matriz, 5)
        posicion_padre = padre["padre"]["pos"]
        costo_actual = padre["costo"]
        estado_padre = padre["estado"]
        estado_actual = copy.deepcopy(estado_padre)
        estado_abuelo = padre["padre"]["estado"]      

        # Variables que manejan el costo de cada paso de acuerdo a lo llena 
        # que vaya la cubeta

        costo = 1
        if( estado_actual["cubeta"] == "1L" and
            estado_actual["llena"] == True): costo = 2
        
        if(estado_actual["cubeta"] == "2L" and
            estado_actual["llena"] == True): costo = 3        
            

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
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n},"costo":costo_actual + costo, "estado":estado_actual,
                                "desplazamiento":direccion,
                                "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})
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
                                    , "estado":estado_actual
                                    ,"desplazamiento":direccion
                                    ,"posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})                                       
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
                                    ,"costo":costo_actual + costo,
                                    "estado":estado_actual,
                                    "desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})  
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
                                    ,"costo":costo_actual + costo,
                                    "estado":estado_actual,
                                    "desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})  
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
                                    ,"costo":costo_actual + costo,
                                    "estado":estado_actual,
                                    "desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})  
                    return (nueva_fila,nueva_columna)



                if(                    
                    matriz[nueva_fila][nueva_columna] == cubeta_uno and
                    estado_actual["cubeta"] == None #and (nueva_fila,nueva_columna) != fuego
                ):
                    estado_actual = {"cubeta": "1L","llena":False}
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n},"costo":costo_actual + costo , "estado":estado_actual,
                                    "desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})
                    return (nueva_fila,nueva_columna)
            # Verificar si la nueva posición está dentro de la matriz
                if( 
                    matriz[nueva_fila][nueva_columna] == cubeta_dos and
                    estado_actual["cubeta"] == None
                ):
                
                    estado_actual = {"cubeta": "2L","llena":False}
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n},"costo":costo_actual + costo, "estado":estado_actual,
                                    "desplazamiento":direccion,
                                    "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})
                    return (nueva_fila,nueva_columna)


                if (                    
                    (nueva_fila,nueva_columna) != posicion_padre and
                    matriz[nueva_fila][nueva_columna] != fuego
                ):
                    # Mover el número a la nueva posición

                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n},"costo":costo_actual + costo, "estado":estado_actual,
                                "desplazamiento":direccion,
                                "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})
                    return (nueva_fila,nueva_columna)
            
                if(
                   
                    estado_actual["cubeta"] == "1L" and
                    estado_abuelo["cubeta"] == None and
                    matriz[nueva_fila][nueva_columna] != fuego
                ):
                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n},"costo":costo_actual + costo, "estado":estado_actual,
                                "desplazamiento":direccion,
                                "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})
                    return (nueva_fila,nueva_columna)
                elif(
                    estado_actual["cubeta"] == "2L" and
                    estado_abuelo["cubeta"] == None
                ):

                    matriz[fila][columna] = 0
                    matriz[nueva_fila][nueva_columna] = agente
                    nodos.append({"padre":{"pos":posicion_actual,"estado":estado_padre,"nodo":n},"costo":costo_actual + costo, "estado":estado_actual,
                                "desplazamiento":direccion,
                                "posicion":(nueva_fila,nueva_columna)})
                    pila.append({"matriz":matriz,"costo":costo_actual + costo})
                    return (nueva_fila,nueva_columna)  
            return (nueva_fila,nueva_columna)

   
    matriz_abajo = mover_numero(copy.deepcopy(pila_inicial), nodos[0], 0,"abajo")
    matriz_arriba = mover_numero(copy.deepcopy(pila_inicial), nodos[0], 0, "derecha")
    matriz_izquierda = mover_numero(copy.deepcopy(pila_inicial), nodos[0],0, "arriba")
    matriz_derecha = mover_numero(copy.deepcopy(pila_inicial),nodos[0], 0, "izquierda")


    def llenar_pila(n, pila):
        while pila:
            m = pila[0]
            index = 0

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

            pila.pop(index)
            n += 1


    camino = llenar_pila(1,pila)  
    ultimo_nodo = nodos[len(nodos)-1]
    tiempo_fin = time.time()
    tiempo_ejecucion = (tiempo_fin - tiempo_inicio) 
    print(tiempo_ejecucion)
    minutos = int(tiempo_ejecucion // 60)
    segundos = int(tiempo_ejecucion % 60)
    reporte = {
       "nodos_expandidos": len(nodos),
       #"profundidad_arbol": ultimo_nodo["profundidad"],
       "tiempo_computo": str( minutos) +":"+str(segundos)  + " minutos"
    }
    print(reporte)      
    return {"camino":camino,"reporte":reporte}           


agente_amplitud()