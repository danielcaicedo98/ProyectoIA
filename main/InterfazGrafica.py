import tkinter as tk
from Reader import get_matriz

# Definir colores para cada valor
colores = {
    0: "white",  # Casilla libre
    1: "black",  # Obstáculo
    2: "red",    # Punto de fuego
    3: "blue",   # Cubeta de un litro
    4: "green",  # Cubeta de dos litros
    5: "orange", # Punto de inicio
    6: "purple"  # Hidrante
}

# Definir la matriz (puedes reemplazar esto con la matriz que desees mostrar)
matriz = get_matriz()

# Función para crear la interfaz gráfica
def crear_interfaz(matriz):
    root = tk.Tk()
    root.title("Representación de Matriz")

    # Crear un widget Canvas para mostrar la matriz
    canvas = tk.Canvas(root, width=30*len(matriz[0]), height=30*len(matriz))
    canvas.pack()

    # Dibujar cuadros en el Canvas según los valores de la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = matriz[i][j]
            color = colores.get(valor, "white")
            canvas.create_rectangle(j*30, i*30, (j+1)*30, (i+1)*30, fill=color, outline="black")

    root.mainloop()

# Llamar a la función para crear la interfaz gráfica con la matriz
crear_interfaz(matriz)
