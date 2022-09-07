import numpy as np
from gcp import random_connected_graph, violation_point, plot_graph
import matplotlib.pyplot as plt


def initialize(n_pop, n_node):
    X = []
    for _ in range(n_pop):
        X.append(np.random.randint(3, size=n_node))
    return X


def fitness(x, A):
    f = violation_point(x, A)
    n = np.sum(A)//2
    return 1 - f/n


def fitness_computation(X, A):
    return [fitness(x, A) for x in X]


def elite_preservation(X, F, n_elite):
    E = []
    elite_id = sorted(range(len(F)),
                      key=lambda k: F[k],
                      reverse=True)[:n_elite]
    for i in elite_id:
        E.append(X[i])
    return E


def parent_selection(X, F, n_parent):
    X_ = []
    p = [f/sum(F) for f in F]
    ids = np.random.choice(len(X), size=n_parent, p=p)
    for i in ids:
        X_.append(X[i])
    return X_


def crossover(x1, x2):
    crossover_point = np.random.randint(len(x1))
    c1 = np.hstack([x2[:crossover_point],x1[crossover_point:]])
    c2 = np.hstack([x1[:crossover_point],x2[crossover_point:]])
    return c1, c2


def mutation(x):
    mutation_point = np.random.randint(len(x1))
    if np.random.random() <= 0.5:
        x[mutation_point] += 1
    else:
        x[mutation_point] -= 1
    x[mutation_point] %= 3
    return x


np.random.seed(318)

n_node = 15
n_edge = 37
A = random_connected_graph(n_node, n_edge)

n_pop = 50
n_gen = 1000
n_elite = 4
p_cx = 0.9
p_mut = 0.1

history = []

population = initialize(n_pop, n_node)

for g in range(n_gen):
    fitnesses = fitness_computation(population, A)

    best_id = np.argmax(fitnesses)
    best_fitness = fitnesses[best_id]
    best_individual = population[best_id]
    history.append(best_fitness)
    if best_fitness == 1:
        break

    elites = elite_preservation(population, fitnesses, n_elite)
    parents = parent_selection(population, fitnesses, n_pop-n_elite)
    offspring = elites

    for x1, x2 in zip(parents[::2], parents[1::2]):

        if np.random.random() <= p_cx:
            c1, c2 = crossover(x1, x2)
        else:
            c1, c2 = x1, x2

        if np.random.random() <= p_mut:
            c1 = mutation(c1)
        if np.random.random() <= p_mut:
            c2 = mutation(c2)

        offspring.extend([c1, c2])

    population = offspring

print(g)
print(best_individual)
print(best_fitness)

plot_graph(A, best_individual)

plt.plot(history)
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
