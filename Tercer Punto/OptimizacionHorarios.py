# tercer_punto_horarios.py
import random
import numpy as np
import matplotlib.pyplot as plt

class ScheduleOptimizer:
    def __init__(self):
        self.teachers = ["ProfA", "ProfB", "ProfC", "ProfD"]
        self.subjects = ["Matemáticas", "Ciencias", "Historia", "Arte"]
        self.groups = ["Grupo1", "Grupo2", "Grupo3"]
        self.time_slots = ["Lun-9:00", "Lun-11:00", "Mar-9:00", "Mar-11:00", 
                          "Mie-9:00", "Mie-11:00"]
        
        # Preferencias de profesores (profesor: [horarios preferidos])
        self.teacher_preferences = {
            "ProfA": ["Lun-9:00", "Mar-9:00"],
            "ProfB": ["Mar-11:00", "Mie-11:00"],
            "ProfC": ["Lun-11:00", "Mie-9:00"],
            "ProfD": ["Mar-9:00", "Mie-11:00"]
        }
        
        # Materias preferidas en ciertos horarios
        self.subject_preferences = {
            "Matemáticas": ["Lun-9:00", "Mar-9:00"],
            "Ciencias": ["Mar-11:00", "Mie-11:00"],
            "Historia": ["Lun-11:00"],
            "Arte": ["Mie-9:00"]
        }
    
    def create_schedule(self):
        """Crea un horario aleatorio"""
        schedule = []
        for time in self.time_slots:
            for group in self.groups:
                teacher = random.choice(self.teachers)
                subject = random.choice(self.subjects)
                schedule.append((time, group, teacher, subject))
        return schedule
    
    def evaluate_schedule(self, schedule):
        """Evalúa el horario basado en restricciones"""
        score = 100  # Puntuación inicial
        
        # Restricción 1: No superposición de profesores en mismo horario
        teacher_time_conflicts = 0
        for time in self.time_slots:
            teachers_in_time = [entry[2] for entry in schedule if entry[0] == time]
            if len(teachers_in_time) != len(set(teachers_in_time)):
                teacher_time_conflicts += 1
        
        score -= teacher_time_conflicts * 20
        
        # Restricción 2: No superposición de grupos en mismo horario
        group_time_conflicts = 0
        for time in self.time_slots:
            groups_in_time = [entry[1] for entry in schedule if entry[0] == time]
            if len(groups_in_time) != len(set(groups_in_time)):
                group_time_conflicts += 1
        
        score -= group_time_conflicts * 30
        
        # Restricción 3: Preferencias de horarios para profesores
        preference_score = 0
        for entry in schedule:
            time, teacher, subject = entry[0], entry[2], entry[3]
            if time in self.teacher_preferences.get(teacher, []):
                preference_score += 5
            if time in self.subject_preferences.get(subject, []):
                preference_score += 3
        
        score += preference_score
        
        # Restricción 4: Distribución balanceada de materias por grupo
        for group in self.groups:
            group_classes = [entry for entry in schedule if entry[1] == group]
            subject_count = {}
            for entry in group_classes:
                subject_count[entry[3]] = subject_count.get(entry[3], 0) + 1
            
            # Penalizar si hay mucha variación en la distribución
            if subject_count:
                max_count = max(subject_count.values())
                min_count = min(subject_count.values())
                score -= (max_count - min_count) * 2
        
        return max(score, 0)  # No permitir puntuaciones negativas
    
    def genetic_algorithm(self, population_size=50, generations=100, mutation_rate=0.1):
        """Algoritmo genético para optimizar horarios"""
        population = [self.create_schedule() for _ in range(population_size)]
        best_fitness_history = []
        avg_fitness_history = []
        
        print("Iniciando algoritmo genético para optimización de horarios...")
        print(f"Población: {population_size}, Generaciones: {generations}")
        print(f"Tasa de mutación: {mutation_rate}")
        
        for generation in range(generations):
            # Evaluar fitness
            fitness_scores = [self.evaluate_schedule(schedule) for schedule in population]
            
            # Guardar estadísticas
            best_fitness = max(fitness_scores)
            avg_fitness = np.mean(fitness_scores)
            best_fitness_history.append(best_fitness)
            avg_fitness_history.append(avg_fitness)
            
            # Selección por ruleta
            selected = []
            total_fitness = sum(fitness_scores)
            if total_fitness > 0:
                probabilities = [f/total_fitness for f in fitness_scores]
                selected = random.choices(population, weights=probabilities, k=population_size)
            else:
                selected = population.copy()
            
            # Cruzamiento (cruce de un punto)
            next_generation = []
            for i in range(0, population_size, 2):
                if i + 1 < population_size:
                    parent1, parent2 = selected[i], selected[i+1]
                    crossover_point = random.randint(1, len(parent1)-1)
                    child1 = parent1[:crossover_point] + parent2[crossover_point:]
                    child2 = parent2[:crossover_point] + parent1[crossover_point:]
                    next_generation.extend([child1, child2])
                else:
                    next_generation.append(selected[i])
            
            # Mutación
            for i in range(len(next_generation)):
                if random.random() < mutation_rate:
                    # Mutar cambiando profesor y materia de una clase aleatoria
                    idx = random.randint(0, len(next_generation[i])-1)
                    time, group, _, _ = next_generation[i][idx]
                    new_teacher = random.choice(self.teachers)
                    new_subject = random.choice(self.subjects)
                    next_generation[i][idx] = (time, group, new_teacher, new_subject)
            
            population = next_generation
            
            # Elitismo: mantener el mejor individuo
            best_schedule = population[np.argmax(fitness_scores)]
            population[0] = best_schedule
            
            if generation % 20 == 0:
                print(f"Generación {generation}: Mejor fitness = {best_fitness}")
        
        # Encontrar el mejor horario
        fitness_scores = [self.evaluate_schedule(schedule) for schedule in population]
        best_schedule = population[np.argmax(fitness_scores)]
        best_fitness = max(fitness_scores)
        
        return best_schedule, best_fitness, best_fitness_history, avg_fitness_history
    
    def print_schedule(self, schedule, title="Horario Optimizado"):
        """Imprime el horario de forma organizada"""
        print(f"\n{title}")
        print("=" * 60)
        
        for group in self.groups:
            print(f"\n{group}:")
            print("-" * 40)
            group_classes = [entry for entry in schedule if entry[1] == group]
            group_classes.sort(key=lambda x: self.time_slots.index(x[0]))
            
            for time in self.time_slots:
                classes_at_time = [entry for entry in group_classes if entry[0] == time]
                if classes_at_time:
                    for class_entry in classes_at_time:
                        print(f"  {time}: {class_entry[3]} - {class_entry[2]}")
                else:
                    print(f"  {time}: Libre")
    
    def plot_convergence(self, best_history, avg_history):
        """Grafica la convergencia del algoritmo"""
        plt.figure(figsize=(10, 5))
        plt.plot(best_history, 'g-', linewidth=2, label='Mejor Fitness')
        plt.plot(avg_history, 'b-', alpha=0.7, label='Fitness Promedio')
        plt.xlabel('Generación')
        plt.ylabel('Fitness')
        plt.title('Convergencia del Algoritmo Genético - Horarios')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

