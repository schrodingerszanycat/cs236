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

    # Other methods remain the same...

    def run(self):
        best_fitness_history = []  # Track best fitness values over generations
        unchanged_generations = 0  # Track consecutive generations with no improvement

        for generation in range(self.max_generations):
            self.generate_successors()
            best_fitness = min(self.evaluate_pop())
            best_fitness_history.append(best_fitness)

            # Check for convergence
            if len(best_fitness_history) > self.convergence_threshold:
                if len(set(best_fitness_history[-self.convergence_threshold:])) == 1:
                    unchanged_generations += 1
                else:
                    unchanged_generations = 0

                if unchanged_generations >= self.convergence_threshold:
                    print(f"Population converged after {generation+1} generations.")
                    break

            # Print progress every 100 generations
            if (generation + 1) % 100 == 0:
                print(f"Generation {generation+1}/{self.max_generations}, Best Fitness: {best_fitness}")

        best_individual = self.population[np.argmin(self.evaluate_pop())]
        return self.binary_to_decimal(best_individual)
