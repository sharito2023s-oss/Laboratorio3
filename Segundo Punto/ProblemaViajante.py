# segundo_punto_tsp.py
import numpy as np
import matplotlib.pyplot as plt
import random

class TSPGeneticAlgorithm:
    def __init__(self, num_cities=10, population_size=100, mutation_rate=0.01, generations=100):
        self.num_cities = num_cities
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.cities = self.generate_cities(num_cities)
        
    def generate_cities(self, n):
        """Genera n ciudades con coordenadas aleatorias entre 0 y 1"""
        return [(random.random(), random.random()) for _ in range(n)]
    
    def distance(self, city1, city2):
        """Calcula la distancia euclidiana entre dos ciudades"""
        return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
    
    def total_distance(self, route):
        """Calcula la distancia total de una ruta"""
        total = 0
        for i in range(len(route)):
            total += self.distance(self.cities[route[i]], self.cities[route[(i + 1) % len(route)]])
        return total
    
    def fitness(self, route):
        """Función de fitness (inversa de la distancia)"""
        return 1 / self.total_distance(route)
    
    def create_individual(self):
        """Crea un individuo (ruta) aleatorio"""
        individual = list(range(self.num_cities))
        random.shuffle(individual)
        return individual
    
    def create_population(self):
        """Crea la población inicial"""
        return [self.create_individual() for _ in range(self.population_size)]
    
    def selection(self, population, fitnesses):
        """Selección por torneo"""
        tournament_size = 3
        selected = []
        
        for _ in range(len(population)):
            tournament = random.sample(list(zip(population, fitnesses)), tournament_size)
            winner = max(tournament, key=lambda x: x[1])[0]
            selected.append(winner)
        
        return selected
    
    def ordered_crossover(self, parent1, parent2):
        """Cruce ordenado (OX)"""
        size = len(parent1)
        child = [-1] * size
        
        # Seleccionar dos puntos de corte
        start, end = sorted(random.sample(range(size), 2))
        
        # Copiar segmento del padre 1 al hijo
        child[start:end] = parent1[start:end]
        
        # Completar con los elementos del padre 2 en orden
        pointer = end
        for gene in parent2[end:] + parent2[:end]:
            if gene not in child:
                if pointer >= size:
                    pointer = 0
                child[pointer] = gene
                pointer += 1
        
        return child
    
    def swap_mutation(self, route):
        """Mutación por intercambio"""
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(len(route)), 2)
            route[i], route[j] = route[j], route[i]
        return route
    
    def evolve(self):
        """Ejecuta el algoritmo genético"""
        population = self.create_population()
        best_fitness_history = []
        avg_fitness_history = []
        
        print("Iniciando algoritmo genético para TSP...")
        print(f"Ciudades: {self.num_cities}, Población: {self.population_size}")
        print(f"Generaciones: {self.generations}, Mutación: {self.mutation_rate}")
        
        for generation in range(self.generations):
            # Calcular fitness
            fitnesses = [self.fitness(individual) for individual in population]
            
            # Guardar estadísticas
            best_fitness = max(fitnesses)
            avg_fitness = np.mean(fitnesses)
            best_fitness_history.append(best_fitness)
            avg_fitness_history.append(avg_fitness)
            
            # Selección
            selected = self.selection(population, fitnesses)
            
            # Cruzamiento
            next_generation = []
            for i in range(0, len(selected), 2):
                if i + 1 < len(selected):
                    parent1, parent2 = selected[i], selected[i + 1]
                    child1 = self.ordered_crossover(parent1, parent2)
                    child2 = self.ordered_crossover(parent2, parent1)
                    next_generation.extend([child1, child2])
                else:
                    next_generation.append(selected[i])
            
            # Mutación
            population = [self.swap_mutation(individual) for individual in next_generation]
            
            # Elitismo: mantener el mejor individuo
            best_individual = population[np.argmax(fitnesses)]
            population[0] = best_individual
            
            if generation % 20 == 0:
                best_distance = 1 / best_fitness
                print(f"Generación {generation}: Mejor distancia = {best_distance:.4f}")
        
        # Encontrar la mejor solución final
        fitnesses = [self.fitness(individual) for individual in population]
        best_individual = population[np.argmax(fitnesses)]
        best_distance = 1 / max(fitnesses)
        
        return best_individual, best_distance, best_fitness_history, avg_fitness_history
    
    def plot_route(self, route, title="Mejor Ruta TSP"):
        """Visualiza la mejor ruta encontrada"""
        x = [self.cities[i][0] for i in route] + [self.cities[route[0]][0]]
        y = [self.cities[i][1] for i in route] + [self.cities[route[0]][1]]
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'o-', markersize=8, linewidth=2, alpha=0.7)
        plt.scatter(x, y, s=100, c='red', alpha=0.7)
        
        # Etiquetar ciudades
        for i, (city_x, city_y) in enumerate(self.cities):
            plt.annotate(str(i), (city_x, city_y), xytext=(5, 5), textcoords='offset points',
                        fontweight='bold')
        
        plt.title(f"{title}\nDistancia total: {self.total_distance(route):.4f}")
        plt.xlabel('Coordenada X')
        plt.ylabel('Coordenada Y')
        plt.grid(True, alpha=0.3)
        plt.show()
    
    def plot_convergence(self, best_history, avg_history):
        """Grafica la convergencia del algoritmo"""
        plt.figure(figsize=(10, 5))
        plt.plot(best_history, 'r-', linewidth=2, label='Mejor Fitness')
        plt.plot(avg_history, 'b-', alpha=0.7, label='Fitness Promedio')
        plt.xlabel('Generación')
        plt.ylabel('Fitness')
        plt.title('Convergencia del Algoritmo Genético - TSP')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

