import tkinter as tk
from PIL import Image, ImageTk
from Amplitud import *
import time
from tkinter import filedialog
from Amplitud import agente_amplitud
from Avara import agente_avara
from CostoUniforme import agente
from A_Estrella import agente_a_estrella
from Profundidad import agente_profundidad
from Config import route
from Reader import Reader

global ventana
global soldier
global lienzo
global mapa
global listaMovimientos
global listaObjetos
global boton1, boton2, botonVolver
global boton3, boton4, boton5, mapaBtn, siguienteBtn,velocidad,_matriz
global pos_esp,pos_sup
global taked_esp
taked_esp = False

velocidad = 0.4




listaObjetos = []


def crearSprite(x,y):
    # Cargar la hoja de sprites completa
    imagen = Image.open("Sprites/sprites.png")

    # Coordenadas del área a recortar
    x_inicio = x * 16
    y_inicio = y * 16
    ancho_recorte =16
    alto_recorte = 16

    # Recortar la imagen
    imagen_recortada = imagen.crop((x_inicio, y_inicio, x_inicio + ancho_recorte, y_inicio + alto_recorte))

    # Convertir la imagen recortada a PhotoImage para Tkinter
    imagen_escala = imagen_recortada.resize((64, 64), Image.ADAPTIVE)
    imagen_tk = ImageTk.PhotoImage(imagen_escala)

    # Crear una etiqueta para mostrar la imagen
    return imagen_tk
def encontrar_posicion(matriz, numero):
        # Encuentra la posición actual del número en la matriz
        for fila in range(len(matriz)):
            for columna in range(len(matriz[fila])):
                if matriz[fila][columna] == numero:
                    return fila, columna
        return None 

def dibujarSprites(imagen):
    global soldier
    global lienzo
    global mapa
    global pos_esp,pos_sup

    x = 0
    y = 0
    filas = 10
    columnas = 10
    sprite_size = 64
    
        

    for fila in range(filas):
        for columna in range(columnas):
            posX = x + columna * sprite_size
            posY = y + fila * sprite_size
            

            lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[0])

            if(mapa[fila][columna] == 1):
                piedra = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[1])
                lienzo.lift(piedra)
            elif(mapa[fila][columna] == 2):
                orco = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[2])
                lienzo.lift(orco)
                agregarObjetoLista(fila,columna,orco)
            elif(mapa[fila][columna] == 6):
                potion = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[3])
                lienzo.lift(potion)
            elif(mapa[fila][columna] == 5):
                soldier = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[4])
                lienzo.lift(soldier)
            elif(mapa[fila][columna] == 3):
                
                
                sword = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[5])
                lienzo.lift(sword)
                agregarObjetoLista(fila,columna,sword)
            elif(mapa[fila][columna] == 4):
                
                superSword = lienzo.create_image(posX, posY, anchor=tk.NW, image=imagen[6])
                lienzo.lift(superSword)
                agregarObjetoLista(fila,columna,superSword)

def agregarObjetoLista(fila,columna,objeto):
    global listaObjetos

    listaObjetos.append([fila,columna,objeto])

def crearSprites():

    orcoPng = Image.open("Sprites/Orco.png")
    soldierPng = Image.open("Sprites/Soldier.png")
    potionPng = Image.open("Sprites/Potion.png")
    swordPng = Image.open("Sprites/Sword.png")
    superSwordPng = Image.open("Sprites/SuperSword.png")
    potionGrande = potionPng.resize((64, 64), Image.ADAPTIVE)
    soldierGrande = soldierPng.resize((41,64), Image.ADAPTIVE)
    swordGrande = swordPng.resize((64,64), Image.ADAPTIVE)
    superSwordGrande = superSwordPng.resize((64,64), Image.ADAPTIVE)

    sprites = []
    imagenPasto = crearSprite(19,8)
    imagenPiedra = crearSprite(17,4)
    imagenFuego = crearSprite(0,12)
    
    orco = ImageTk.PhotoImage(orcoPng)
    soldier = ImageTk.PhotoImage(soldierGrande)
    potion = ImageTk.PhotoImage(potionGrande)
    sword = ImageTk.PhotoImage(swordGrande)
    superSword = ImageTk.PhotoImage(superSwordGrande)

    sprites.append(imagenPasto)
    sprites.append(imagenPiedra)
    sprites.append(orco)
    sprites.append(potion)
    sprites.append(soldier)
    sprites.append(sword)
    sprites.append(superSword)
    #sprites.append(imagenFuego)

    return sprites 

