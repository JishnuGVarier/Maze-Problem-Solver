import pygame
from cell import Cell

class Maze:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.thickness = 4
        self.grid_cells = [Cell(col, row, self.thickness) for row in range(self.rows) for col in range(self.cols)]

    # carve grid cell walls. It used to remove the walls b/w the cell to carve the path
    def remove_walls(self, current, next):
        dx = current.x - next.x#this will find the relative position of the next cell to current cell
        if dx == 1:#If dx is 1, it means next is to the left of current.
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:# If dx is -1, it means next is to the right.
            current.walls['right'] = False
            next.walls['left'] = False
        dy = current.y - next.y#same as above
        if dy == 1:#If dy is 1, it means next is above current.
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:#If dy is 1, it means next is above current.
            current.walls['bottom'] = False
            next.walls['top'] = False

    # generates maze
    def generate_maze(self):
        current_cell = self.grid_cells[0]#initialize the current cell with the first cell
        array = []
        break_count = 1#this will track the no of visited cells...this will be done until all cells are visited
        while break_count != len(self.grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(self.cols, self.rows, self.grid_cells)
            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                self.remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()#pops it and set it as current cell...like backtracking
        return self.grid_cells
    
