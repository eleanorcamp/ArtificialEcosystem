from Organisms import *

class DataContainer:
    def __init__(self):
        self.gene_count: dict = {"food_seeking": None,
                                 "strength": None,
                                 "mating_score": None,
                                 "mating_focus": None}
        self.eaters: list = []
        self.eater_count: int = 0
        self.plants: list = []
        self.plant_count: int = 0
        self.energy_list: list = []

    def update_genes(self, eaters: list[Eater]):
        food_seeking: list = []
        strength: list = []
        mating_score: list = []
        mating_focus: list = []

        for e in eaters:
            food_seeking.append(e.genes["food_seeking"])
            strength.append(e.genes["strength"])
            mating_score.append(e.genes["mating_score"])
            mating_focus.append(e.genes["mating_focus"])

        self.gene_count["food_seeking"] = food_seeking
        self.gene_count["strength"] = strength
        self.gene_count["mating_score"] = mating_score
        self.gene_count["mating_focus"] = mating_focus

    def update_eaters(self, eaters: list[Eater]):
        self.eaters = eaters
        self.eater_count = len(eaters)
        self.update_genes(eaters)

    def update_plants(self, plants: list[Plant]):
        self.plants = plants
        self.eater_count = len(plants)

