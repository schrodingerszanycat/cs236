import random
import numpy as np

def f(x):
    return x**2 - 4*x + 4

def hill_climbing(initial_solution, step_size, max_iterations):
    current_solution = initial_solution
    current_value = f(current_solution)
    
    for _ in range(max_iterations):
        next_solution = current_solution + random.uniform(-step_size, step_size)
        next_value = f(next_solution)
        
        if next_value < current_value:
            current_solution = next_solution
            current_value = next_value
            
    return current_solution

def create_population(population_size):
    return [np.random.randint(0, 2, 10) for _ in range(population_size)]

def decode_individual(individual):
    x = int("".join(str(bit) for bit in individual), 2)
    return x / 1023 * 20 - 10

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(population_size, mutation_rate, max_generations):
    population = create_population(population_size)
    
    for _ in range(max_generations):
        fitness_values = [f(decode_individual(individual)) for individual in population]
        
        if min(fitness_values) == 0:
            break
        
        sorted_population = [x for _, x in sorted(zip(fitness_values, population))]
        
        selected_parents = sorted_population[:2]
        offspring = crossover(*selected_parents)
        offspring = [mutate(child, mutation_rate) for child in offspring]
        
        population = sorted_population[:-2] + offspring
        
    best_individual = min(population, key=lambda x: f(decode_individual(x)))
    return decode_individual(best_individual)

initial_solution = random.uniform(-10, 10)
step_size = 0.1
max_iterations = 1000

population_size = 20
mutation_rate = 0.01
max_generations = 100

hill_climbing_solution = hill_climbing(initial_solution, step_size, max_iterations)

genetic_algorithm_solution = genetic_algorithm(population_size, mutation_rate, max_generations)

print("Hill Climbing Solution:", hill_climbing_solution)
print("Genetic Algorithm Solution:", genetic_algorithm_solution)
