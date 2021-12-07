import numpy as np


def floyd_warshall(matrix):
    vertices = len(matrix)
    fw_distance_matrix = matrix.copy()  # make a copy of matrix, (if there is no distance keep the default ones)
    fw_distance_matrix[np.isnan(fw_distance_matrix)] = np.inf  # fill indirect paths as well in fw_distance_matrix
    path_matrix = np.zeros((vertices, vertices))  # create the path matrix initially filled with 0's

    for i in range(vertices):
        for j in range(vertices):
            path_matrix[i, j] = i  # replace each line with the corresponding vertex

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if i != j:
                    if fw_distance_matrix[i][j] > fw_distance_matrix[i][k] + fw_distance_matrix[k][j]:  # if our default value is larger replace it
                        fw_distance_matrix[i][j] = fw_distance_matrix[i][k] + fw_distance_matrix[k][j]  # update shortest distance from i to j
                        path_matrix[i, j] = path_matrix[k, j]  # update the optimal previous node
                else:
                    fw_distance_matrix[i][j] = 0  # distances from the same node equal to 0
#     print("Floyd-Warshall distances matrix: \n")
#     print(fw_distance_matrix)
#     print("\nPath matrix: \n")
#     print(path_matrix)
    path = reconstruct_path(path_matrix, len(matrix) - 1)  # reconstruct the path to the destination node
    print("Floyd-Warshall Shortest Path: ", path, "\nCost of Shortest Path: ", fw_distance_matrix[0][len(fw_distance_matrix[0])-1])
    return path


def reconstruct_path(path_matrix, destination, path=[]):
    source = 0
    destination = int(destination)
    if source == destination:  # return path if destination is reached
        path += [source]
        shortest_path = list(reversed(path))
        return shortest_path
    else:
        path += [destination]  # add current node
        return reconstruct_path(path_matrix, path_matrix[source, destination])  # update destination
