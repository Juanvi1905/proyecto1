#Juego de Adivinanza: Crea un juego donde el programa selecciona
#un número aleatorio y el usuario tiene que adivinarlo.

import tkinter as tk
import random
numero_intentos = 5

def comprobar_adivinanza():
    try:
        global numero_intentos
        numero_adivinanza = int(entrada.get())
        if numero_intentos > 0:
            if numero_adivinanza == numero_aleatorio:
                resultado.config(text="¡Correcto! Has ganado perro.")
            elif numero_adivinanza < numero_aleatorio:
                resultado.config(text="Intenta con un número más grande.")
            else:
                resultado.config(text="Intenta con un número más pequeño.")
            numero_intentos -= 1
            numero_intentosimprimir.config(text=f"te quedan {numero_intentos} intentos")
            numero_intentosimprimir.pack(pady=10)
        elif numero_intentos == 0:
            numero_intentosimprimir.config(text=f"PERDISTE CABRON")
            numero_intentosimprimir.pack(pady=10)
    except ValueError:
        resultado.config(text="Ingresa un número válido.")


def reiniciar_juego():
    global numero_aleatorio, numero_intentos
    numero_intentos = 5
    numero_aleatorio = random.randint(1, 10)
    resultado.config(text="¡Juego reiniciado! Adivina un nuevo número.")
    numero_intentosimprimir.config(text="")
    numero_intentosimprimir.pack(pady=10)
    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Adivina el número")


numero_aleatorio = random.randint(1, 10)

instruccion = tk.Label(ventana, text="Adivina el número entre 1 y 10:")
instruccion.pack(pady=10)


entrada = tk.Entry(ventana)
entrada.pack(pady=5)


boton_adivinar = tk.Button(ventana, text="Adivinar", command=comprobar_adivinanza)
boton_adivinar.pack(pady=5)

resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)
numero_intentosimprimir = tk.Label(ventana, text="")
numero_intentosimprimir.pack(pady=10)

boton_reiniciar = tk.Button(ventana, text="Reiniciar Juego", command=reiniciar_juego)
boton_reiniciar.pack(pady=5)

ventana.mainloop()