def experimentar_tasas_mutacion_horarios():
    """Experimenta con diferentes tasas de mutación para horarios"""
    tasas_mutacion = [0.05, 0.1, 0.2, 0.3]
    resultados = []
    
    optimizer = ScheduleOptimizer()
    
    for tasa in tasas_mutacion:
        print(f"\n--- Experimentando con tasa de mutación: {tasa} ---")
        best_schedule, best_fitness, best_history, avg_history = optimizer.genetic_algorithm(
            generations=50, mutation_rate=tasa
        )
        resultados.append((tasa, best_fitness))
        
        print(f"Tasa: {tasa}, Mejor fitness: {best_fitness}")
    
    # Mostrar comparación
    print("\n=== COMPARACIÓN DE TASAS DE MUTACIÓN ===")
    for tasa, fitness in resultados:
        print(f"Tasa {tasa}: Fitness = {fitness}")

if __name__ == "__main__":
    print("=== OPTIMIZACIÓN DE HORARIOS ESCOLARES ===")
    
    optimizer = ScheduleOptimizer()
    
    # Horario inicial aleatorio
    print("\nGenerando horario inicial aleatorio...")
    initial_schedule = optimizer.create_schedule()
    initial_fitness = optimizer.evaluate_schedule(initial_schedule)
    print(f"Fitness del horario inicial: {initial_fitness}")
    
    # Optimizar con algoritmo genético
    print("\nOptimizando horario con algoritmo genético...")
    best_schedule, best_fitness, best_history, avg_history = optimizer.genetic_algorithm(
        generations=100, mutation_rate=0.1
    )
    
    print(f"\n=== RESULTADOS FINALES ===")
    print(f"Fitness del horario optimizado: {best_fitness}")
    print(f"Mejora: {best_fitness - initial_fitness} puntos")
    
    # Mostrar horarios
    optimizer.print_schedule(initial_schedule, "Horario Inicial (Aleatorio)")
    optimizer.print_schedule(best_schedule, "Horario Optimizado")
    
    # Graficar convergencia
    optimizer.plot_convergence(best_history, avg_history)
    
    # Experimentar con diferentes tasas de mutación
    print("\n=== EXPERIMENTACIÓN CON TASAS DE MUTACIÓN ===")
    experimentar_tasas_mutacion_horarios()