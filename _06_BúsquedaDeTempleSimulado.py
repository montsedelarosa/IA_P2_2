# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import random
import math

def simulated_annealing(problem, initial_temperature, cooling_rate, max_iterations):
    current_solution = problem.initial_solution()
    current_cost = problem.get_value(current_solution)
    best_solution = current_solution
    best_cost = current_cost
    temperature = initial_temperature

    for iteration in range(max_iterations):
        neighbor_solution = problem.get_neighbor(current_solution)
        neighbor_cost = problem.get_value(neighbor_solution)

        if neighbor_cost > current_cost:
            current_solution = neighbor_solution
            current_cost = neighbor_cost
        else:
            delta = neighbor_cost - current_cost
            probability = math.exp(delta / temperature)

            if random.random() < probability:
                current_solution = neighbor_solution
                current_cost = neighbor_cost

        if current_cost > best_cost:
            best_solution = current_solution
            best_cost = current_cost

        temperature *= cooling_rate

    return best_solution

class OptimizationProblem:
    def initial_solution(self):
        return [1, 2, 3]  # Ejemplo de solución inicial

    def get_neighbor(self, solution):
        # Genera un vecino de manera aleatoria para ilustrar el concepto.
        neighbor = solution[:]
        index = random.randint(0, len(neighbor) - 1)
        neighbor[index] += random.uniform(-0.1, 0.1)
        return neighbor

    def get_value(self, solution):
        # Esta es una función de ejemplo que se podría optimizar.
        # Debes reemplazarla por tu propia función de evaluación.
        return -sum((x - 3) ** 2 for x in solution)

# Ejemplo de uso
if __name__ == "__main__":
    problem = OptimizationProblem()

    initial_temperature = 100.0
    cooling_rate = 0.95
    max_iterations = 1000

    final_solution = simulated_annealing(problem, initial_temperature, cooling_rate, max_iterations)

    print("Solución final:", final_solution)
