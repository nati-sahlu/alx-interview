#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a 2D grid.
"""

def island_perimeter(grid):
    """
    Returns the perimeter of the island defined in the grid.
    
    Args:
        grid (list of list of int): 2D grid representing water (0) and land (1).
    
    Returns:
        int: The total perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 1:
                # Start with 4 sides
                sides = 4

                # Check land above
                if y > 0 and grid[y - 1][x] == 1:
                    sides -= 1

                # Check land below
                if y < rows - 1 and grid[y + 1][x] == 1:
                    sides -= 1

                # Check land to the left
                if x > 0 and grid[y][x - 1] == 1:
                    sides -= 1

                # Check land to the right
                if x < cols - 1 and grid[y][x + 1] == 1:
                    sides -= 1

                perimeter += sides

    return perimeter

