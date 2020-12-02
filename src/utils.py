

class Coordinates():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y


    def __eq__(self, other):
        if type(self) != type(other):
            raise TypeError("Cant compare Coordinate with " + str(type(other)))
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        return f"Coordinate<x:{self.x},y:{self.y}>"

    def __str__(self):
        return self.__repr__()