def moverSoldado(y, direccion):
    global lienzo
    global soldier
    global ventana
    
    lienzo.lift(soldier)

    if(direccion == "Abajo"):
        print("Movimiento: ", direccion)
        lienzo.move(soldier, 0, 64)
    elif(direccion == "Arriba"):
        print("Movimiento: ", direccion)
        lienzo.move(soldier, 0, -64)
    elif(direccion == "Derecha"):
        print("Movimiento: ", direccion)
        lienzo.move(soldier, 64, 0)
    elif(direccion == "Izquierda"):
        print("Movimiento: ", direccion)
        lienzo.move(soldier, -64, 0)

    ventana.update()

    return 0

    

def generarVentana():
    global lienzo
    global ventana
    global mapa
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5, mapaBtn, siguienteBtn

    #TODO Ahora hay que hacer que cuando le de click al boton el soldado empiece a moverse por el mapa

    

    ventana = tk.Tk()
    ventana.title("Mostrar Primer Sprite")
    botonVolver = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("Volver"))
    boton1 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton1"))
    boton2 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton2"))
    boton3 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton3"))
    boton4 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton4"))
    boton5 = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("boton5"))
    mapaBtn = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("mapaBtn"))    
    siguienteBtn = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mensaje("SiguienteBtn"))


    lienzo = tk.Canvas(ventana, width=640, height=640)
    lienzo.pack()



    """ mostrarOpcionesIniciales() """
    mostrarSeleccionarMapa()
    

    


    #moverSoldado(lienzo)

    # Ejecutar la ventana
    ventana.geometry("640x640")
    ventana.mainloop()

def identificarMovimientosCompletos():
    global listaMovimientos, velocidad
    global taked_esp,pos_sup,pos_esp

    for lista_de_movimientos in listaMovimientos:

        for i in range(1, len(lista_de_movimientos)):
            fila_anterior, columna_anterior = lista_de_movimientos[i - 1]
            fila_actual, columna_actual = lista_de_movimientos[i]

            # Comparamos las filas y columnas para determinar la dirección
            if fila_anterior < fila_actual:
                direccion = "Abajo"
            elif fila_anterior > fila_actual:
                direccion = "Arriba"
            elif columna_anterior < columna_actual:
                direccion = "Derecha"
            elif columna_anterior > columna_actual:
                direccion = "Izquierda"

            
            moverSoldado(0, direccion)
            


            fil_esp,col_esp = pos_esp
            fil_sup,col_sup = pos_sup           

            if (fila_actual, columna_actual) == (fil_esp,col_esp) and (not taked_esp): 
                taked_esp = True
                eliminarObjeto(fila_actual, columna_actual)               
            if (fila_actual, columna_actual) == (fil_sup,col_sup) and (not taked_esp): 
                taked_esp = True
                eliminarObjeto(fila_actual, columna_actual)    
            if (fila_actual, columna_actual) != (fil_esp,col_esp) and (fila_actual, columna_actual) != (fil_sup,col_sup):     
                eliminarObjeto(fila_actual, columna_actual)
            time.sleep(velocidad)

# def generarMovimientosAmplitud():
#     global listaMovimientos
#     global lienzo

#     destruirBotones()
#     sprites = crearSprites()
#     dibujarSprites(sprites)

#     cicloBombero(mapa)
#     listaMovimientos = getListaMovimientos()
#     print("Lista movimientos: ", listaMovimientos)
#     identificarMovimientosCompletos()
#     mostrarSeleccionarMapa()


def eliminarObjeto(fila, columna):
    global listaObjetos
    global lienzo

    for sublista in listaObjetos:
        if sublista[0] == fila and sublista[1] == columna:           
            lienzo.delete(sublista[2])


def mostrarSeleccionarMapa():

    global lienzo, OpcionesImg
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5, mapaBtn

    destruirBotones()

    mapaBtn = tk.Button(ventana, text="Mapa",width=19,height=1, command=lambda: abrirArchivos())
    mapaBtn.place(x=46, y=328)

    agregarImagenMenu("SeleccioneMapa")

def mostrarDatosFinales(nodos, profundidad, tiempo):

    global lienzo, OpcionesImg
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5, mapaBtn, siguienteBtn
    global taked_esp 
    taked_esp = False

    destruirBotones()


    # Coloca las etiquetas en la ventana
    """ lblNodos.pack() """


    siguienteBtn = tk.Button(ventana, text="Continuar",width=19,height=1, command=lambda: mostrarSeleccionarMapa())
    siguienteBtn.place(x=46, y=582)

    agregarImagenMenu("DatosFinales")
    lblNodos = lienzo.create_text(130, 123, text=nodos, fill="white", font=("Helvetica", 24))
    lblProfundidad = lienzo.create_text(130, 295, text=profundidad, fill="white", font=("Helvetica", 24))
    lblNTiempo = lienzo.create_text(130, 455, text=tiempo, fill="white", font=("Helvetica", 24))
    lienzo.lift(lblNodos)
    lienzo.lift(lblProfundidad)
    lienzo.lift(lblNTiempo)

