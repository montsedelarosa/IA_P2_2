# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import random

def tabu_search(problem, max_iterations, tabu_list_size):
    current_solution = problem.initial_solution()
    best_solution = current_solution
    tabu_list = []

    for _ in range(max_iterations):
        neighbors = problem.get_neighbors(current_solution)
        neighbors = [neighbor for neighbor in neighbors if neighbor not in tabu_list]

        if not neighbors:
            break

        neighbor = max(neighbors, key=lambda x: problem.get_value(x))

        tabu_list.append(neighbor)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

        if problem.get_value(neighbor) > problem.get_value(best_solution):
            best_solution = neighbor

        current_solution = neighbor

    return best_solution

class OptimizationProblem:
    def initial_solution(self):
        return [1, 2, 3]  # Ejemplo de solución inicial

    def get_neighbors(self, solution):
        # Genera vecinos de manera aleatoria para ilustrar el concepto.
        neighbors = [solution[:] for _ in range(5)]
        for neighbor in neighbors:
            index = random.randint(0, len(neighbor) - 1)
            neighbor[index] += random.uniform(-0.1, 0.1)
        return neighbors

    def get_value(self, solution):
        # Esta es una función de ejemplo que se podría optimizar.
        # Debes reemplazarla por tu propia función de evaluación.
        return -sum((x - 3) ** 2 for x in solution)

# Ejemplo de uso
if __name__ == "__main__":
    problem = OptimizationProblem()

    max_iterations = 100
    tabu_list_size = 10
    final_solution = tabu_search(problem, max_iterations, tabu_list_size)

    print("Solución final:", final_solution)
