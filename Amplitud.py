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
    


    matriz_inicial = _matriz

    cola = [{
        "matriz":matriz_inicial,
        "jugador": caballo_maquina,
        "rama_min_max": "max",
        "pocision_anterior": (0,0),
        "pocision_actual": (0,0),
        "beneficio_acumulado": 0,
        "profundidad": 0,
        "nodo_padre": None 
    }]
    #cola = []
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

    

    def movimiento_caballo(_cola, n, direccion):        

        

        matriz = _cola["matriz"]
        caballo_turno = _cola["jugador"]        
        posicion_actual = encontrar_posicion(matriz, caballo_turno)    
        rama_min_max = _cola["rama_min_max"]
        beneficio = _cola["beneficio_acumulado"]
        profundidad = _cola["profundidad"]
        nodo_padre = _cola["nodo_padre"]

        print(direccion)

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

            if( 0 <= nueva_fila < len(matriz) and
                0 <= nueva_columna < len(matriz[nueva_fila]) and
                matriz[nueva_fila][nueva_columna] != enemigo 
              #  and matriz[nueva_fila][nueva_columna] != casilla_tomada
                ):

                matriz[fila][columna] = espacio_vacio
                matriz[nueva_fila][nueva_columna] = caballo_turno               
                print("condicional para movimiento en espacio vacio",caballo_turno)
                print((fila,columna)) 

                cola.append({
                        "matriz":matriz,
                        "jugador": caballo_turno,
                        "rama_min_max": rama_min_max,
                        "pocision_anterior": (fila,columna),
                        "pocision_actual": (nueva_fila,nueva_columna),
                        "beneficio_acumulado": beneficio,
                        "profundidad": profundidad + 1, 
                        "nodo_padre": n
                })

                print(profundidad + 1)
                return

                # #condicional en caso de que que caiga en una casilla vacía    
                # if(matriz[nueva_fila][nueva_columna] == espacio_vacio):
                
                #     matriz[fila][columna] = espacio_vacio
                #     matriz[nueva_fila][nueva_columna] = caballo_turno               
                #     print("condicional para movimiento en espacio vacio")
                #     print((nueva_fila,nueva_columna))      
                    
                #     cola.append({
                #         "matriz":matriz,
                #         "jugador": caballo_jugador,
                #         "rama_min_max": rama_min_max,
                #         "pocision_anterior": (fila,columna),
                #         "pocision_actual": (nueva_fila,nueva_columna),
                #         "beneficio_acumulado": beneficio,
                #         "profundidad": profundidad + 1, 
                #         "nodo_padre": nodo_padre + 1
                #     })

                #     nodos.append({
                #         "matriz":matriz,
                #         "jugador": caballo_jugador,
                #         "rama_min_max": rama_min_max,
                #         "pocision_anterior": (fila,columna),
                #         "pocision_actual": (nueva_fila,nueva_columna),
                #         "beneficio_acumulado": beneficio,
                #         "profundidad": profundidad + 1 
                #     })
                #     return
                
                # #Condicional para movimiento en casilla con moneda 
                
                # if(matriz[nueva_fila][nueva_columna] == moneda_uno):
                
                #     matriz[fila][columna] = espacio_vacio
                #     matriz[nueva_fila][nueva_columna] = caballo_turno               
                #     print("condicional para movimiento en moneda uno")
                #     print((nueva_fila,nueva_columna))      
                    
                #     cola.append({
                #         "matriz":matriz,
                #         "jugador": caballo_jugador,
                #         "rama_min_max": rama_min_max,
                #         "pocision_anterior": (fila,columna),
                #         "pocision_actual": (nueva_fila,nueva_columna),
                #         "beneficio_acumulado": beneficio + 1,
                #         "profundidad": profundidad + 1
                #     })
                #     return
                
                # #Condicional para movimiento en casilla con moneda 

                # if(matriz[nueva_fila][nueva_columna] == moneda_dos):
                
                #     matriz[fila][columna] = espacio_vacio
                #     matriz[nueva_fila][nueva_columna] = caballo_turno               
                #     print("condicional para movimiento en moneda dos")
                #     print((nueva_fila,nueva_columna))      
                    
                #     cola.append({
                #         "matriz":matriz,
                #         "jugador": caballo_jugador,
                #         "rama_min_max": rama_min_max,
                #         "pocision_anterior": (fila,columna),
                #         "pocision_actual": (nueva_fila,nueva_columna),
                #         "beneficio_acumulado": beneficio + 1,
                #         "profundidad": profundidad + 2
                #     })
                #     return
                
            return
        return 

   
    
    def mover_caballo():

        aux = 0
        n = 0
        profundidad = 0
        caballo_turno = caballo_maquina
        while True:
        #while cola:
            m = cola[0]
            if (profundidad < m["profundidad"]):
                profundidad = m["profundidad"]
                if m["jugador"] == caballo_maquina:
                    caballo_turno = caballo_jugador
                elif m["jugador"] == caballo_jugador:
                    caballo_turno = caballo_maquina    
            #aux += 1
            m["jugador"] = caballo_turno
            if m["profundidad"] + 1 == 4:
                return

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


    camino = mover_caballo()   
    #print(cola[1])
    #print(camino)

    return camino 

agente_amplitud(Reader('Prueba1.txt'))