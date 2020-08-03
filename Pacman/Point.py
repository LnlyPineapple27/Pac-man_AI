import math
import copy as cp


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def manhattan_distant(self, another):
        return abs(self.x - another.x) + abs(self.y - another.y)

    def euclid_distant(self, another):
        return math.sqrt((self.x - another.x)**2 + (self.y - another.y)**2)

    def position(self):
        return cp.copy(self.x), cp.copy(self.y)
