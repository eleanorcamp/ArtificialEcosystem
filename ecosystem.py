from Organisms import *
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
        # eater does something
        print(eater)

def sim_season(plot: Plot, periods: int = 100):
    # simulate the 100 periods
    for _ in range(periods):
        sim_period(plot)
    plot.increase_ages()

    # take stats of ecosystem at end of season
    avg_eater_eng: float = get_eater_eng(plot.eaters)
    plants_remaining: int = len(plot.plants)

def setup_plot(size: int = 100):
    plot = Plot(size)
    plot.add_plants(100)
    plot.add_eaters(10)
    return plot

def main():
    # print("Main")

    plot_size: int = 100
    plot = setup_plot(plot_size)

    print_eaters(plot)
    print_plants(plot)

main()