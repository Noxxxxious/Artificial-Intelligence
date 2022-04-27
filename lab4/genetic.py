import numpy as np
from utils import fitness
import random


class Genetic:
    def __init__(self, coords, population_size=100, elite_size=10, mutation_rate=0.01):
        self.coords = coords
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate

    def population_fitness(self, population):
        population_fitness = {}
        for i, individual in enumerate(population):
            # 1/fitness -> change to maximization problem
            population_fitness[i] = 1/fitness(self.coords, individual)

        return {k: v for k, v in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True)}

    def best_solution(self, population):
        population_fitness = list(self.population_fitness(population))
        best_ind = population_fitness[0]
        return population[best_ind]

    def initial_population(self):
        population = []
        # Create initial population
        for i in range(self.population_size):
            solution = np.random.permutation(len(self.coords))
            population.append(solution)
        return population

    def selection(self, population):
        selection = []
        population_fit = self.population_fitness(population)
        probability = {}
        selection = []

        sum_fitness = 0.0
        for val in population_fit.values():
            sum_fitness += val
        previous_probability = 0.0

        for key, value in zip(population_fit.keys(), population_fit.values()):
            probability[key] = previous_probability + value/sum_fitness
            previous_probability = probability[key]
        for i in range(len(population)):
            rand = random.random()
            for key, value in probability.items():
                if rand <= value or i < 10:
                    selection.append(population[key])
                    break

        return selection

    def crossover_population(self, population):
        offspring = []
        for i in range(100):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            slice = parent1[random.randrange(len(parent1)):random.randrange(len(parent1))]
            new_coords = np.array([x for x in parent2 if x not in slice])
            offspring.append(parent1)
            final = np.append(new_coords, slice)
            offspring.append(final)
        return offspring

    def mutate_population(self, population):
        i = 0
        for p in population:
            if i > 5:
                rand = random.random()
                if rand <= self.mutation_rate:
                    rand1 = random.randrange(0, len(p))
                    rand2 = random.randrange(0, len(p))
                    p[[rand1, rand2]] = p[[rand2, rand1]]
        return population

    def next_generation(self, population):
        selection = self.selection(population)
        children = self.crossover_population(selection)
        next_generation = self.mutate_population(children)
        return next_generation
