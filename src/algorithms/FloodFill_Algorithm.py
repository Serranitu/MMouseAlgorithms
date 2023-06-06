from collections import deque
import numpy as np
from . import API


class FloodFill_Algorithm():
    def __init__(self, rows = 16, cols = 16):
        """
        Initializes a new instance of the FloodFill_Algorithm class.

        Args:
            rows (int): The number of rows in the labyrinth grid. Default is 16.
            cols (int): The number of columns in the labyrinth grid. Default is 16.
        """
        self.position = (0,0)
        self.adjacency_matrix = [[0] * 256 for _ in range(256)]
        self.index = self.position[0] * 16 + self.position[1] 
        self.rows = rows
        self.cols = cols
        self.distances = self.initialize_distances()

    def update_adjacencies(self):
        """
        Updates the adjacency matrix based on the current wall configuration.

        This method uses the API module to check for walls in different directions
        and updates the adjacency matrix accordingly.

        Returns:
            None
        """
        if API.wallRight():
            self.adjacency_matrix[self.index][self.index + 1] = 1
        if API.wallLeft():
            self.adjacency_matrix[self.index][self.index - 1] = 1 
        if API.wallFront():
            self.adjacency_matrix[self.index + 16][self.index] = 1

    def checkLeft(self):
        """
        Checks if there is a wall on the left side of the current position.

        Returns:
            bool: True if there is a wall on the left side, False otherwise.
        """
        return self.adjacency_matrix[self.index][self.index - 1] == 1

    def checkRight(self):

        return self.adjacency_matrix[self.index][self.index + 1] == 1

    def checkFront(self):
        """
        Checks if there is a wall in front of the current position.

        Returns:
            bool: True if there is a wall in front, False otherwise.
        """
        return self.adjacency_matrix[self.index + 16][self.index - 1]

    def checkBelow(self):
        """
        Checks if there is a wall below the current position.

        Returns:
            bool: True if there is a wall below, False otherwise.
        """
        return self.adjacency_matrix[self.index - 16][self.index - 1]

    def initialize_distances(self):
        """
        Initializes the distances matrix for flood-fill algorithm.

        Returns:
            list: A 2D matrix containing initial distances from the center cell.
        """
        distances = [[float('inf') for _ in range(self.cols)] for _ in range(self.rows)]
        center_row = self.rows // 2
        center_col = self.cols // 2
        queue = deque()
        
        # Set the center cell distance to 0 and enqueue it
        distances[center_row][center_col] = 0
        queue.append((center_row, center_col))
        
        # Possible neighbors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Initialize all distances in a queue
        while queue:
            row, col = queue.popleft()
            current_distance = distances[row][col]
            
            for d_row, d_col in directions:
                new_row = row + d_row
                new_col = col + d_col
                
                index = self.position[0] * 16 + self.position[1] 
                # Check if the new cell is within the labyrinth and is a path (0)
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    new_distance = current_distance + 1
                    if new_distance < distances[new_row][new_col]:
                        distances[new_row][new_col] = new_distance
                        queue.append((new_row, new_col))
        return distances

    def isValidPosition(self, new_row,new_col):
        """
        Checks if the given position is a valid position within the labyrinth grid.

        Args:
            new_row (int): The row index of the position.
            new_col (int): The column index of the position.

        Returns:
            bool: True if the position is valid, False otherwise.
        """

        if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
            return True
        return False

    def getClosest(self):
        """
        Moves to the closest valid position adjacent to the current position.

        This method checks the validity of positions in all four directions (left, right, up, down)
        and moves to the first valid position it encounters.

        Note: This method assumes that there is at least one valid adjacent position.

        Returns:
            None
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d_row, d_col in directions:
            new_row = self.position[0] + d_row
            new_col = self.position[1] + d_col
            if self.isValidPosition(new_row,new_col):
                print("valid")

    def move_mouse(old_position, new_position):
        x1, y1 = old_position
        x2, y2 = new_position

        dx = x2 - x1
        dy = y2 - y1

        if dx > 0:
            API.turnRight()
        elif dx < 0:
            API.turnLeft()
        elif dy > 0:
            API.turnRight()
            API.turnRight()
        API.moveForward()