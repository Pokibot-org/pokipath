import pygame
import sys

from cell import Cell, CELL_STATUS_EMPTY, CELL_STATUS_OCCUPIED
from utils import Coordinates
from cellgrid import CellGrid

BACKGROUND_COLOR = (33, 28, 28)
EMPTY_CELL_COLOR = (220, 220, 220)
GOAL_CELL_COLOR = (113, 240, 100)
START_CELL_COLOR = (71, 220, 205)
OCCUPIED_CELL_COLOR = (180, 34, 50)
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
        self.start_pathfinding = False

    

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
        for cell_coordinates.x in range(self.width):
            for cell_coordinates.y in range(self.height):
                cell = pygame.Rect(cell_coordinates.x*self.block_size, cell_coordinates.y*self.block_size,
                                self.block_size, self.block_size)
                
                
                pygame.draw.rect(SCREEN, self.get_cell_color(cell_coordinates), cell)
                pygame.draw.rect(SCREEN, BORDER_COLOR, cell, 1)


    def add_obstacle(self, crd : Coordinates):
        self.cellgrid[crd].occupy()
    
    def compute_path(self, crd_start : Coordinates, crd_goal : Coordinates):
        self.start = crd_start
        self.goal = crd_goal
        self.start_pathfinding = True
    
    def _get_empty_neightbour_count(self, cell_coordinates : Coordinates, grid : CellGrid):
        count = 0
        for x in range(-1,2):
            for y in range(-1,2):
                if (abs(x) == abs(y)):
                    continue
                neighbour_cell = Coordinates(cell_coordinates.x + x, cell_coordinates.y + y)

                if self.cellgrid.is_outside(neighbour_cell):
                    continue
                
                if self.cellgrid[neighbour_cell].is_empty():
                    count += 1

        return count
    
    def _occupied_cell_behaviour(self, cell_coordinates : Coordinates, grid : CellGrid):
        for x in range(-1,2):
            for y in range(-1,2):
                if (abs(x) == abs(y)):
                    continue
                neighbour_cell = Coordinates(cell_coordinates.x + x, cell_coordinates.y + y)
                
                if self.cellgrid.is_outside(neighbour_cell):
                    continue
                
                if not self.cellgrid[neighbour_cell].is_empty():
                    continue
                
                if self._get_empty_neightbour_count(neighbour_cell, grid) >= 3:
                    grid[neighbour_cell].occupy()
                
                if self._get_empty_neightbour_count(neighbour_cell, grid) <= 1:
                    grid[neighbour_cell].occupy()
                
            
            
    def process_pathfinding(self):
        if self.start_pathfinding:
            cell_coordinates = Coordinates()
            tmp_grid = self.cellgrid.copy()
            for cell_coordinates.x in range(self.width):
                for cell_coordinates.y in range(self.height):
                    if not self.cellgrid[cell_coordinates].is_empty():
                        self._occupied_cell_behaviour(cell_coordinates, tmp_grid)
                        
                    if (cell_coordinates.x == 0 or 
                        cell_coordinates.y == 0 or 
                        cell_coordinates.x == self.width-1 or 
                        cell_coordinates.y == self.height-1):
                        if not (cell_coordinates == self.goal or cell_coordinates == self.goal):
                            tmp_grid[cell_coordinates].occupy()
                    
                    ## end process
                    if cell_coordinates == self.goal or cell_coordinates == self.goal:
                        tmp_grid[cell_coordinates].empty()
            self.cellgrid = tmp_grid.copy()



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

    fps = 2
    anim_speed = int(1/fps * 1000)

    while True:
        grid.draw()
        grid.process_pathfinding()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        pygame.time.delay(anim_speed)


if __name__ == "__main__":
    main()