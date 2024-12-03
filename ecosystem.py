import random
from Organisms import *
# import numpy as np

def get_eater_eng(eaters: List[Eater]):
    eng_sum: float = 0
    for eater in eaters:
        eng_sum += eater.energy
    return eng_sum / len(eaters)

def sim_period(plot: Plot):
    for eater in plot.eaters:
        # eater does something
        print(eater)

def sim_season(plot: Plot, periods: int = 100):
    # simulate the 100 periods
    for _ in range(periods):
        sim_period(plot)

    # take stats of ecosystem at end of season
    avg_eater_eng: float = get_eater_eng(plot.eaters)
    plants_remaining: int = len(plot.plants)


def add_plants(plot: Plot, num_plants: int = 100):
    plants_added: int = 0
    while plants_added < num_plants:
        x = random.randint(0, plot.size - 1)
        y = random.randint(0, plot.size - 1)
        if plot.grid[x][y] == 0:
            plot.grid[x][y] = 1
            plants_added += 1
    return plot

def add_eaters(plot: Plot, num_eaters: int = 10):
    eaters_added: int = 0
    while eaters_added < num_eaters:
        x = random.randint(0, plot.size - 1)
        y = random.randint(0, plot.size - 1)
        if plot.grid[x][y] == 0:
            plot.grid[x][y] = 2
            eaters_added += 1
    return plot

def setup_plot(size: int = 100):
    plot = Plot(size)
    add_plants(plot, 100)
    add_eaters(plot, 10)
    return plot

def main():
    # print("Main")

    plot_size: int = 100
    plot = setup_plot(plot_size)

    # plot: Plot = Plot(plot_size)
    # plot =
    # print(plot.grid)
    for row in plot.grid:
        print(row)

main()