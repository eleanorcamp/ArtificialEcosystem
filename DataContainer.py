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
        self.mated_list: list = []
        self.death_count: int = 0
        self.reproduce_count: int = 0

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

    def update_mated_list(self, plot: Plot):
        self.mated_list = plot.mated_list
        self.reproduce_count = len(self.mated_list)

    def update_dead_eaters(self, dead_eaters: list[Eater]):
        self.death_count = len(dead_eaters)

    def update_energy_levels(self, eaters: list[Eater]):
        self.energy_list = [eater.energy for eater in eaters]