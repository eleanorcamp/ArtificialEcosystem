from Organisms import *
import random
# import numpy as np

# helper functions
def get_eater_eng(eaters: List[Eater]):
    eng_sum: float = 0
    for eater in eaters:
        eng_sum += eater.energy
    return eng_sum / len(eaters)

def print_eaters(plot: Plot):
    for eater in plot.eaters:
        print(f"There is an eater at {eater.location}")
    print(f"There are currently {len(plot.eaters)} total eaters")

def print_plants(plot: Plot):
    for plant in plot.plants:
        print(f"There is a plant at {plant.location}")
    print(f"There are currently {len(plot.plants)} total plants")


# simulation functions
def sim_period(plot: Plot):
    for eater in plot.eaters:
        # gather variables from eater
        food_seek: float = eater.genes["food_seeking"]
        strength: int = eater.genes["strength"]
        mating_score: int = eater.genes["mating_score"]
        mating_focus: int = eater.genes["mating_focus"]
        current_location: tuple = eater.location

        # determine eater's preferred choice
        task_option: str = random.choices(["reproduce", "move"],
                                         weights = [mating_focus, 1-mating_focus])

        if task_option == "move":
            plant_nearby: bool = False
            movement_choice: str = random.choices(["food", "random"],
                                             weights = [food_seek, 1-food_seek])


        # print(f"Eater with food_seek: {mating_focus} has chosen: {task_option}")

def sim_season(plot: Plot, periods: int = 100):
    # simulate the 100 periods
    for _ in range(periods):
        sim_period(plot)
    plot.increase_ages()

    # take stats of ecosystem at end of season
    avg_eater_eng: float = get_eater_eng(plot.eaters)
    plants_remaining: int = len(plot.plants)

def setup_plot(size: int = 100, plant_count: int = 100, eater_count: int = 25):
    plot = Plot(size)
    # add `plant_count` plants to the plot, randomly located
    plot.add_plants(plant_count)
    # add `eater_count` eaters to the plot with random a random
    # location, and random values for all genes
    plot.add_eaters(eater_count)
    return plot

def main():
    # print("Main")

    plot_size: int = 100
    plot = setup_plot(plot_size)
    sim_period(plot)

    # print_eaters(plot)
    # print_plants(plot)

main()