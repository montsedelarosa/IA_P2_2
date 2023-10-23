# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import random

# Configuración del algoritmo genético
population_size = 50
chromosome_length = 20
mutation_rate = 0.01
generations = 100

# Función de aptitud (fitness function)
def fitness(chromosome, target):
    return sum(1 for a, b in zip(chromosome, target) if a == b)

# Genera una población inicial aleatoria
def initialize_population(population_size, chromosome_length):
    return [''.join(random.choice('01') for _ in range(chromosome_length)) for _ in range(population_size)]

# Selecciona individuos para reproducción basados en su aptitud
def select_parents(population, target):
    return sorted(population, key=lambda x: -fitness(x, target))[:2]

# Cruza dos padres para generar un hijo
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

# Aplica una mutación con cierta probabilidad
def mutate(chromosome, mutation_rate):
    mutated_chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            mutated_chromosome[i] = '0' if chromosome[i] == '1' else '1'
    return ''.join(mutated_chromosome)

# Algoritmo genético principal
def genetic_algorithm(target, population_size, chromosome_length, mutation_rate, generations):
    population = initialize_population(population_size, chromosome_length)
    for generation in range(generations):
        parents = select_parents(population, target)
        child = crossover(parents[0], parents[1])
        child = mutate(child, mutation_rate)
        population.append(child)
        population = sorted(population, key=lambda x: -fitness(x, target))[:population_size]
        best_fit = fitness(population[0], target)
        print(f"Generación {generation + 1}: Mejor aptitud = {best_fit}, Mejor individuo = {population[0]}")

    return population[0]

if __name__ == "__main__":
    target_pattern = "11001010111011011001"
    best_solution = genetic_algorithm(target_pattern, population_size, chromosome_length, mutation_rate, generations)
    print(f"Mejor solución encontrada: {best_solution}")
