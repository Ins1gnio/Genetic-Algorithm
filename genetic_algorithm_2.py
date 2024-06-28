"""
Genetic Algorithm (GA) code written in python, created for "Fundamental of Intelligent System" Class, BME.
Binary genome (1 or 0), fitness score equal to summation (minimum value)
(c) AS. - 2024
"""

import numpy as np
import random


class main_ga:
    def __init__(self):
        self.n_chromosome = 100     # define number of population   100
        self.n_gene = 8             # define number of gene in chromosome 8
        self.p_crossover = 0.7      # define probability to do crossover / mating between 2 chosen parents
        self.p_mutation = 0.01      # define probability to do mutation
        self.n_generation = 50     # define maximum generation
        self.generation = 0

        self.k = 2  # define number of genes to cross-over
        self.l = 2  # define number of genes to mutation

        # create a population (as a matrix)
        self.population = []
        self.create_population()

        for _ in range(self.n_generation):
            # calculate fitness in each chromosome
            self.fitness_score = []
            self.compute_fitness()

            # choose parents --> roulette
            self.p_chromosome, self.parents, self.child = [[] for _ in range(3)]
            self.choose_parents()

    def create_population(self):
        for _ in range(self.n_chromosome):
            self.population.append([np.random.randint(0, 2) for _ in range(self.n_gene)])   # create population
        print("gen." + str(self.generation) + " population: " + str(self.population))

    def compute_fitness(self):
        for i in range(self.n_chromosome):
            summation = sum(self.population[i])
            if summation != 0:
                self.fitness_score.append(summation)
            else:
                self.fitness_score.append(1)
        # print("fitness score: " + str(self.fitness_score))

    def choose_parents(self):
        invert = [1 / i for i in self.fitness_score]
        fitness_sum = sum(invert)
        for i in range(self.n_chromosome):
            self.p_chromosome.append(invert[i] / fitness_sum)    # define the chances
        # print("p chromosome as parent: " + str(self.p_chromosome))

        for _ in range(int(self.n_chromosome / 2)):
            self.parents = []
            [self.parents.append(random.choices(self.population, self.p_chromosome)[0]) for _ in range(2)]  # roulette based on chances for parent 1 & 2
            # print("parents :" + str(self.parents))

            # cross-over
            if np.random.random() < self.p_crossover:
                for _ in range(self.k):
                    index = np.random.randint(0, self.n_gene)
                    temp = self.parents[0][index]
                    self.parents[0][index] = self.parents[1][index]
                    self.parents[1][index] = temp
                    # print(index, self.parents)

            # mutation
            if np.random.random() < self.p_mutation:
                for _ in range(self.l):
                    index = np.random.randint(0, self.n_gene)
                    self.parents[0][index] = np.abs(self.parents[0][index] - 1)
                    self.parents[1][index] = np.abs(self.parents[1][index] - 1)

            self.child.append(self.parents[0][:])
            self.child.append(self.parents[1][:])

        self.population = self.child

        self.generation += 1
        print("gen." + str(self.generation) + " population: " + str(self.population))


if __name__ == '__main__':
    main_ga()
