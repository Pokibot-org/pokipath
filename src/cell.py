
CELL_STATUS_EMPTY = 0
CELL_STATUS_OCCUPIED = 1
# STATUS_IS_GOAL = 2
# STATUS_IS_START = 3

class Cell():
    def __init__(self, status=CELL_STATUS_EMPTY):
        self.status = status
    
    def is_empty(self):
        return self.status == CELL_STATUS_EMPTY
    
    def empty(self):
        self.status = CELL_STATUS_EMPTY

    def occupy(self):
        self.status = CELL_STATUS_OCCUPIED