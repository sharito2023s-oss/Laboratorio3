# primer_punto_maximo_global.py
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Función cuadrática f(x) = x^2 - 3x + 4"""
    return x**2 - 3*x + 4

def encontrar_maximo_global():
    """
    Encuentra el máximo global de la función cuadrática.
    Como es una parábola cóncava hacia arriba, el máximo estará en los extremos del dominio.
    """
    # Evaluamos en un rango amplio
    x_values = np.linspace(-100, 100, 1000)
    y_values = f(x_values)
    
    max_idx = np.argmax(y_values)
    x_max = x_values[max_idx]
    y_max = y_values[max_idx]
    
    print(f"Función: f(x) = x² - 3x + 4")
    print(f"Máximo global encontrado en:")
    print(f"x = {x_max:.2f}")
    print(f"f(x) = {y_max:.2f}")
    
    # Graficar
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, 'b-', linewidth=2, label='f(x) = x² - 3x + 4')
    plt.plot(x_max, y_max, 'ro', markersize=8, label=f'Máximo: ({x_max:.2f}, {y_max:.2f})')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Máximo Global de la Función Cuadrática')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()
    
    return x_max, y_max

if __name__ == "__main__":
    encontrar_maximo_global()