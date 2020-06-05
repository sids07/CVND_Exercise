import pdb
from helpers import normalize, blur
import numpy as np

def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    grid = np.array(grid)
    beliefs = np.array(beliefs)
    new_beliefs = np.zeros_like(beliefs)
    s=0
    # loop through all grid cells
    for i in range(beliefs.shape[0]):
        for j in range(beliefs.shape[1]):
        # check if the sensor reading is equal to the color of the grid cell
        # if so, hit = 1
        # if not, hit = 0
            hit = (color == grid[i][j]) 
            new_beliefs[i][j]=beliefs[i][j] * (hit * p_hit + (1-hit) * p_miss)
    
    for i in range(new_beliefs.shape[0]):
        for j in range(new_beliefs.shape[1]):
            s += new_beliefs[i][j]
    # divide all elements of q by the sum to normalize
    for i in range(new_beliefs.shape[0]):
        for j in range(new_beliefs.shape[1]):
            new_beliefs[i][j] = new_beliefs[i][j] / s
    #
    # TODO - implement this in part 2
    grid = grid.tolist()
    beliefs = beliefs.tolist()

    return new_beliefs.tolist()


def move(dy, dx, beliefs, blurring):
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy ) % height
            new_j = (j + dx ) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
    return blur(new_G, blurring)