def experimentar_tasas_mutacion():
    """Experimenta con diferentes tasas de mutación"""
    tasas_mutacion = [0.01, 0.05, 0.1, 0.2]
    resultados = []
    
    for tasa in tasas_mutacion:
        print(f"\n--- Experimentando con tasa de mutación: {tasa} ---")
        tsp = TSPGeneticAlgorithm(mutation_rate=tasa, generations=50)
        best_route, best_distance, best_history, avg_history = tsp.evolve()
        resultados.append((tasa, best_distance, best_history[-1]))
        
        print(f"Tasa: {tasa}, Mejor distancia: {best_distance:.4f}")
    
    # Mostrar comparación
    print("\n=== COMPARACIÓN DE TASAS DE MUTACIÓN ===")
    for tasa, distancia, fitness in resultados:
        print(f"Tasa {tasa}: Distancia = {distancia:.4f}, Fitness = {fitness:.4f}")

if __name__ == "__main__":
    # Ejecución principal del TSP
    print("=== PROBLEMA DEL VIAJANTE (TSP) ===")
    
    # Configurar y ejecutar algoritmo genético
    tsp = TSPGeneticAlgorithm(num_cities=10, generations=100, mutation_rate=0.02)
    
    print("Ciudades generadas:")
    for i, city in enumerate(tsp.cities):
        print(f"  Ciudad {i}: ({city[0]:.3f}, {city[1]:.3f})")
    
    # Ejecutar algoritmo genético
    best_route, best_distance, best_history, avg_history = tsp.evolve()
    
    print(f"\n=== RESULTADOS FINALES ===")
    print(f"Mejor ruta encontrada: {best_route}")
    print(f"Distancia total: {best_distance:.4f}")
    
    # Visualizar resultados
    tsp.plot_convergence(best_history, avg_history)
    tsp.plot_route(best_route)
    
    # Experimentar con diferentes tasas de mutación
    print("\n=== EXPERIMENTACIÓN CON TASAS DE MUTACIÓN ===")
    experimentar_tasas_mutacion()