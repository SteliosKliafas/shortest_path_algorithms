import numpy as np


def dijkstra(matrix, source=0):
    vertices = len(matrix)
    not_visited = np.arange(0, vertices)  # list of nodes from (0, 1, 2, 3 ..., N)
    previous_node_list = [np.nan] * vertices  # list of previous nodes for each node (how we get there)
    shortest_distance_from_source_list = [np.inf] * vertices  # table of node distances from source (values init to inf)
    shortest_distance_from_source_list[source] = 0  # value of source to source is 0

    while len(not_visited) != 0:  # visit all nodes, if yes than dijkstra's algorithm has finished
        current_node = not_visited[0]  # initialize current_node to source
        for node in not_visited:  # loop over unvisited nodes to find the shortest distance from source so far
            if shortest_distance_from_source_list[node] < shortest_distance_from_source_list[current_node]:
                current_node = node  # set current node to node with shortest distance from source
        not_visited = np.delete(not_visited, np.where(not_visited == current_node))

        for i in range(vertices):
            if matrix[current_node][i] == np.NaN:  # if there is no path from current_node to node i continue
                continue
            distance = shortest_distance_from_source_list[current_node] + matrix[current_node][
                i]  # calculate total distance to next node
            if distance < shortest_distance_from_source_list[
                i]:  # if distance is shorter than our current one, update it
                shortest_distance_from_source_list[i] = distance
                previous_node_list[i] = current_node  # update the node which holds the shortest distance to node i

    #     print("Dijkstra previous node list: ", previous_node_list)
    #     print("\nDijkstra distance matrix: ", shortest_distance_from_source_list)
    i = vertices - 1
    path = [i]
    while i != 0:
        path.append(previous_node_list[i])
        i = previous_node_list[i]
    print("Shortest Path: ", list(reversed(path)), "\nCost of Shortest Path: ",
          shortest_distance_from_source_list[vertices - 1])
    return shortest_distance_from_source_list, previous_node_list
