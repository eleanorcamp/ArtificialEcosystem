from typing import List
import numpy as np


class Eater:
    def __init__(self, x: int, y: int):
        self.genes: List = []
        self.energy: int = 0
        self.age: int = 0
        self.location = (x, y)

        self.plants_eaten: int = 0
        self.distance_covered: int = 0
        self.num_kids: int = 0

    def set_location(self, x: int, y: int):
        self.location = (x, y)

    def inc_age(self):
        self.age += 1

class Plant:
    def __init__(self, x: int, y: int):
        self.age: int = 0
        self.location = (x, y)

    def inc_age(self):
        self.age += 1

class Plot:
    def __init__(self, size):
        self.grid = np.zeros([size, size])
        self.eaters: List[Eater] = list()
        self.plants: List[Plant] = list()
        self.size: int = size
