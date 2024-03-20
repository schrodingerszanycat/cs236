import numpy as np
import sys
import random

class Genetic(object):
    def __init__(self, f, pop_size=20, n_variables=10, mutation_rate=0.1):
        self.f = f
        self.pop_size = pop_size
        self.n_variables = n_variables
        self.mutation_rate = mutation_rate
        self.population = self.initializePopulation()
        self.evaluatePopulation()

    def initializePopulation(self):
        return [np.random.randint(2, size=self.n_variables) for _ in range(self.pop_size)]

    def binaryToDecimal(self, binary):
        decimal = 0
        for i in range(len(binary)):
            decimal += binary[i] * 2**i
        return decimal

    def evaluatePopulation(self):
        return [self.f(self.binaryToDecimal(individual)) for individual in self.population]

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

    def nextGen(self):
        results = self.evaluatePopulation()
        children = []

        while len(children) < self.pop_size:
            # Tournament selection
            idx1, idx2 = np.random.choice(range(self.pop_size), size=2, replace=False)
            parent1, parent2 = self.population[idx1], self.population[idx2]

            # Crossover
            child1, child2 = self.crossover(parent1, parent2)

            # Mutation
            child1 = self.mutate(child1)
            child2 = self.mutate(child2)

            children.append(child1)
            children.append(child2)

        self.population = children

    def run(self, generations=100):
        for _ in range(generations):
            self.nextGen()
        best_individual = self.population[np.argmin(self.evaluatePopulation())]
        return self.binaryToDecimal(best_individual)

f = lambda x: x**2 - 4 * x + 4

gen = Genetic(f)
minim = gen.run()
print('Minimum found x =', minim)