def mostrarOpcionesIniciales():
    global lienzo, OpcionesImg
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5, mapaBtn
    

    destruirBotones()

    boton1 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: mostrarOpcionesInformada())
    boton1.place(x=46, y=220)

    boton2 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: mostrarOpcionesNoInformada())
    boton2.place(x=46, y=388)


    agregarImagenMenu("Opciones")

def generarMovimientosProfundidad(_m):
    global listaMovimientos
    global lienzo

    destruirBotones()
    sprites = crearSprites()
    dibujarSprites(sprites)

    

    try:
        profundidad1 = agente_profundidad(_m)
        #print(agente_costo["reporte"])
        listaMovimientos = [profundidad1["camino"]]
        print("Lista movimientos: ", listaMovimientos)
        identificarMovimientosCompletos()
        print("NODOS",profundidad1["reporte"]["nodos_expandidos"])
        print("PROFUNDIDAD",profundidad1["reporte"]["profundidad_arbol"])
        print("TIEMPO",profundidad1["reporte"]["tiempo_computo"])
        nodos = profundidad1["reporte"]["nodos_expandidos"]
        profundidad = profundidad1["reporte"]["profundidad_arbol"]
        tiempo = profundidad1["reporte"]["tiempo_computo"]
    except Exception as e:                
        mostrarDatosFinales("falla de algoritmo", "falla de algoritmo", "falla de algoritmo")
    else:
        mostrarDatosFinales(nodos, profundidad, tiempo)
    #mostrarSeleccionarMapa()            

def generarMovimientosAmplitud(_m):
    
    global listaMovimientos
    global lienzo

    destruirBotones()
    sprites = crearSprites()
    dibujarSprites(sprites)
    try:
        agente_amplitud_interfaz = agente_amplitud(_m)
        print(agente_amplitud_interfaz["reporte"])
        listaMovimientos = [agente_amplitud_interfaz["camino"]]
        print("Lista movimientos: ", listaMovimientos)
        identificarMovimientosCompletos()
        print("NODOS",agente_amplitud_interfaz["reporte"]["nodos_expandidos"])
        print("PROFUNDIDAD",agente_amplitud_interfaz["reporte"]["profundidad_arbol"])
        print("TIEMPO",agente_amplitud_interfaz["reporte"]["tiempo_computo"])

        nodos = agente_amplitud_interfaz["reporte"]["nodos_expandidos"]
        profundidad = agente_amplitud_interfaz["reporte"]["profundidad_arbol"]
        tiempo = agente_amplitud_interfaz["reporte"]["tiempo_computo"]
        
    except Exception as e:                
        mostrarDatosFinales("falla de algoritmo", "falla de algoritmo", "falla de algoritmo")
    else:
        mostrarDatosFinales(nodos, profundidad, tiempo)

    
    
        #mostrarSeleccionarMapa()

def generarMovimientosCosto(_m):
    global listaMovimientos
    global lienzo

    destruirBotones()
    sprites = crearSprites()
    dibujarSprites(sprites)

    try:
        #cicloBombero(mapa)
        agente_costo = agente(_m)
        #print[agente_costo["reporte"]]
        listaMovimientos = [agente_costo["camino"]]
        print("Lista movimientos: ", listaMovimientos)
        identificarMovimientosCompletos()
        print("NODOS",agente_costo["reporte"]["nodos_expandidos"])
        print("PROFUNDIDAD",agente_costo["reporte"]["profundidad_arbol"])
        print("TIEMPO",agente_costo["reporte"]["tiempo_computo"])

        nodos = agente_costo["reporte"]["nodos_expandidos"]
        profundidad = agente_costo["reporte"]["profundidad_arbol"]
        tiempo = agente_costo["reporte"]["tiempo_computo"]
        
    except Exception as e:                
        mostrarDatosFinales("falla de algoritmo", "falla de algoritmo", "falla de algoritmo")
    else:
        mostrarDatosFinales(nodos, profundidad, tiempo)

    
    
    """ mostrarSeleccionarMapa() """

