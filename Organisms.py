from typing import List, Dict
from enum import Enum
import numpy as np
import random
from math import dist

class Decision(Enum):
    MOVE = "move"
    MATE = "mate"
    FAILED_MATE = "failed_mate"

class Eater:
    def __init__(self, x: int, y: int, genes: Dict):
        self.genes: list = [] # food_seeking, strength, mating_score, mating_focus
        self.energy: int = 50
        self.age: int = 0
        self.location = (x, y)
        self.genes: Dict = genes
        self.sex: str = random.choice(["male", "female"])
        self.state: Dict = {
                        "last_decision": None,
                        "eaten": None,
                        "last_mated": 0,
                        "debugging": None
        }

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
        self.eaters: list[Eater] = list()
        self.plants: list[Plant] = list()
        self.size: int = size

    def add_plants(self, num_plants: int = 100):
        plants_added: int = 0
        while plants_added < num_plants:
            x: int = random.randint(0, self.size - 1)
            y: int = random.randint(0, self.size - 1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = 1
                self.plants.append( Plant(x, y) )
                plants_added += 1

    def add_eaters(self, num_eaters: int = 10):
        eaters_added: int = 0
        while eaters_added < num_eaters:
            x: int = random.randint(0, self.size - 1)
            y: int = random.randint(0, self.size - 1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = 2
                this_gene: dict = {"food_seeking": random.random(),
                             "strength": random.randint(1, 20),
                             "mating_score": random.randint(1, 20),
                             "mating_focus": 0.5}
                self.eaters.append( Eater(x, y, this_gene) )
                eaters_added += 1

    def increase_ages(self):
        for eater in self.eaters:
            eater.inc_age()
        for plant in self.plants:
            plant.inc_age()
