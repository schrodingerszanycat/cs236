import numpy as np

def objective_function(x):
    return x**2 - 4*x + 4

def binary_to_decimal(binary):
    decimal = 0
    for bit in binary:
        decimal = decimal*2 + bit
    return decimal

def initialize_population(population_size, chromosome_length):
    return np.random.randint(2, size=(population_size, chromosome_length))

def selection(population, fitness):
    fitness = np.array(fitness)
    idx = np.random.choice(np.arange(len(population)), size=len(population), replace=True, p=fitness/fitness.sum())
    return population[idx]

def crossover(parent1, parent2, crossover_rate):
    if np.random.rand() < crossover_rate:
        crossover_point = np.random.randint(len(parent1))
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2
    else:
        return parent1, parent2

def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if np.random.rand() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(population_size, chromosome_length, crossover_rate, mutation_rate, generations):
    population = initialize_population(population_size, chromosome_length)
    convergence_criteria = 1e-6
    best_fitness = float('inf')
    best_individual = None
    for generation in range(generations):
        fitness_values = [objective_function(binary_to_decimal(individual)) for individual in population]
        avg_fitness = np.mean(fitness_values)
        if abs(avg_fitness - best_fitness) < convergence_criteria:
            break
        selected_population = selection(population, fitness_values)
        new_population = []
        for i in range(0, len(selected_population), 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i+1]
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = np.array(new_population)
        best_index = np.argmin(fitness_values)
        if fitness_values[best_index] < best_fitness:
            best_fitness = fitness_values[best_index]
            best_individual = population[best_index]
    best_solution = binary_to_decimal(best_individual)
    return best_solution

population_size = 20
chromosome_length = 10 
crossover_rate = 0.8
mutation_rate = 0.01
generations = 1000

solution = genetic_algorithm(population_size, chromosome_length, crossover_rate, mutation_rate, generations)
print("Best solution:", solution)
print("Minimum value of f(x):", objective_function(solution))
