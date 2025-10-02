# 🔍 Búsqueda del Máximo Global - Función Cuadrática

## 📋 Descripción del Proyecto

Este programa encuentra el máximo global de la función cuadrática f(x) = x² - 3x + 4 mediante evaluación exhaustiva en un rango amplio de valores.

## 🧮 Función Analizada

```python

f(x) = x² - 3x + 4

```

### Características de la Función: 

- Tipo: Parábola cóncava hacia arriba (coeficiente de x² positivo)

- Forma: U-shaped

- Comportamiento:

    - Mínimo en el vértice

    - Máximo en los extremos del dominio

    - Sin máximo global finito (crece hacia infinito)


## ⚙️ Implementación del Algoritmo

### Método de Búsqueda

```python

def encontrar_maximo_global():
    # Evaluar en rango amplio: -100 a 100
    x_values = np.linspace(-100, 100, 1000)
    y_values = f(x_values)
    
    # Encontrar índice del valor máximo
    max_idx = np.argmax(y_values)
    x_max = x_values[max_idx]
    y_max = y_values[max_idx]

```

## Parámetros de Búsqueda:

- Dominio evaluado: [-100, 100]

- Número de puntos: 1000

- Método: Evaluación exhaustiva

- Precisión: 0.2 unidades (200/1000)

## 📊 Resultado Obtenido

```text

Función: f(x) = x² - 3x + 4
Máximo global encontrado en:
x = -100.00
f(x) = 10304.00

```
### Análisis del Resultado:

- Posición del máximo: x = -100

- Valor máximo: f(x) = 10304

- Interpretación: La función alcanza su valor máximo en el extremo izquierdo del dominio evaluado

## 🎯 Explicación Matemática

Comportamiento de la Función

```python

f(x) = x² - 3x + 4

```

- Derivada: f'(x) = 2x - 3

- Punto crítico: x = 1.5 (MÍNIMO, no máximo)

- Concavidad: Positiva (coeficiente de x² = 1 > 0)

- Conclusión: No tiene máximo global finito

### ¿Por qué el máximo está en x = -100?

- Al ser una parábola hacia arriba, crece hacia infinito en ambos extremos

- En el dominio limitado [-100, 100], el máximo está en el extremo izquierdo

- Si ampliamos el dominio (ej: [-1000, 1000]), el máximo estaría en x = -1000

## 👥 Autores
- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  

- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)