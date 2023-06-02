from collections import deque
import numpy as np
from . import API


class FloodFill_Algorithm():
    def __init__(self):
        self.position = (0,0)
        self.adjacency_matrix = [[0] * 256 for _ in range(256)]
        self.distmaze = np.zeros((16,16))
        self.index = self.position[0] * 16 + self.position[1] 
        self.rows = 16
        self.cols = 16

def update_adjacencies(self):
    if API.wallRight():
        self.adjacency_matrix[self.index][self.index + 1] = 1
    if API.wallLeft():
        self.adjacency_matrix[self.index][self.index - 1] = 1 
    if API.wallFront():
        self.adjacency_matrix[self.index + 16][self.index] = 1

def checkLeft(self):
    return self.adjacency_matrix[self.index][self.index - 1] == 1

def checkRight(self):

    return self.adjacency_matrix[self.index][self.index + 1] == 1

def checkFront(self):

    return self.adjacency_matrix[self.index + 16][self.index - 1]

def checkBelow(self):

    return self.adjacency_matrix[self.index - 16][self.index - 1]



def calculate_distances(self):
    
    # Initialize a matrix to store the distances
    distances = [[float('inf') for _ in range(self.cols)] for _ in range(self.rows)]
    
    # Define the center coordinates
    center_row = self.rows // 2
    center_col = self.cols // 2
    
    # Create a queue for BFS
    queue = deque()
    
    # Set the center cell distance to 0 and enqueue it
    distances[center_row][center_col] = 0
    queue.append((center_row, center_col))
    
    # Define the possible neighbors' directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Perform BFS
    while queue:
        row, col = queue.popleft()
        current_distance = distances[row][col]
        
        # Check all four neighbors
        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col
            
            index = self.position[0] * 16 + self.position[1] 
            # Check if the new cell is within the labyrinth and is a path (0)
            if 0 <= new_row < rows and 0 <= new_col < cols and labyrinth[new_row][new_col] == 0:
                # Calculate the new distance
                new_distance = current_distance + 1
                
                # Update the distance if it's shorter
                if new_distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_distance
                    queue.append((new_row, new_col))
    
    return distances

