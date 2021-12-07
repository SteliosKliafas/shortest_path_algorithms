import numpy as np
import time

def create_maze():
    height = input("\n Enter the number of rows: ")
    width = input("\n Enter the number of columns: ")
    if height.isdigit() and width.isdigit():
        height, width = int(height), int(width)
        grid = np.random.randint(0, 10, (height, width))
        grid[height - 1][width - 1] = 0
        grid[0][0] = 0
        print("\n The Integer Maze: \n")
        print(grid)
        return grid
    else:
        raise ValueError("Please provide positive integer values for the number of rows and columns")


def create_row(pos, grid):
    row_of_distance_table = np.empty((len(grid), len(grid[0])))
    row_of_distance_table[:] = np.NaN
    row = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if pos[0]+1 == x and pos[1] == y or pos[0]-1 == x and pos[1] == y \
                    or pos[0] == x and pos[1] == y+1 or pos[0] == x and pos[1] == y-1:
                row_of_distance_table[x][y] = grid[x][y]
    for array in row_of_distance_table:
        row = np.concatenate([row, array], axis=None)
    # print(row)
    return row


def adjacency_matrix():
    grid = create_maze()
    distance_matrix = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            distance_matrix.append(create_row([x, y], grid))
    distance_matrix = np.vstack(distance_matrix)
    print("\n The Adjacency Matrix denoting the distances of all paths: \n")
    print(distance_matrix)
    print("\n height: ", len(distance_matrix), "width: ", len(distance_matrix[0]))
    return distance_matrix
