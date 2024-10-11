import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def regla_falsa(f, a, b, tol=1e-5, max_iter=100):
    """
    Implementación del método de la regla falsa.

    Args:
        f: La función para la cual se busca la raíz.
        a: Extremo izquierdo del intervalo inicial.
        b: Extremo derecho del intervalo inicial.
        tol: Tolerancia para la convergencia.
        max_iter: Número máximo de iteraciones.

    Returns:
        c: La aproximación de la raíz.
        iteraciones: Número de iteraciones realizadas.
    """

    if f(a) * f(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")

    iteraciones = 0
    while iteraciones < max_iter:
        c = b - f(b) * (b - a) / (f(b) - f(a))

        if abs(f(c)) < tol:
            break

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iteraciones += 1

    return c, iteraciones

def biseccion(f, a, b, tol=1e-5, max_iter=100):
    """
    Implementación del método de bisección.

    Args:
        f: La función para la cual se busca la raíz.
        a: Extremo izquierdo del intervalo inicial.
        b: Extremo derecho del intervalo inicial.
        tol: Tolerancia para la convergencia.
        max_iter: Número máximo de iteraciones.

    Returns:
        c: La aproximación de la raíz.
        iteraciones: Número de iteraciones realizadas.
    """

    if f(a) * f(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo.")

    iteraciones = 0
    while iteraciones < max_iter:
        c = (a + b) / 2

        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        iteraciones += 1

    return c, iteraciones

def calcular_raiz():
    """
    Función llamada cuando se presiona el botón "Calcular".
    Obtiene los valores de entrada, realiza el cálculo y muestra los resultados.
    """

    try:
        # Verificar que todos los campos tengan valores
        if not entry_funcion.get() or not entry_a.get() or not entry_b.get() or not entry_tol.get() or not entry_max_iter.get():
            resultado_label.config(text="Por favor, ingrese todos los datos.")
            return

        # Obtener la función desde el cuadro de texto y reemplazar ^ por **
        func_str = entry_funcion.get().replace('^', '**')
        f = lambda x: eval(func_str)

        a = float(entry_a.get())
        b = float(entry_b.get())
        tol = float(entry_tol.get())
        max_iter = int(entry_max_iter.get())

        # Seleccionar el método
        metodo = metodo_var.get()
        if metodo == "Regla Falsa":
            raiz, iteraciones = regla_falsa(f, a, b, tol, max_iter)
        elif metodo == "Bisección":
            raiz, iteraciones = biseccion(f, a, b, tol, max_iter)
        else:
            resultado_label.config(text="Método no válido.")
            return

        resultado_label.config(text=f"Raíz aproximada: {raiz:.6f}\nIteraciones: {iteraciones}")

        # Graficar la función
        x_vals = np.linspace(a - 1, b + 1, 100)  # Ajusta el rango según sea necesario
        y_vals = f(x_vals)

        ax.clear()
        ax.plot(x_vals, y_vals, label='f(x)')
        ax.axhline(0, color='black', linestyle='--')
        ax.axvline(raiz, color='red', linestyle='--', label=f'Raíz: {raiz:.2f}')
        ax.legend()
        canvas.draw()

    except Exception as e:
        resultado_label.config(text=f"Error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Métodos Numéricos para Encontrar Raíces")

# Cuadro para la función
frame_funcion = ttk.Frame(ventana)
frame_funcion.pack(padx=10, pady=10)

label_funcion = ttk.Label(frame_funcion, text="Función f(x):")
label_funcion.pack(side=tk.LEFT)

entry_funcion = ttk.Entry(frame_funcion)
entry_funcion.pack(side=tk.LEFT)

# Cuadro para los intervalos
frame_intervalos = ttk.Frame(ventana)
frame_intervalos.pack(padx=10, pady=10)

label_a = ttk.Label(frame_intervalos, text="a:")
label_a.pack(side=tk.LEFT)

entry_a = ttk.Entry(frame_intervalos)
entry_a.pack(side=tk.LEFT)

label_b = ttk.Label(frame_intervalos, text="b:")
label_b.pack(side=tk.LEFT)

entry_b = ttk.Entry(frame_intervalos)
entry_b.pack(side=tk.LEFT)

# Cuadro para la tolerancia y máximo de iteraciones
frame_parametros = ttk.Frame(ventana)
frame_parametros.pack(padx=10, pady=10)

label_tol = ttk.Label(frame_parametros, text="Tolerancia:")
label_tol.pack(side=tk.LEFT)

entry_tol = ttk.Entry(frame_parametros)
entry_tol.pack(side=tk.LEFT)
entry_tol.insert(0, "1e-5")  # Valor predeterminado

label_max_iter = ttk.Label(frame_parametros, text="Máximo de iteraciones:")
label_max_iter.pack(side=tk.LEFT)

entry_max_iter = ttk.Entry(frame_parametros)
entry_max_iter.pack(side=tk.LEFT)
entry_max_iter.insert(0, "100")  # Valor predeterminado

# Selección del método
frame_metodo = ttk.Frame(ventana)
frame_metodo.pack(padx=10, pady=10)

metodo_var = tk.StringVar(value="Regla Falsa")
label_metodo = ttk.Label(frame_metodo, text="Método:")
label_metodo.pack(side=tk.LEFT)

metodo_regla_falsa = ttk.Radiobutton(frame_metodo, text="Regla Falsa", variable=metodo_var, value="Regla Falsa")
metodo_regla_falsa.pack(side=tk.LEFT)

metodo_biseccion = ttk.Radiobutton(frame_metodo, text="Bisección", variable=metodo_var, value="Bisección")
metodo_biseccion.pack(side=tk.LEFT)

# Botón para calcular
calcular_button = ttk.Button(ventana, text="Calcular", command=calcular_raiz)
calcular_button.pack(pady=10)

# Etiqueta para mostrar el resultado
resultado_label = ttk.Label(ventana, text="")
resultado_label.pack()

# Gráfico
fig = plt.Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

ventana.mainloop()