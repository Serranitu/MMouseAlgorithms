import sys
from . import API
import numpy as np
from collections import deque

def calculate_distances(labyrinth):
    rows = len(labyrinth)
    cols = len(labyrinth[0])
    
    # Initialize a matrix to store the distances
    distances = [[float('inf') for _ in range(cols)] for _ in range(rows)]
    
    # Define the center coordinates
    center_row = rows // 2
    center_col = cols // 2
    
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
            
            # Check if the new cell is within the labyrinth and is a path (0)
            if 0 <= new_row < rows and 0 <= new_col < cols and labyrinth[new_row][new_col] == 0:
                # Calculate the new distance
                new_distance = current_distance + 1
                
                # Update the distance if it's shorter
                if new_distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_distance
                    queue.append((new_row, new_col))
    
    return distances
def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def select(algorithm:str):
    log("Running...")
    API.setColor(0, 0, "G")
    API.setText(0, 0, "abc")
    if algorithm == 'left_wall':
        log("Selected Left Wall Algorithm")
        left_wall()

def left_wall():
    while True:
        if not API.wallLeft():
            API.turnLeft()
        while API.wallFront():
            API.turnRight()
        API.moveForward()
"""distmaze := int[16][16]
 wallmaze := int[16][16]
goal := <8,8>
start := <0,0>
checks := stack of cells to verify
all cells in wallmaze := empty
for cell in distmaze
	cell := shortest dist to goal
checks.push(start)
while(start != goal)
	while(stack !empty)
		cellCheck := checks.pop
		if cellCheck.value isn't 1 greater than accessible neighbors
			minVal := minimal value of accessible neighbors of cellCheck
			cellCheck := minVal++
			for neighbor in cellCheck neighbors
				cellCheck.push(neighbor)
	advance to next ideal neighbor
return ideal path """
def flood_fill():

    wallmaze = np.zeros(16,16)