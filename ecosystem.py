from Organisms import *
import random
from typing import List
import math
import numpy as np



# helper functions
def get_distance(point1, point2):
    return math.dist(point1,point2)

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

def check_valid_coords(loc: np.ndarray):
    x = loc[0]
    y = loc[1]

    if   x > 100: x = 100
    elif x < 0:   x = 0

    if   y > 100: y = 100
    elif y < 0:   y = 0

    return x,y



# DIRECTIONS: List[tuple] = [(0,2), (2,0), (0,-2), (-2,0)]
DIRECTIONS: List[tuple] = [
    (0, 2),    # North
    (1, 1),    # Northeast
    (2, 0),    # East
    (1, -1),   # Southeast
    (0, -2),   # South
    (-1, -1),  # Southwest
    (-2, 0),   # West
    (-1, 1)    # Northwest
]

# code modified from https://www.analytics-link.com/post/2018/08/21/calculating-the-compass-direction-between-two-points-in-python
def get_direction(origin, destination):
    delta_x = destination[0] - origin[0]
    delta_y = destination[1] - origin[1]

    degrees = math.atan2(delta_x, delta_y)/math.pi*180
    if degrees < 0:
        degrees = 360 + degrees

    compass_brackets = DIRECTIONS + [(2,0)]

    compass_lookup = round(degrees / 45)
    # print(compass_brackets)
    return compass_brackets[compass_lookup]

def get_closest_plant(eater: Eater, plants: List):
    min_dist: float = float('inf')
    closest_plant = None
    for plant in plants:
        this_dist: float = get_distance(eater.location, plant.location)
        if this_dist < min_dist:
            min_dist: float = this_dist
            closest_plant = plant
    return closest_plant

def move_eater(plot: Plot, eater: Eater, direction: tuple):
    # grab values of previous eater location and set it to 0
    old_x,old_y = eater.location
    plot.grid[old_x][old_y] = 0

    # calculate new location and validate it
    new_loc: np.ndarray = np.add(eater.location, direction)
    loc: tuple = check_valid_coords(new_loc)
    eater.location = loc

    # update plot.grid status
    new_x, new_y = eater.location
    plot.grid[new_x][new_y] = 2

def is_valid_index(i: int, j: int, n: int, m: int):
    return not (i < 0 or j < 0 or i > n - 1 or j > m - 1)
def get_neighbors(arr: List, i: int, j: int):
    # Size of given 2d array
    n: int = len(arr)
    m: int  = len(arr[0])

    # Initialising a vector array
    # where adjacent element will be stored
    v: List = []

    # Checking for all the possible adjacent positions
    if is_valid_index(i - 1, j - 1, n, m):   v.append(arr[i - 1][j - 1])
    if is_valid_index(i - 1, j,     n, m):   v.append(arr[i - 1][j])
    if is_valid_index(i - 1, j + 1, n, m):   v.append(arr[i - 1][j + 1])
    if is_valid_index(i,     j - 1, n, m):   v.append(arr[i][j - 1])
    if is_valid_index(i,     j + 1, n, m):   v.append(arr[i][j + 1])
    if is_valid_index(i + 1, j - 1, n, m):   v.append(arr[i + 1][j - 1])
    if is_valid_index(i + 1, j,     n, m):   v.append(arr[i + 1][j])
    if is_valid_index(i + 1, j + 1, n, m):   v.append(arr[i + 1][j + 1])

    # Returning the vector
    return v


def get_neighbor_indices(arr: List, i: int, j: int):
    # Size of given 2d array
    n: int = len(arr)
    m: int  = len(arr[0])

    # Initialising a vector array
    # where adjacent element will be stored
    v: List = []

    # Checking for all the possible adjacent positions
    if is_valid_index(i - 1, j - 1, n, m):   v.append( (i-1, j-1) )
    if is_valid_index(i - 1, j,     n, m):   v.append( (i-1, j  ) )
    if is_valid_index(i - 1, j + 1, n, m):   v.append( (i-1, j+1) )
    if is_valid_index(i,     j - 1, n, m):   v.append( (i,   j-1) )
    if is_valid_index(i,     j + 1, n, m):   v.append( (i,   j+1) )
    if is_valid_index(i + 1, j - 1, n, m):   v.append( (i+1, j-1) )
    if is_valid_index(i + 1, j,     n, m):   v.append( (i+1, j  ) )
    if is_valid_index(i + 1, j + 1, n, m):   v.append( (i+1, j+1) )

    # Returning the vector
    return v

def get_eater_from_loc(arr: list[Eater], loc: tuple):
    for eater in arr:
        # print(f"LOC: {loc}\tEATER_LOC: {eater.location}")
        if eater.location == loc:
            return eater
    return None

