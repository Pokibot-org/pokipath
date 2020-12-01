from cell import Cell
from utils import Coordinates


class CellGrid():
    def __init__(self, width, height):
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]
    
    def __getitem__(self, key : Coordinates) -> Cell:
        if not isinstance(key, Coordinates):
            raise TypeError("CellGrid can only be accesed with Coordinates as a key")
        return self.cells[key.y][key.x]

    def __setitem__(self, key: Coordinates, value):
        if not isinstance(key, Coordinates):
            raise TypeError("CellGrid can only be accesed with Coordinates as a key")
        self.cells[key.y][key.x] = value