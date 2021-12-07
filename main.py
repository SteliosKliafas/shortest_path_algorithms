from algorithms.ant_colony_optimization import ant_colony
from algorithms.dijkstra import dijkstra
from algorithms.floyd_warshall import floyd_warshall
from maze.maze import adjacency_matrix
import time


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_grid = adjacency_matrix()

    start_time = time.time()
    print("\n ANT COLONY OPTIMIZATION ALGORITHM \n")
    ant_colony(data_grid)
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time1 = time.time()
    print("\n DIJKSTRA'S ALGORITHM \n")
    dijkstra(data_grid)
    print("--- %s seconds ---" % (time.time() - start_time1))

    start_time2 = time.time()
    print("\n FLOYD WARSHALL ALGORITHM \n")
    floyd_warshall(data_grid)
    print("--- %s seconds ---" % (time.time() - start_time2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
