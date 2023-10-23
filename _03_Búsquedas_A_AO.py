# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import heapq

def a_star_search(graph, start, goal, heuristic):
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        _, current_node = heapq.heappop(open_set)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        for neighbor, cost in graph[current_node]:
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None

def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.append(current_node)
    path.reverse()
    return path

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un grafo de ejemplo donde cada arista tiene un costo
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('D', 2), ('E', 4)],
        'C': [('A', 3), ('F', 2)],
        'D': [('B', 2)],
        'E': [('B', 4), ('F', 1)],
        'F': [('C', 2), ('E', 1), ('G', 3)],
        'G': [('F', 3)]
    }

    start_node = 'A'
    goal_node = 'G'

    # Definimos una heurística simple basada en la distancia en línea recta
    heuristic = {
        'A': 7,
        'B': 6,
        'C': 5,
        'D': 2,
        'E': 4,
        'F': 2,
        'G': 0
    }

    path = a_star_search(graph, start_node, goal_node, heuristic)

    if path:
        print(f"Camino de {start_node} a {goal_node} usando A*: {path}")
    else:
        print(f"No se encontró un camino de {start_node} a {goal_node} usando A*.")
