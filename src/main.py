import pygame
import sys

from cell import Cell, CELL_STATUS_EMPTY, CELL_STATUS_OCCUPIED
from utils import Coordinates
from cellgrid import CellGrid

BACKGROUND_COLOR = (33, 28, 28)
EMPTY_CELL_COLOR = (220, 220, 220)
GOAL_CELL_COLOR = (113, 240, 100)
START_CELL_COLOR = (71, 220, 205)
OCCUPIED_CELL_COLOR = (216, 34, 50)
CHOSEN_PATH_CELL_COLOR = (150, 40, 250)

BORDER_COLOR = (0, 0, 0)

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600


class Grid(CellGrid):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block_size = WINDOW_WIDTH//width
        self.cellgrid = CellGrid(self.width, self.height)
        self.start = None
        self.goal = None

    

    def get_cell_color(self, cell_coordinates):
        if self.start is not None:
            if self.start == cell_coordinates:
                return START_CELL_COLOR
        if self.goal is not None:
            if self.goal == cell_coordinates:
                return GOAL_CELL_COLOR
        if not self.cellgrid[cell_coordinates].is_empty():
            return OCCUPIED_CELL_COLOR
        return EMPTY_CELL_COLOR

    def draw(self):
        cell_coordinates = Coordinates()
        for x in range(self.width):
            for y in range(self.height):
                cell_coordinates.update(x, y)
                cell = pygame.Rect(x*self.block_size, y*self.block_size,
                                self.block_size, self.block_size)
                
                
                pygame.draw.rect(SCREEN, self.get_cell_color(cell_coordinates), cell)
                pygame.draw.rect(SCREEN, BORDER_COLOR, cell, 1)


    def add_obstacle(self, crd : Coordinates):
        self.cellgrid[crd].occupy()
    
    def compute_path(self, crd_start : Coordinates, crd_goal : Coordinates):
        self.start = crd_start
        self.goal = crd_goal

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BACKGROUND_COLOR)


    grid_width = 30
    grid_height = 20
    grid = Grid(grid_width, grid_height)
    grid.add_obstacle(Coordinates(10,10))
    grid.add_obstacle(Coordinates(11,10))
    grid.add_obstacle(Coordinates(9,10))
    grid.add_obstacle(Coordinates(10,9))
    grid.add_obstacle(Coordinates(10,11))
    grid.compute_path(Coordinates(2,2), Coordinates(grid_width - 2, grid_height - 2))


    while True:
        grid.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()