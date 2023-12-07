import copy
import time
from Reader import Reader

def agente_amplitud(_matriz):
    tiempo_inicio = time.time()
    
    #Definicion de objetos del mapa
    casilla_tomada = 5
    espacio_vacio = 0
    moneda_uno = 1
    moneda_dos = 2   
    caballo_maquina = 3   
    caballo_jugador = 4
    puntos_moneda_uno = 1
    puntos_moneda_dos = 3
    profundidad_arbol = 2


    matriz_inicial = _matriz

    cola = [{
        "matriz":matriz_inicial,
        "jugador": caballo_maquina,
        "rama_min_max": "max",
        "pocision_anterior": (0,0),
        "pocision_actual": (0,0),
        "puntos_obtenidos": 0,
        "beneficio_acumulado": 0,
        "profundidad": 0,
        "nodo_padre": None, 
        "alpha": -10000000,
        "alpha_monedas": -10000000
    }]
    #cola = []
    nodos = []
    nodos.append(cola[0])

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

    def sumatoria_beneficio(pocision, matriz):
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
    

    def movimiento_caballo(_cola, n, direccion):        

        

        matriz = _cola["matriz"]
        caballo_turno = _cola["jugador"]        
        posicion_actual = encontrar_posicion(matriz, caballo_turno)    
        rama_min_max = _cola["rama_min_max"]
        beneficio = _cola["beneficio_acumulado"]
        profundidad = _cola["profundidad"]
        nodo_padre = _cola["nodo_padre"]
        puntos_obtenidos = _cola["puntos_obtenidos"]
        alpha = _cola["alpha"]
        alpha_monedas = _cola["alpha_monedas"]

        #print(direccion)

        if not posicion_actual:
            return matriz  # Si no se encuentra el número, no se realiza ningún movimiento
        fila, columna = posicion_actual
        # Definir los desplazamientos para las cuatro direcciones
        desplazamientos = {
            #desplazamiento en L atras
            "atras_arriba_dos": (-2, -1),
            "atras_arriba_una": (-1, -2),            
            "atras_abajo_una": (1, -2),
            "atras_abajo_dos": (2, -1),

            #desplazamiento en L adelante
            "adelante_abajo_dos": (2, 1),
            "adelante_abajo_una": (1, 2),            
            "adelante_arriba_una": (-1, 2),
            "adelante_arriba_dos": (-2, 1),
            
        }
        # Calcular la nueva posición
        desplazamiento = desplazamientos.get(direccion)    

        enemigo = caballo_maquina
        #Verificar cuál es el contrincante
        if(caballo_turno == caballo_maquina):
            enemigo = caballo_jugador        

        if desplazamiento:
            nueva_fila = fila + desplazamiento[0]
            nueva_columna = columna + desplazamiento[1]
            beneficio = sumatoria_beneficio((nueva_fila,nueva_columna),matriz)

            if( 0 <= nueva_fila < len(matriz) and
                0 <= nueva_columna < len(matriz[nueva_fila]) and
                matriz[nueva_fila][nueva_columna] != enemigo 
              #  and matriz[nueva_fila][nueva_columna] != casilla_tomada
                ):

                #condicional en caso de que que caiga en una casilla vacía    
                if(matriz[nueva_fila][nueva_columna] == espacio_vacio):
                
                    matriz[fila][columna] = espacio_vacio
                    matriz[nueva_fila][nueva_columna] = caballo_turno               
                       
                    
                    cola.append({
                        "matriz":matriz,
                        "jugador": caballo_turno,
                        "rama_min_max": rama_min_max,
                        "pocision_anterior": (fila,columna),
                        "pocision_actual": (nueva_fila,nueva_columna),
                        "puntos_obtenidos": puntos_obtenidos,
                        "beneficio_acumulado": beneficio,
                        "profundidad": profundidad + 1, 
                        "nodo_padre": n
                    })
                    nodos.append({
                            "matriz":matriz,
                            "jugador": caballo_turno,
                            "rama_min_max": rama_min_max,
                            "pocision_anterior": (fila,columna),
                            "pocision_actual": (nueva_fila,nueva_columna),
                            "puntos_obtenidos":0,
                            "puntos_acumulados": puntos_obtenidos,
                            "beneficio_acumulado": beneficio,
                            "profundidad": profundidad + 1, 
                            "nodo_padre": n,
                            "alpha":alpha,
                            "alpha_monedas":alpha_monedas
                    })                   
                   
                    return        
                
                if(matriz[nueva_fila][nueva_columna] == moneda_uno):
                
                    matriz[fila][columna] = espacio_vacio
                    matriz[nueva_fila][nueva_columna] = caballo_turno               
                    cola.append({
                            "matriz":matriz,
                            "jugador": caballo_turno,
                            "rama_min_max": rama_min_max,
                            "pocision_anterior": (fila,columna),
                            "pocision_actual": (nueva_fila,nueva_columna),
                            "puntos_obtenidos": puntos_obtenidos + puntos_moneda_uno,
                            "beneficio_acumulado": beneficio,
                            "profundidad": profundidad + 1, 
                            "nodo_padre": n
                        })
                    nodos.append({
                            "matriz":matriz,
                            "jugador": caballo_turno,
                            "rama_min_max": rama_min_max,
                            "pocision_anterior": (fila,columna),
                            "pocision_actual": (nueva_fila,nueva_columna),
                            "puntos_obtenidos": puntos_moneda_uno,
                            "puntos_acumulados": puntos_obtenidos + puntos_moneda_uno,
                            "beneficio_acumulado": beneficio,
                            "profundidad": profundidad + 1, 
                            "nodo_padre": n,
                            "alpha":alpha,
                            "alpha_monedas":alpha_monedas
                    })
                    return
                
                #Condicional para movimiento en casilla con moneda 

                if(matriz[nueva_fila][nueva_columna] == moneda_dos):
                
                    matriz[fila][columna] = espacio_vacio
                    matriz[nueva_fila][nueva_columna] = caballo_turno               
                    cola.append({
                        "matriz":matriz,
                        "jugador": caballo_turno,
                        "rama_min_max": rama_min_max,
                        "pocision_anterior": (fila,columna),
                        "pocision_actual": (nueva_fila,nueva_columna),
                        "puntos_obtenidos": puntos_obtenidos + puntos_moneda_dos,
                        "beneficio_acumulado": beneficio,
                        "profundidad": profundidad + 1, 
                        "nodo_padre": n
                    })
                    nodos.append({
                            "matriz":matriz,
                            "jugador": caballo_turno,
                            "rama_min_max": rama_min_max,
                            "pocision_anterior": (fila,columna),
                            "pocision_actual": (nueva_fila,nueva_columna),
                            "puntos_obtenidos":puntos_moneda_dos,
                            "puntos_acumulados": puntos_obtenidos + puntos_moneda_dos,
                            "beneficio_acumulado": beneficio,
                            "profundidad": profundidad + 1, 
                            "nodo_padre": n,
                            "alpha":alpha,
                            "alpha_monedas":alpha_monedas 
                    })
                return                
            return
        return 
    
    estado_jugador = [
        {
                        
                        "pocision_anterior": (0,0),
                        "pocision_actual": (0,0),                        
                        "puntos_acumulados": 0                        
        }
    ]
    print(estado_jugador[0])

    def movimiento_caballo_jugador(anterior,nuevo):      

        fila,columna = anterior
        nueva_fila,nueva_columna = nuevo
        caballo_turno = caballo_jugador
        matriz = _matriz        
        enemigo = caballo_maquina  

        if( 0 <= nueva_fila < len(matriz) and
            0 <= nueva_columna < len(matriz[nueva_fila]) and
            matriz[nueva_fila][nueva_columna] != enemigo 
            #  and matriz[nueva_fila][nueva_columna] != casilla_tomada
            ):

            #condicional en caso de que que caiga en una casilla vacía    
            if(matriz[nueva_fila][nueva_columna] == espacio_vacio):
            
                matriz[fila][columna] = espacio_vacio
                matriz[nueva_fila][nueva_columna] = caballo_turno               

                estado_jugador[0]["pocision_anterior"] = (fila,columna)
                estado_jugador[0]["pocision_actual"] = (nueva_fila,nueva_columna)                       
                estado_jugador[0]["puntos_acumulados"] =  estado_jugador[0]["puntos_acumulados"]                              
                
                return        
            
            if(matriz[nueva_fila][nueva_columna] == moneda_uno):
            
                matriz[fila][columna] = espacio_vacio
                matriz[nueva_fila][nueva_columna] = caballo_turno               

                estado_jugador[0]["pocision_anterior"] = (fila,columna)
                estado_jugador[0]["pocision_actual"] = (nueva_fila,nueva_columna)                       
                estado_jugador[0]["puntos_acumulados"] =  estado_jugador[0]["puntos_acumulados"]  + puntos_moneda_uno       
               
                return
            
            #Condicional para movimiento en casilla con moneda 

            if(matriz[nueva_fila][nueva_columna] == moneda_dos):
            
                matriz[fila][columna] = espacio_vacio
                matriz[nueva_fila][nueva_columna] = caballo_turno               

                estado_jugador[0]["pocision_anterior"] = (fila,columna)
                estado_jugador[0]["pocision_actual"] = (nueva_fila,nueva_columna)                       
                estado_jugador[0]["puntos_acumulados"] =  estado_jugador[0]["puntos_acumulados"]  + puntos_moneda_dos   
                return                
            return
        return

            
    
    def mover_caballo():

        aux = 0
        #while True:
        n = 0
        profundidad = 0
        caballo_turno = caballo_maquina
        rama_min_max = "max"
        alpha = 0
        alpha_monedas = 0
        while True:
        #while cola:
            m = cola[0]
        # m["rama_min_max"] = rama_min_max
            if (profundidad < m["profundidad"]):
                profundidad = m["profundidad"]
                if m["jugador"] == caballo_maquina:
                    caballo_turno = caballo_jugador
                    rama_min_max = "min"
                    
                elif m["jugador"] == caballo_jugador:
                    caballo_turno = caballo_maquina    
                    rama_min_max = "max"
                    
                
            if  rama_min_max == 'min':
                alpha = -100000000
                alpha_monedas = -100000000
            elif rama_min_max == 'max':
                alpha = 100000000
                alpha_monedas = 100000000

            
            #aux += 1
            m["jugador"] = caballo_turno
            m["rama_min_max"] = rama_min_max
            m["alpha"] = alpha
            m["alpha_monedas"] = alpha_monedas
            if m["profundidad"]  == profundidad_arbol:
                break

            if(m["nodo_padre"] == None):
                m["alpha"] = -10000000    
                m["alpha_monedas"] = -10000000  
            if(m["nodo_padre"] == 0):
                m["alpha"] = -10000000    
                m["alpha_monedas"] = -10000000      
            # ADELANTE 

            #movimiento en L atras arriba dos casillas
            mov_atras_arriba_dos = movimiento_caballo(copy.deepcopy(m),n, "atras_arriba_dos")

            #movimiento en L atras arriba una casilla
            mov_atras_arriba_uno = movimiento_caballo(copy.deepcopy(m), n, "atras_arriba_una")               

            #movimiento en L atras arriba dos casillas
            mov_atras_abajo_uno = movimiento_caballo(copy.deepcopy(m),n, "atras_abajo_una")

            #movimiento en L atras arriba dos casillas
            mov_atras_abajo_dos = movimiento_caballo(copy.deepcopy(m),n, "atras_abajo_dos")

            
            #ADELANTE

            #movimiento en L atras arriba dos casillas
            mov_adelante_abajo_dos = movimiento_caballo(copy.deepcopy(m),n, "adelante_abajo_dos")  


            #movimiento en L atras arriba dos casillas
            mov_adelante_abajo_una = movimiento_caballo(copy.deepcopy(m),n, "adelante_abajo_una")
            

            #movimiento en L atras arriba una casilla
            mov__adelante_arriba_una = movimiento_caballo(copy.deepcopy(m),n, "adelante_arriba_una")            

            #movimiento en L atras arriba dos casillas
            mov__adelante_arriba_dos = movimiento_caballo(copy.deepcopy(m),n, "adelante_arriba_dos")

            
            cola.pop(0)              
            n += 1           

        puntos_alcanzables = 0
        j = profundidad_arbol 
        
        while j >= 0:
            for i in range(len(nodos)):      
                                
                if  nodos[i]["nodo_padre"] != None:  
                    if nodos[i]["profundidad"] == j:
                        if nodos[i]["rama_min_max"] == "min": 
                            if nodos[i]["puntos_obtenidos"] >  0:                                
                                if  nodos[i]["puntos_acumulados"] <  nodos[nodos[i]["nodo_padre"]]["alpha_monedas"]:                                                                                              
                                    nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"] 

                            elif (nodos[i]["beneficio_acumulado"] < nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                                nodos[nodos[i]["nodo_padre"]]["alpha"] = nodos[i]["beneficio_acumulado"]
                                nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"] 
                        
                        if nodos[i]["rama_min_max"] == "max": 
                           
                            if nodos[i]["puntos_obtenidos"] >  0:                                
                                #if  nodos[i]["puntos_acumulados"] >  nodos[nodos[i]["nodo_padre"]]["alpha_monedas"]:                                                                                              
                                nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"] 
                                nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"] 
                                nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = nodos[i]["pocision_anterior"] 
                                nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = nodos[i]["pocision_actual"] 

                            elif (nodos[i]["beneficio_acumulado"] > nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                                nodos[nodos[i]["nodo_padre"]]["alpha"] = nodos[i]["beneficio_acumulado"]
                                nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"]   
                                nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = nodos[i]["pocision_anterior"] 
                                nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = nodos[i]["pocision_actual"] 
                                            
            j -= 1       
          
        fila_anterior, columna_anterior = nodos[0]["pocision_anterior"]
        fila_actual, columna_actual = nodos[0]["pocision_actual"]
    
        _matriz[fila_anterior][columna_anterior] = espacio_vacio
        _matriz[fila_actual][columna_actual] = caballo_maquina      

        
        
        fila_anterior_jugador,columna_anterior_jugador = encontrar_posicion(_matriz, caballo_jugador)
        #print(fila_anterior_jugador,columna_anterior_jgador)
         
        fila_jugador = int(input("Ingrese la posición de la fila: "))
        columna_jugador = int(input("Ingrese la posición de la columna: "))
        movimiento_caballo_jugador(( fila_anterior_jugador,columna_anterior_jugador),(fila_jugador,columna_jugador))

        # _matriz[fila_anterior_jugador][columna_anterior_jugador] = espacio_vacio
        # _matriz[fila_jugador][columna_jugador] = caballo_jugador  

    def imprimir_matriz(matriz):
        for fila in matriz:
            print(" ".join(map(str, fila)))
    
    while True:
        mover_caballo()    
        cola = [{
            "matriz":matriz_inicial,
            "jugador": caballo_maquina,
            "rama_min_max": "max",
            "pocision_anterior": (0,0),
            "pocision_actual": (0,0),
            "puntos_obtenidos": 0,
            "beneficio_acumulado": 0,
            "profundidad": 0,
            "nodo_padre": None, 
            "alpha": -10000000,
            "alpha_monedas": -10000000
        }]
        #cola = []
        nodos = []
        nodos.append(cola[0])
        imprimir_matriz(_matriz)   
        print(estado_jugador)

    
    
    

    
    #return  _matriz


agente_amplitud(Reader('Prueba1.txt'))