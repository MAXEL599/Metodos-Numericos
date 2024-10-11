import numpy as np
from time import *
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
import re

gx = []
gy = []

def newton_raphson_method(x, f, df, maxiter, tol): 
    for n in range(maxiter):
        y = x
        x = x - f(x) / df(x)
        gy.append(x)
        gx.append(n + 1)
        if abs(x - y) <= tol:
            return [x, n]
    return [x, 999999]

def grafico():
    plt.plot(gx, gy, 'r')
    plt.title('Método de Newton-Raphson')
    plt.xlabel("Número de iteraciones")
    plt.ylabel("Valor de X")
    plt.show()

def run_newton_raphson():
    try:
        f_str = entry_f.get().replace("^", "**")
        df_str = entry_df.get().replace("^", "**")
        
        # Reemplazar patrones como '2x' por '2*x'
        f_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', f_str)
        df_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', df_str)
        
        X0 = float(entry_X0.get())
        maxite = int(entry_maxite.get())
        tol = float(entry_tol.get())
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
        return

    # Definir las funciones f(x) y f'(x) a partir de las cadenas de entrada
    f = lambda x: eval(f_str)
    df = lambda x: eval(df_str)

    # Limpiar las listas gx y gy antes de cada ejecución
    gx.clear()
    gy.clear()
    gy.append(X0)
    gx.append(0)

    [x, k] = newton_raphson_method(X0, f, df, maxite, tol)

    if k == 999999:
        result_label.config(text="El método diverge o no converge para la cota de error pedida")
    else:
        result_label.config(text=f"La raíz buscada es: {x}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Método de Newton-Raphson")

tk.Label(root, text="f(x):").grid(row=0, column=0)
entry_f = tk.Entry(root)
entry_f.grid(row=0, column=1)

tk.Label(root, text="f'(x):").grid(row=1, column=0)
entry_df = tk.Entry(root)
entry_df.grid(row=1, column=1)

tk.Label(root, text="X0:").grid(row=2, column=0)
entry_X0 = tk.Entry(root)
entry_X0.grid(row=2, column=1)

tk.Label(root, text="Número máximo de iteraciones:").grid(row=3, column=0)
entry_maxite = tk.Entry(root)
entry_maxite.grid(row=3, column=1)

tk.Label(root, text="Tolerancia:").grid(row=4, column=0)
entry_tol = tk.Entry(root)
entry_tol.grid(row=4, column=1)

run_button = tk.Button(root, text="Ejecutar", command=run_newton_raphson)
run_button.grid(row=5, column=0, columnspan=2)

graph_button = tk.Button(root, text="Ver Gráfica", command=grafico)
graph_button.grid(row=6, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=7, column=0, columnspan=2)

root.mainloop()