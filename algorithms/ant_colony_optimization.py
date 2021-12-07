import numpy as np


def pheromone_update(pheromone_matrix, path, path_distance):
    evaporation_rate = 0.001
    q = 7
    pheromone_matrix = pheromone_matrix * (1 - evaporation_rate)
    for path_move in path:
        pheromone_matrix[path_move] += q/path_distance
    return pheromone_matrix


def node_selection(matrix_row, pheromone_matrix_row, visibility_matrix_row, nodes_visited):
    nodes = np.arange(0, len(matrix_row))
    a = 1  # controls pheromones influence on the model
    b = 1  # controls visibility influence on the model
    row = (pheromone_matrix_row**a) * (visibility_matrix_row**b)  # visibility matrix = 1/distances
    probability_matrix_row = row/np.nansum(row)
    where_nans = np.isnan(probability_matrix_row)
    probability_matrix_row[where_nans] = 0  # assign a probability of 0 to non viable paths
    distance = np.nan
    neighbors = np.argwhere(~np.isnan(matrix_row))  # neighbours have non nan values
    while np.isnan(distance):
        chosen_node = np.random.choice(nodes, 1, p=probability_matrix_row)[0]  # choose move with probabilities
        if np.all(np.in1d(neighbors, nodes_visited)):  # if all neighbours have been visited and there is no other move, reset
            return ["ant_didnt_find_food"]
        if chosen_node in nodes_visited:  # if node has already been visited, continue
            continue
        if matrix_row[chosen_node] != np.nan:  # if chosen node is valid
            distance = matrix_row[chosen_node]

    return [distance, chosen_node]


def ant_path(matrix, pheromone_matrix, visibility_matrix):
    nodes_visited = [0]
    path = []
    prev = 0
    node = 0
    total_distance = 0
    while node != len(matrix)-1:
        data = node_selection(matrix[node], pheromone_matrix[node], visibility_matrix[node], nodes_visited)
        if data[0] == "ant_didnt_find_food":  # if ant didn't find food, send it back to nest
            nodes_visited = [0]
            path = []
            prev = 0
            node = 0
            total_distance = 0
            continue
        distance = data[0]
        total_distance += distance
        node = data[1]
        path.append((prev, node))  # construct ant's path
        prev = node  # update prev node
        nodes_visited.append(node)
    return [path, total_distance]


def ant_colony(matrix):
    ant_colony_paths = []
    shortest_path = np.inf
    n_ants = 10  # choose the number of ants
    visibility_matrix = np.true_divide(1, matrix+0.1)
    pheromone_matrix = matrix.copy()
    where_non_nan = ~np.isnan(matrix)
    pheromone_matrix[where_non_nan] = 1  # initialize pheromone close to 0
    for i in range(n_ants):
        data = ant_path(matrix, pheromone_matrix, visibility_matrix)
        path = data[0]
        path_distance = data[1]
        ant_colony_paths.append((path, path_distance))
        pheromone_matrix = pheromone_update(pheromone_matrix, path, path_distance)
    for path in ant_colony_paths:
        if path[1] < shortest_path:
            shortest_path = path[1]
            show_path = path
#     print("PHEROMONE MATRIX\n", pheromone_matrix)
#     print("VISIBILITY MATRIX\n", visibility_matrix)
#     print("ANT COLONY PATHS \n", ant_colony_paths)
    print("Shortest Path: ", show_path[0], "\nCost of Shortest Path: ", show_path[1])
    return show_path
