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
    recorrido = []   
    recorrido_min = []
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
    nodos = []
    #nodos.append(cola[0])

    
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
        puntos_obtenidos = _cola["puntos_obtenidos"]
        alpha = _cola["alpha"]
        alpha_monedas = _cola["alpha_monedas"]
        

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
            beneficio = sumatoria_beneficio((nueva_fila,nueva_columna),matriz) / 10

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

    def distancia_manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def encontrar_posicion_mas_cercana(matriz, fila, columna):
        uno_o_dos_encontrado = False
        distancia_mas_cercana = float('inf')
        posicion_mas_cercana = None

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == 1 or matriz[i][j] == 2:
                    uno_o_dos_encontrado = True
                    dist = distancia_manhattan((fila, columna), (i, j))
                    if dist < distancia_mas_cercana:
                        distancia_mas_cercana = dist
                        posicion_mas_cercana = (i, j)

        return uno_o_dos_encontrado, posicion_mas_cercana

    def encontrar_mejor_movimiento_en_L(matriz, fila, columna, fila_previa, columna_previa, visitados):
        movimientos = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
        uno_o_dos_cercano, posicion_mas_cercana = encontrar_posicion_mas_cercana(matriz, fila, columna)

        if not uno_o_dos_cercano:
            return None

        mejor_movimiento = None
        mejor_distancia = float('inf')

        for mov in movimientos:
            nueva_fila = fila + mov[0]
            nueva_columna = columna + mov[1]

            if 0 <= nueva_fila < len(matriz) and 0 <= nueva_columna < len(matriz[0]) and (nueva_fila, nueva_columna) != (fila_previa, columna_previa) and (nueva_fila, nueva_columna) not in visitados:
                dist = distancia_manhattan((nueva_fila, nueva_columna), posicion_mas_cercana)
                if dist < mejor_distancia:
                    mejor_distancia = dist
                    mejor_movimiento = (nueva_fila, nueva_columna)

        return mejor_movimiento

    def encontrar_camino_hacia_1_o_2(matriz, fila_inicial, columna_inicial, posiciones_evitar):
        visitados = set(posiciones_evitar)
        camino = [(fila_inicial, columna_inicial)]

        fila_previa = None
        columna_previa = None

        while True:
            movimiento = encontrar_mejor_movimiento_en_L(matriz, camino[-1][0], camino[-1][1], fila_previa, columna_previa, visitados)
            if movimiento is None:
                break
            visitados.add(movimiento)
            camino.append(movimiento)
            fila_previa, columna_previa = camino[-2]

            if matriz[movimiento[0]][movimiento[1]] == 1 or matriz[movimiento[0]][movimiento[1]] == 2:
                break

        return camino        

    def mover_caballo():        
        n = 0
        profundidad = 0
        caballo_turno = caballo_maquina
        rama_min_max = "max"
        while True:        
            m = cola[0]        
            if (profundidad < m["profundidad"]):
                profundidad = m["profundidad"]
                if m["jugador"] == caballo_maquina:
                    caballo_turno = caballo_jugador
                    rama_min_max = "min"                    
                elif m["jugador"] == caballo_jugador:
                    caballo_turno = caballo_maquina    
                    rama_min_max = "max"                   
                
            if  rama_min_max == 'min':
                m["alpha"] = -10000000    
                m["alpha_monedas"] = -10000000 
            elif rama_min_max == 'max':
                m["alpha"] = 10000000    
                m["alpha_monedas"] = 10000000             
            
            m["jugador"] = caballo_turno
            m["rama_min_max"] = rama_min_max
            if m["profundidad"]  == profundidad_arbol:
                break

            
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
        
        #while j >= 0:
        #for i in range(len(nodos)): 
        i = 0
        while i < 37:            
            if  nodos[i]["nodo_padre"] != None:  
                if nodos[i]["profundidad"] == 2:
                    if nodos[i]["rama_min_max"] == "min": 
                        if nodos[i]["puntos_obtenidos"] >  nodos[i]["beneficio_acumulado"]:  
                            if nodos[i]["puntos_obtenidos"] >  nodos[nodos[i]["nodo_padre"]]["alpha"]:                                                                                              
                                nodos[nodos[i]["nodo_padre"]]["alpha"] = nodos[i]["puntos_obtenidos"] 
                                nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"] 
                                nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = nodos[i]["pocision_anterior"] 
                                nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = nodos[i]["pocision_actual"] 
                                recorrido_min.clear()

                        elif(nodos[i]["puntos_obtenidos"] <  nodos[i]["beneficio_acumulado"]):
                            if (nodos[i]["beneficio_acumulado"] > nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                                nodos[nodos[i]["nodo_padre"]]["alpha"] = nodos[i]["beneficio_acumulado"]
                                nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"]   
                                nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = nodos[i]["pocision_anterior"] 
                                nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = nodos[i]["pocision_actual"] 
                                recorrido_min.clear()
                                
                        elif(nodos[i]["puntos_obtenidos"] == 0 and  nodos[i]["beneficio_acumulado"] == 0):                        
                            nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = encontrar_posicion(_matriz,caballo_maquina) 
                            fil,col = nodos[nodos[i]["nodo_padre"]]["pocision_anterior"]
                            pos_act = encontrar_camino_hacia_1_o_2(_matriz,fil,col,recorrido)     
                            nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = pos_act[1]
                            recorrido_min.append(pos_act[1])
                    
                    # elif nodos[i]["rama_min_max"] == "max":       
                    # print("puntos onbtenidos",nodos[i]["puntos_obtenidos"] )    
                    # print("beneficio acumulado",nodos[i]["beneficio_acumulado"])    
                    # print("aplha padre",nodos[nodos[i]["nodo_padre"]]["alpha"])                 
                    # if nodos[i]["puntos_obtenidos"] >  nodos[i]["beneficio_acumulado"]:  
                    #     if nodos[i]["puntos_obtenidos"] >  nodos[nodos[i]["nodo_padre"]]["alpha"]:                                                                                              
                    #         nodos[nodos[i]["nodo_padre"]]["alpha"] = nodos[i]["puntos_obtenidos"] 
                    #         nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"] 
                    #         nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = nodos[i]["pocision_anterior"] 
                    #         nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = nodos[i]["pocision_actual"] 
                    #         recorrido.clear()
                    # elif(nodos[i]["puntos_obtenidos"] <  nodos[i]["beneficio_acumulado"]):
                    #     if (nodos[i]["beneficio_acumulado"] > nodos[nodos[i]["nodo_padre"]]["alpha"]):                                                                                              
                    #         nodos[nodos[i]["nodo_padre"]]["alpha"] = nodos[i]["beneficio_acumulado"]
                    #         nodos[nodos[i]["nodo_padre"]]["alpha_monedas"] = nodos[i]["puntos_acumulados"]   
                    #         nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = nodos[i]["pocision_anterior"] 
                    #         nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = nodos[i]["pocision_actual"] 
                    #         recorrido.clear()
                            
                    # elif(nodos[i]["puntos_obtenidos"] == 0 and  nodos[i]["beneficio_acumulado"] == 0):                        
                        # nodos[nodos[i]["nodo_padre"]]["pocision_anterior"] = encontrar_posicion(_matriz,caballo_maquina) 
                        # fil,col = nodos[nodos[i]["nodo_padre"]]["pocision_anterior"]
                        # pos_act = encontrar_camino_hacia_1_o_2(_matriz,fil,col,recorrido)     
                        # nodos[nodos[i]["nodo_padre"]]["pocision_actual"] = pos_act[1]
                        # recorrido.append(pos_act[1])
                    #nodos.pop(i)            
            i += 1                                
                  
        print("alpha actual---->",nodos[1]["alpha_monedas"])  
        print("alpha actual---->",nodos[1]["nodo_padre"])  

        print("nodo 2")

        print("alpha actual---->",nodos[2]["alpha_monedas"])  
        print("alpha actual---->",nodos[2]["nodo_padre"]) 

        print("nodo 3")


        print("alpha actual---->",nodos[3]["alpha_monedas"])  
        print("alpha actual---->",nodos[3]["nodo_padre"]) 


        print("nodo 4")

        print("alpha actual---->",nodos[4]["alpha_monedas"])  
        print("alpha actual---->",nodos[4]["nodo_padre"]) 

        print("nodo 5")

        print("alpha actual---->",nodos[36]["alpha_monedas"])  
        print("alpha actual---->",nodos[36]["nodo_padre"]) 
        print("rama---->",nodos[36]["rama_min_max"]) 

        print(len(nodos))  
        #print("alpha---->",nodos[1]["pocision_anterior"])  
        #print("alpha actual---->",nodos[1]["pocision_actual"])  
        fila_anterior, columna_anterior = nodos[0]["pocision_anterior"]
        fila_actual, columna_actual = nodos[0]["pocision_actual"]
    
        _matriz[fila_anterior][columna_anterior] = espacio_vacio
        _matriz[fila_actual][columna_actual] = caballo_maquina      

        cola.clear()
        nodos.clear()
        
        fila_anterior_jugador,columna_anterior_jugador = encontrar_posicion(_matriz, caballo_jugador)
        #print(fila_anterior_jugador,columna_anterior_jgador)
         
        fila_jugador = int(input("Ingrese la posición de la fila: "))
        columna_jugador = int(input("Ingrese la posición de la columna: "))
        movimiento_caballo_jugador(( fila_anterior_jugador,columna_anterior_jugador),(fila_jugador,columna_jugador))

        _matriz[fila_anterior_jugador][columna_anterior_jugador] = espacio_vacio
        _matriz[fila_jugador][columna_jugador] = caballo_jugador  

    def imprimir_matriz(matriz):
        for fila in matriz:
            print(" ".join(map(str, fila)))
    #mover_caballo() 
    #imprimir_matriz(_matriz)  
    while True:
        mover_caballo()    
        print("reset")
        print(cola)
        print(nodos)
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
        
        #nodos = []
        nodos.append(cola[0])
        imprimir_matriz(_matriz)   
        print(estado_jugador)
   

agente_amplitud(Reader('Prueba1.txt'))