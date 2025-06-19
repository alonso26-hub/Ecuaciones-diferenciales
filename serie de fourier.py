# series de fourier con gráfica
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy import symbols, integrate, cos, sin, pi, lambdify

x = symbols('x')

def calcular_fourier(fx,L,N):
    a0 = (1/L) * integrate(fx, (x,-L,L))
    an = []
    bn = []
    for n in range(1,N+1):
        an_i = (1/L) * integrate(fx*cos(n*pi*x/L), (x,-L,L))
        bn_i = (1/L) * integrate(fx*sin(n*pi*x/L), (x,-L,L))
        an.append(an_i)
        bn.append(bn_i)
    return a0, an, bn

def mostrar_resultados(a0, an, bn, N):
    print(f"\na0/2 = {sp.simplify(a0/2)}")
    for n in range(1, N + 1):
        print(f"a{n} = {sp.simplify(an[n-1])} | b{n} = {sp.simplify(bn[n-1])}")

def graficar_fourier(fx, a0, an, bn, L, N, num_puntos=1000):
    puntos=np.linspace(-L,L,num_puntos)
    f_numeric=lambdify(x,fx,'numpy')
    f_real=f_numeric(puntos)

    suma = a0/2
    for n in range(1,N+1):
       suma += an[n-1] * cos(n*pi*x/L) + bn[n-1] *sin(n*pi*x/L)
    f_aprox_func = lambdify(x, suma, 'numpy')
    f_aprox = f_aprox_func(puntos)

# aqui cambias el tamaño de la gráfica y colores 
    plt.figure(figsize=(10,6))
    plt.plot(puntos,f_real,label='Función original',color='skyblue')
    plt.plot(puntos,f_aprox, label=f'Serie de Fourier (N={N})',color='magenta',linestyle='--')
    plt.title('Aproximación con Serie de Fourier')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

def ingresar_funcion():
    expr = input("Ingrese la función f(x): ")
    fx = sp.sympify(expr)
    return fx

# aqui puedes cambiar la función predeterminada, yo ocupe la vista en clase con el profesor 
def main():
    while True:
        print("\n SERIES DE FOURIER ")
        print("1) Ingresa tu función")
        print("2) Usar este ejemplo (f(x) = x en [-pi, pi])")
        print("3) Salir")
        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '1':
            fx = ingresar_funcion()
            entrada = input("Ingrese el valor de L (intervalo [-L, L]): ")
            L = float(sp.N(sp.sympify(entrada)))
            N = int(input("Ingrese el número de términos N que desea calcular: "))
            print(f"\nCalculando Serie de Fourier para f(x) = {fx} en [-{L}, {L}] con {N} términos...")
            a0,an,bn=calcular_fourier(fx,L,N)
            mostrar_resultados(a0,an,bn,N)
            graficar_fourier(fx,a0,an,bn,L,N)

        elif opcion == '2':
            fx = x
            L = np.pi
            N = 5
            print(f"\nEjemplo precargado: f(x) = x en [-{L}, {L}] con {N} términos...")
            a0,an,bn = calcular_fourier(fx,L,N)
            mostrar_resultados(a0,an,bn,N)
            graficar_fourier(fx,a0,an,bn,L,N)

# aqui puedes cambiar el mensaje de despedida como "adiós otaku"
        elif opcion == '3':
            print("¡adiós, cuidate y suerte!")
            break
# y aqui puedes poner un mensaje para cuando no sigan las instrucciones
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
