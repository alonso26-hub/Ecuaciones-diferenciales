import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from ipywidgets import interact, Dropdown, Text, FloatSlider

# === Funciones predefinidas ===
def f1(t): return t
def f2(t): return np.sin(t)
def f3(t): return np.exp(t)
def f4(t): return np.heaviside(t, 1)
def f5(t): return t**2

funciones = {
    "t": f1,
    "sin(t)": f2,
    "e^t": f3,
    "u(t) (escalón unitario)": f4,
    "t^2": f5,
    "personalizada": None
}

# === Función para evaluar funciones personalizadas ===
def parse_func(texto):
    def func(t):
        try:
            return eval(texto, {"t": t, "np": np, "sin": np.sin, "cos": np.cos, "exp": np.exp, "log": np.log, "heaviside": np.heaviside})
        except:
            return 0*t
    return func

# === Cálculo de la convolución ===
def convolucion(f, g, t):
    integrando = lambda tau: f(tau) * g(t - tau)
    resultado, _ = quad(integrando, 0, t)
    return resultado

# === Función principal para graficar y mostrar resultados ===
def graficar_convolucion(nombre_f, texto_f, nombre_g, texto_g, tmax=10):
    f = parse_func(texto_f) if nombre_f == "personalizada" else funciones[nombre_f]
    g = parse_func(texto_g) if nombre_g == "personalizada" else funciones[nombre_g]

    t_vals = np.linspace(0, tmax, 20)  # menos puntos para imprimir resultados legibles
    conv_vals = np.array([convolucion(f, g, t) for t in t_vals])

    plt.figure(figsize=(10, 5))
    plt.plot(t_vals, conv_vals, label="Convolución f * g")
    plt.title("Convolución de dos funciones")
    plt.xlabel("t")
    plt.ylabel("Resultado")
    plt.grid(True)
    plt.legend()
    plt.show()

    print("\nResultados de la convolución en puntos seleccionados:")
    for t, val in zip(t_vals, conv_vals):
        print(f"t = {t:.2f}  →  convolución = {val:.4f}")

# === Interactivo ===
interact(
    graficar_convolucion,
    nombre_f=Dropdown(options=list(funciones.keys()), value="t", description="f(t):"),
    texto_f=Text(value="t", description="f(t) =", placeholder="ej. sin(t) + t**2"),
    nombre_g=Dropdown(options=list(funciones.keys()), value="sin(t)", description="g(t):"),
    texto_g=Text(value="sin(t)", description="g(t) =", placeholder="ej. exp(-t)"),
    tmax=FloatSlider(value=10, min=1, max=20, step=1, description="t máximo:")
)
