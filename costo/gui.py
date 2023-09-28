import tkinter as tk
import time
from algoritmo_costo import agente
from Reader import get_matriz
colores = {
    0: "white",  # Casilla libre
    1: "black",  # Obstáculo
    2: "red",    # Punto de fuego
    3: "blue",   # Cubeta de un litro
    4: "green",  # Cubeta de dos litros
    5: "orange", # Punto de inicio
    6: "purple"  # Hidrante
}



# Define la matriz inicial
matriz_inicial = get_matriz()


import tkinter as tk
#from Reader import get_matriz
import time

# Definir colores para cada valor
colores = {
    0: "white",  # Casilla libre
    1: "black",  # Obstáculo
    2: "red",    # Punto de fuego
    3: "purple",   # Cubeta de un litro
    4: "green",  # Cubeta de dos litros
    5: "orange", # Punto de inicio
    6: "blue"  # Hidrante
}

# Define la secuencia de movimiento

secuencia = agente()
# Definir la matriz (puedes reemplazar esto con la matriz que desees mostrar)
matriz = matriz_inicial

# Función para crear la interfaz gráfica
def crear_interfaz(matriz):
    root = tk.Tk()
    root.title("Representación de Matriz")

    # Crear un widget Canvas para mostrar la matriz
    canvas = tk.Canvas(root, width=30 * len(matriz[0]), height=30 * len(matriz))
    canvas.pack()

    # Función para actualizar la matriz en el canvas
    def actualizar_matriz():
        canvas.delete("all")  # Limpiar el canvas
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                valor = matriz[i][j]
                color = colores.get(valor, "white")
                canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color, outline="black")

    # Llamar a la función para actualizar la matriz
    actualizar_matriz()

  #  Función para mover el número 5
    def mover_numero(posiciones):
        for posicion in posiciones:
            pos = 0
            if  matriz[posicion[0]][posicion[1]] == 3:
                matriz[posicion[0]][posicion[1]] = 5
                pos = 3
            elif  matriz[posicion[0]][posicion[1]] == 4:
                matriz[posicion[0]][posicion[1]] = 5
                pos = 4  
            elif  matriz[posicion[0]][posicion[1]] == 6:
                matriz[posicion[0]][posicion[1]] = 5
                pos = 6     
            else:
                matriz[posicion[0]][posicion[1]] = 5

            actualizar_matriz()
            root.update()  # Actualizar la ventana
            time.sleep(0.5)  # Pausa de medio segundo para ver el movimiento
            if  matriz[posicion[0]][posicion[1]] == 2:
                matriz[posicion[0]][posicion[1]] = 5
            else:
                matriz[posicion[0]][posicion[1]] = pos

            actualizar_matriz()
            root.update()  # Actualizar la ventana
            time.sleep(0.1)  # Pausa de 0.1 segundos entre movimientos
   



    # Crear un botón para iniciar el movimiento
    boton_iniciar = tk.Button(root, text="Iniciar Movimiento", command=lambda: mover_numero(secuencia))
    boton_iniciar.pack()

    root.mainloop()

# Llamar a la función para crear la interfaz gráfica con la matriz
crear_interfaz(matriz)