def sim_period(plot: Plot):
    for eater in plot.eaters:

        if eater.state["last_mated"] > 25:

            mating_focus: int = eater.genes["mating_focus"]
            task_option: str = random.choices(["mate", "move"],
                                              weights=[1-mating_focus, mating_focus], k=1)[0]
            # print(f"TASK: {task_option}")
            if task_option == "mate":

                eater_x: int = eater.location[0]
                eater_y: int = eater.location[1]
                # eater.state["last_decision"] = Decision.MATE
                eater_neighbors: list = get_neighbors( plot.grid, eater.location[0], eater.location[1] )
                # if this eater has other eaters in its surrounding area
                if 2 in eater_neighbors:
                    eater.state["debugging"] = "IN THE LOOP"
                    eater_mate_score: int = eater.genes["mating_score"]
                    # find locations of potential mates
                    potential_mates_locations: List[tuple] = get_neighbor_indices(plot.grid, eater_x, eater_y)

                    # make a list of potential mates from those locations
                    potential_mates: List[Eater] = []
                    for point in potential_mates_locations:
                        potential_mate = get_eater_from_loc(plot.eaters, point)
                        if potential_mate: potential_mates.append(potential_mate)

                    # go through potential mates to (hopefully) find a pair
                    for pm in potential_mates:
                        # if two eaters are same sex go to the next potential_mate
                        if eater.sex == pm.sex:
                            continue
                        # if eater mating_score is too low go to the next
                        if eater.sex == "male" and eater_mate_score < pm.genes["mating_score"]:
                            continue
                        # if potential mate mating_score is too low go to the next
                        if eater.sex == "female" and eater_mate_score > pm.genes["mating_score"]:
                            continue
                        else:
                            print(f"{eater.sex.upper()}: {eater_mate_score}  AND "
                                  f"{pm.sex} potential mate: {pm.genes["mating_score"]}")
                            # reset eaters' last_mated
                            eater.state["last_mated"] = 0
                            pm.state["last_mated"] = 0
                            # add child eater to random spot
                            plot.add_eaters(1)
                            # print("WE HAVE A MATE")
                            break
                    # not exactly sure what type of eater is being left
                    # in this section, but it needs to have it's last_mated incremented
                    eater.state["debugging"] = "left behind?"
                    if eater.state["last_mated"] > 0: eater.state["last_mated"] += 1
                else:
                    # handle the food/random movement
                    eater.state["last_mated"] += 1
                    continue
    nums = set()
    for eater in plot.eaters:
        nums.add(eater.state["last_mated"])
        # print(f"{eater.state["debugging"]}  {eater.state["last_mated"]}")
    print(nums)




# simulation functions
def sim_period_beta(plot: Plot):
    # DEBUGGING
    """
    for eater in plot.eaters:
        print(f" Eater currently at {eater.location} ")
    for plant in plot.plants:
        print(f"Plant currently at {plant.location}")
    """

    # initial decision of "move or stay to mate"
    for eater in plot.eaters:
        mating_focus: int = eater.genes["mating_focus"]
        task_option: str = random.choices(["mate", "move"],
                                          weights=[mating_focus, 1 - mating_focus], k=1)[0]
        # print(f"TASK OPTION: {type(task_option)}") # debugging
        if task_option == 'move':
            eater.state["last_decision"] = Decision.MOVE
            food_seek: float = eater.genes["food_seeking"]
            movement_choice: str = random.choices(["food", "random"],
                                                  weights=[food_seek, 1 - food_seek], k=1)[0]
            if movement_choice == "random":
                move_direction: tuple = random.choice(DIRECTIONS)
                move_eater(plot, eater, move_direction)
            elif movement_choice == "food":
                closest_plant = get_closest_plant(eater, plot.plants)
                move_direction = get_direction(eater.location, closest_plant.location)
                move_eater(plot, eater, move_direction)
            # print(f"Eater now at {eater.location}") # debugging

        elif task_option == "mate":
            eater.state["last_decision"] = Decision.MATE

    # go through plot, attempt to feed/mate all eaters
    for i in range( len(plot.grid) ):
        for j in range( len(plot.grid[i]) ):
            # if there is a plant at the current index
            # we check it for neighboring eaters
            if plot.grid[i][j] == 1:
                neighbors = get_neighbor_indices(plot.grid, i, j)


    # go through eaters again to determine eating or mating status
    for eater in plot.eaters:
        # try to eat for every eater that moved
        if eater.state["last_decision"] == Decision.MOVE:
            print("EATER STATE MOVE")
            strength: int = eater.genes["strength"]


        elif eater.state["last_decision"] == Decision.MATE:
            print("EATER STATE MATE")
            # add logic to (hopefully) mate
            mating_score: int = eater.genes["mating_score"]


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
    plot = setup_plot(plot_size, 1, 100)
    sim_period(plot)

    # print_eaters(plot)
    # print_plants(plot)

if __name__ == "__main__":
    main()