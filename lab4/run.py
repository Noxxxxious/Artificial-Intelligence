from matplotlib import pyplot as plt
from genetic import Genetic
from utils import generate_random_coords, plot_improvement, plot_route


def genetic(coords, generations=500, population_size=100, elite_size=10, mutation_rate=0.01):
    genetic = Genetic(coords, population_size=population_size, elite_size=elite_size, mutation_rate=mutation_rate)

    population = genetic.initial_population()
    best_solution = genetic.best_solution(population)
    steps = [best_solution]
    for i in range(generations):
        population = genetic.next_generation(population)
        best_solution = genetic.best_solution(population)
        steps.append(best_solution)

    return best_solution, steps


nb_cords = 25
cords = generate_random_coords(nb_cords)
best_solution, steps = genetic(cords)

fig, ax = plt.subplots(ncols=2, figsize=(10, 5))
plot_improvement(ax[0], cords, steps)
plot_route(ax[1], cords, best_solution)
plt.show()
