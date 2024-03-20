import numpy as np
import sys
import random

class Genetic(object):
    def __init__(self, f, pop_size=20, n_variables=10, mutation_rate=0.1, max_generations=1000, convergence_threshold=10):
        self.f = f
        self.pop_size = pop_size
        self.n_variables = n_variables
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.convergence_threshold = convergence_threshold
        self.population = self.initialize_pop()
        self.evaluate_pop()

    def initialize_pop(self):
        return [np.random.randint(2, size=self.n_variables) for _ in range(self.pop_size)]

    def evaluate_pop(self):
        return [self.f(self.binary_to_decimal(individual)) for individual in self.population]

    def crossover(self, parent1, parent2):
        crossover_point = np.random.randint(1, self.n_variables)
        child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
        return child1, child2

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    def generate_successors(self):
        results = self.evaluate_pop()
        successors = []

        while len(successors) < self.pop_size:
            # Tournament selection
            idx1, idx2 = np.random.choice(range(self.pop_size), size=2, replace=False)
            parent1, parent2 = self.population[idx1], self.population[idx2]
            # Crossover
            child1, child2 = self.crossover(parent1, parent2)
            # Mutation
            child1 = self.mutate(child1)
            child2 = self.mutate(child2)
            
            successors.append(child1)
            successors.append(child2)

        self.population = successors
    
    def binary_to_decimal(self, binary):
        decimal = 0
        for i in range(len(binary)):
            decimal += binary[i] * 2**i
        return decimal

    def run(self):
        best_fitness_history = [] 
        unchanged_generations = 0  

        for generation in range(self.max_generations):
            self.generate_successors()
            best_fitness = min(self.evaluate_pop())
            best_fitness_history.append(best_fitness)

            if len(best_fitness_history) > self.convergence_threshold:
                if len(set(best_fitness_history[-self.convergence_threshold:])) == 1:
                    unchanged_generations += 1
                else:
                    unchanged_generations = 0

                if unchanged_generations >= self.convergence_threshold:
                    print(f"Population converged after {generation+1} generations.")
                    break

        best_individual = self.population[np.argmin(self.evaluate_pop())]
        return self.binary_to_decimal(best_individual)
            
def hill_climbing(f, lower, upper, step_size):
    if upper < lower:
        return None
    current = lower
    f_min = sys.maxsize
    while current < upper:
        neighbor = current + step_size
        if f(neighbor) < f(current):
            f_min = min(f_min, f(neighbor))
        else:
            break  
        current = neighbor
    return f_min, current

def main():
    f_order = int(input("Enter the order of f(x): "))
    coeffs = []
    for i in range(f_order + 1):
        ele = float(input("Enter coefficients in ascending order: "))
        coeffs.append(ele)
    f = np.poly1d(coeffs)
    print("f(x) =", f)
    l = float(input("Lower bound: "))
    u = float(input("Upper bound: "))
    step = float(input("Step size: "))
    val, x_val = hill_climbing(f, l, u, step)
    print("Using Hill Climbing: ")
    print("Minimum value found f=:", val)
    #print("At", x_val)

    f2 = lambda x: x**2 - 4 * x + 4
    gen = Genetic(f2)
    minim = gen.run()
    print("Using Genetic Algorithm: ")
    print('Minimum value found f=: ', minim)

if __name__ == "__main__":
    main()
































