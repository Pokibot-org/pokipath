from cell import Cell
from utils import Coordinates
import copy

class CellGrid():
    def __init__(self, width, height):
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]
        self.height = height
        self.width = width
    
    def __getitem__(self, key : Coordinates) -> Cell:
        if not isinstance(key, Coordinates):
            raise TypeError("CellGrid can only be accesed with Coordinates as a key")
        return self.cells[key.y][key.x]

    def __setitem__(self, key: Coordinates, value):
        if not isinstance(key, Coordinates):
            raise TypeError("CellGrid can only be accesed with Coordinates as a key")
        self.cells[key.y][key.x] = value
    
    def is_outside(self, crd: Coordinates):
        return crd.x < 0 or crd.y < 0 or crd.x >= self.width or crd.y >= self.height

    def copy(self):
        new_grid = CellGrid(self.width, self.height)
        new_grid.cells = []
        for i in range(len(self.cells)):
            new_grid.cells.append(copy.deepcopy(self.cells[i]))
        return new_grid
    
    def debug_print(self):
        print("Grid : ")
        for row in self.cells:
            for cell in row:
                if (cell.is_empty()):
                    print(end=".")
                else:
                    print(end="X")
            print("")
        
    
