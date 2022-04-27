import numpy as np


def plot_route(ax, cords, solution):
    solution_cords = [cords[i] for i in solution]
    x, y = zip(*solution_cords)

    # Draw the primary path for the TSP problem
    for i in range(-1, len(x) - 1):
        ax.plot((x[i], x[i+1]), (y[i], y[i+1]), marker='o', color='g')

    # Set axis too slightly larger than the set of x and y
    ax.set_xlim(min(x)*1.1, max(x)*1.1)
    ax.set_ylim(min(y)*1.1, max(y)*1.1)


def plot_improvement(ax, coords, steps):

    progress = []
    for solution in steps:
        progress.append(fitness(coords, solution))
    ax.plot(progress)

    ax.set_ylabel('Distance')
    ax.set_xlabel('Iteration step')


def generate_random_coords(nb_cords):
    cords = []
    for i in range(nb_cords):
        x = np.random.random() * 1000
        y = np.random.random() * 1000
        cords.append((x, y))

    return cords


def dist(n0, n1):
    return np.sqrt((n0[0] - n1[0]) ** 2 + (n0[1] - n1[1]) ** 2)


def fitness(cords, solution):
    nb_cords = len(cords)
    assert sorted(solution) == list(range(nb_cords))

    fit = 0
    for i in range(nb_cords):
        n0 = cords[solution[i % nb_cords]]
        n1 = cords[solution[(i + 1) % nb_cords]]
        fit += dist(n0, n1)
    return fit