def generarMovimientos_a_estrella(_m):
    global listaMovimientos
    global lienzo

    destruirBotones()
    sprites = crearSprites()
    dibujarSprites(sprites)

    try:
            #print[agente_costo["reporte"]]
        agente_estrella = agente_a_estrella(_m)
        listaMovimientos = [agente_estrella["camino"]]
        print("Lista movimientos: ", listaMovimientos)
        identificarMovimientosCompletos()
        print("NODOS",agente_estrella["reporte"]["nodos_expandidos"])
        print("PROFUNDIDAD",agente_estrella["reporte"]["profundidad_arbol"])
        print("TIEMPO",agente_estrella["reporte"]["tiempo_computo"])

        nodos = agente_estrella["reporte"]["nodos_expandidos"]
        profundidad = agente_estrella["reporte"]["profundidad_arbol"]
        tiempo = agente_estrella["reporte"]["tiempo_computo"]
        
    except Exception as e:                
        mostrarDatosFinales("falla de algoritmo", "falla de algoritmo", "falla de algoritmo")
    else:
        mostrarDatosFinales(nodos, profundidad, tiempo)

    #cicloBombero(mapa)
    

   

    """ mostrarSeleccionarMapa() """

def generarMovimientos_avara(_m):
    # mensaje("avara")
    global listaMovimientos
    global lienzo
    print(1)
    destruirBotones()
    sprites = crearSprites()
    dibujarSprites(sprites)  


    try:
            #cicloBombero(mapa)
        agente_avara1 = agente_avara(_m)
        #print[agente_costo["reporte"]]
        listaMovimientos = [agente_avara1["camino"]]
        print("Lista movimientos: ", listaMovimientos)
        identificarMovimientosCompletos()
        print("NODOS",agente_avara1["reporte"]["nodos_expandidos"])
        print("PROFUNDIDAD",agente_avara1["reporte"]["profundidad_arbol"])
        print("TIEMPO",agente_avara1["reporte"]["tiempo_computo"])

        nodos = agente_avara1["reporte"]["nodos_expandidos"]
        profundidad = agente_avara1["reporte"]["profundidad_arbol"]
        tiempo = agente_avara1["reporte"]["tiempo_computo"]

    except Exception as e:                
        mostrarDatosFinales("falla de algoritmo", "falla de algoritmo", "falla de algoritmo")
    else:
        mostrarDatosFinales(nodos, profundidad, tiempo)

    """ mostrarSeleccionarMapa() """

def abrirArchivos():
    global mapa
    global route,_matriz  
    global pos_esp,pos_sup  
    archivo = filedialog.askopenfilename()  
    
    if archivo:
        _matriz = Reader(archivo)
        pos_sup = encontrar_posicion(_matriz,4)
        pos_esp = encontrar_posicion(_matriz,3)
        print(f"Archivo seleccionado: {archivo}")       
        try:
            mapa = []
            with open(archivo, 'r') as file:
                for linea in file:
                    lista_de_numeros = [int(numero) for numero in linea.split()]
                    mapa.append(lista_de_numeros)

            print("\n\nMAPA SECUNDARIA\n")
            #mostrarMapa(mapa)

            mostrarOpcionesIniciales()
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
    else:
        print("Ningún archivo seleccionado.")


    
    return 0

def mostrarOpcionesNoInformada():
    global lienzo, OpcionesImg
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5,_matriz

    destruirBotones()

    boton3 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: generarMovimientosAmplitud(_matriz))
    boton3.place(x=47, y=160)

    boton4 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: generarMovimientosCosto(_matriz))
    boton4.place(x=47, y=327)

    boton5 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: generarMovimientosProfundidad(_matriz))
    boton5.place(x=47, y=497)

    botonVolver = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mostrarOpcionesIniciales())
    botonVolver.place(x=47, y=600)

    agregarImagenMenu("NoInformadaOpciones")

def mostrarOpcionesInformada():
    
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5

    destruirBotones()

    boton1 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: generarMovimientos_avara(_matriz))
    boton1.place(x=46, y=220)

    boton2 = tk.Button(ventana, text="Seleccionar",width=19,height=1, command=lambda: generarMovimientos_a_estrella(_matriz))
    boton2.place(x=46, y=388)

    botonVolver = tk.Button(ventana, text="Volver",width=19,height=1, command=lambda: mostrarOpcionesIniciales())
    botonVolver.place(x=47, y=600)

    agregarImagenMenu("InformadaOpciones")
    
    

def agregarImagenMenu(Imagen):
    global lienzo, OpcionesImg
    opciones = Image.open(f"Intro/{Imagen}.png")
    OpcionesImg = ImageTk.PhotoImage(opciones)
    imagen = lienzo.create_image(0,0, anchor=tk.NW, image=OpcionesImg)
    lienzo.lift(imagen)


def destruirBotones():
    global boton1, boton2, boton3, botonVolver
    global boton3, boton4, boton5, mapaBtn, siguienteBtn
    
    boton1.destroy()
    boton2.destroy()
    boton3.destroy()
    boton4.destroy()
    boton5.destroy()
    mapaBtn.destroy()
    siguienteBtn.destroy()
    botonVolver.destroy()


def mensaje(mensaje):
    print("Mensaje: ", mensaje)