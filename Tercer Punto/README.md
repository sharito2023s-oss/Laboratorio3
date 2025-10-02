# 🎓 Optimización de Horarios Escolares con Algoritmo Genético

## 📋 Descripción del Proyecto

Este proyecto implementa un algoritmo genético para optimizar horarios escolares, considerando múltiples restricciones y preferencias de profesores y materias. El sistema genera horarios balanceados que maximizan la satisfacción de profesores y la distribución equitativa de materias.

## ⚙️ Configuración del Sistema

### 🧑‍🏫 Recursos Humanos

- 4 Profesores: ProfA, ProfB, ProfC, ProfD

- 4 Materias: Matemáticas, Ciencias, Historia, Arte

- 3 Grupos: Grupo1, Grupo2, Grupo3

## 🕐 Horarios Disponibles

1. 🏙️ Generación de Ciudades

```text

Lun-9:00, Lun-11:00, Mar-9:00, Mar-11:00, Mie-9:00, Mie-11:00

```

## 🎯 Sistema de Evaluación (Fitness)

### Puntuación Base: 100 puntos

🔴 Penalizaciones (Restricciones Duras)

- Superposición de profesores: -20 puntos por conflicto

- Superposición de grupos: -30 puntos por conflicto

- Distribución desbalanceada: -2 puntos por variación excesiva

🟢 Bonificaciones (Preferencias)

- Horarios preferidos de profesores: +5 puntos

- Horarios ideales para materias: +3 puntos

## 🧬 Algoritmo Genético Implementado

### Parámetros Principales

```python

population_size = 50    # 50 horarios por generación
generations = 100       # 100 iteraciones
mutation_rate = 0.1     # 10% probabilidad de mutación

```

### Componentes del Algoritmo

1. 🧪 Población Inicial

- Genera horarios aleatorios válidos

- Cada horario contiene 18 clases (6 horarios × 3 grupos)

2. 🏆 Selección por Ruleta

```python

probabilities = [f/total_fitness for f in fitness_scores]
selected = random.choices(population, weights=probabilities, k=population_size)

```

3. 🔀 Cruzamiento de Un Punto

- Combina dos horarios padres en puntos aleatorios

- Genera nuevos horarios hijos

4. 🧬 Mutación Controlada

- Cambia profesor y materia en clases aleatorias

- Tasa configurable (0.05 - 0.3)

5. 🥇 Elitismo

-Conserva el mejor horario entre generaciones

- Previene pérdida de soluciones óptimas


## 📊 Resultados Obtenidos

### Comparativa de Rendimiento

```text

Horario Inicial (Aleatorio): Fitness = 84
Horario Optimizado: Fitness = 153
Mejora: +69 puntos (82% de mejora)

```

### Evolución del Fitness

```text

Generación 0: Mejor fitness = 113
Generación 20: Mejor fitness = 140
Generación 40: Mejor fitness = 156
Generación 60: Mejor fitness = 158
Generación 80: Mejor fitness = 160

``` 
## 🔬 Experimentación con Tasas de Mutación

### Resultados Comparativos

```text

Tasa de Mutación	Mejor Fitness	Eficiencia
0.05	            161	            ✅ Óptima
0.1	                160	            ✅ Muy buena
0.2	                159	            ✅ Buena
0.3	                146         	❌ Baja

```

## 📈 Análisis de Resultados

- Tasa 0.05: Mayor fitness final (161)

- Tasa 0.1: Balance ideal entre exploración y explotación

- Tasas altas (>0.2): Fitness reducido por mutación excesiva

## 🗓️ Ejemplo de Horario Optimizado

### Grupo1 (Optimizado)

```text

Lun-9:00: Arte - ProfD
Lun-11:00: Historia - ProfC
Mar-9:00: Ciencias - ProfD
Mar-11:00: Matemáticas - ProfB
Mie-9:00: Matemáticas - ProfD
Mie-11:00: Matemáticas - ProfD

```

### Características del Horario Óptimo

- ✅ Sin superposiciones de profesores

- ✅ Distribución balanceada de materias

- ✅ Preferencias respetadas en horarios

- ✅ Cobertura completa de todos los grupos

## 👥 Autores
- **Carlos Andrés Suárez Torres** → [Carlos23Andres](https://github.com/Carlos23Andres)  

- **Saira Sharid Sanabria Muñoz** → [sharito202](https://github.com/sharito202)