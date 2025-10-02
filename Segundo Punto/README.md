# 🧬 Algoritmo Genético para el Problema del Viajante (TSP)

## 📋 Descripción del Proyecto

Implementación completa de un algoritmo genético para resolver el Problema del Viajante (TSP) con visualización de resultados y experimentación de parámetros.

## 🎯 Características Principales

### 🔧 Funcionalidades Implementadas

- Generación automática de ciudades con coordenadas aleatorias

- Algoritmo genético completo con selección, cruce y mutación

- Visualización interactiva de rutas y convergencia

- Experimentación sistemática con tasas de mutación

- Métricas de rendimiento en tiempo real

## ⚙️ Componentes del Algoritmo

1. 🏙️ Generación de Ciudades

```python

def generate_cities(self, n):
    return [(random.random(), random.random()) for _ in range(n)]
```

- Genera n ciudades con coordenadas entre 0 y 1

- Distribución uniforme para pruebas representativas

2. 📊 Función de Fitness

```python

def fitness(self, route):
    return 1 / self.total_distance(route)

```

- Fitness inversamente proporcional a la distancia

- Mayor fitness = mejor solución

3. 🏆 Selección por Torneo

```python

def selection(self, population, fitnesses):
    tournament_size = 3
    # Selecciona 3 individuos aleatorios
    # Elige el de mayor fitness

```

- Tamaño de torneo: 3 individuos

- Presión selectiva: moderada

4. 🧬 Mutación por Intercambio

```python

def swap_mutation(self, route):
    if random.random() < self.mutation_rate:
        # Intercambia dos ciudades aleatorias

```

- Tasa configurable (por defecto 0.02)

- Introduce diversidad en la población

## 📈 Parámetros del Algoritmo

```text

Parámetro	          Valor Por Defecto	 Descripción
Número de Ciudades	  10	                 Tamaño del problema TSP
Tamaño de Población	  100	             Individuos por generación
Tasa de Mutación	  0.02	             Probabilidad de mutación
Generaciones	      100	             Iteraciones del algoritmo
Tamaño de Torneo	  3	                 Individuos en selección

```

## 🎪 Resultados del Ejemplo

### 🏁 Ejecución Principal

```python

Ciudades generadas:
  Ciudad 0: (0.252, 0.724)
  Ciudad 1: (0.429, 0.355)
  ...
  Ciudad 9: (0.929, 0.324)

Generación 0: Mejor distancia = 3.6418
Generación 20: Mejor distancia = 2.6133
...
Generación 80: Mejor distancia = 2.6133

Mejor ruta encontrada: [8, 0, 3, 5, 1, 9, 2, 4, 6, 7]
Distancia total: 2.6133

```

## 🔬 Experimentación con Tasas de Mutación


```text

Tasa    Mutación	Mejor Distancia	Fitness
0.01	2.9949	    0.3339
0.05	3.0924	    0.3234
0.10	2.5234	    0.3963
0.20	2.4732	    0.4043

```

## 📊 Análisis de Resultados

### 🎯 Patrones Observados

1. Convergencia rápida: Mejora significativa en primeras 20 generaciones

2. Estancamiento: Mantiene misma solución por múltiples generaciones

3. Tasa óptima de mutación: 0.1-0.2 para este problema específico

## 📈 Comportamiento del Algoritmo

- Exploración inicial: Amplia búsqueda en espacio de soluciones

- Explotación posterior: Refinamiento de soluciones prometedoras

- Balance exploración-explotación: Controlado por tasa de mutación


## 🎨 Visualizaciones Generadas

1. 📍 Mapa de Ruta Óptima

- Ciudades representadas como puntos rojos

- Ruta conectada con líneas azules

- Etiquetas numeradas para cada ciudad

- Distancia total mostrada en título

2. 📈 Gráfica de Convergencia

- Línea roja: Mejor fitness por generación

- Línea azul: Fitness promedio por generación

- Tendencia de mejora a lo largo del tiempo

## 📚 Aplicaciones Prácticas

### 🚚 Logística y Transporte

- Optimización de rutas de reparto

- Planificación de circuitos de distribución

### 🎒 Turismo y Viajes

- Diseño de itinerarios turísticos eficientes

- Circuitos de visitas a puntos de interés

### 🔬 Investigación Operativa

- Benchmarking de algoritmos de optimización

- Estudio de metaheurísticas para problemas NP-duros

## 👥 Autores
- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  

- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)