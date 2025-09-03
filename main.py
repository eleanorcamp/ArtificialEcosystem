from Organisms import *
from ecosystem import *
from DataContainer import *


def main():
    plot_size: int = 100
    plot = setup_plot(plot_size, 100, 50)

    # uncomment line below to display initial plot
    # display_image(plot)

    # initial dictionary to hold DataContainer objects
    containers = dict()

    # simulate the seasons
    for i in range(10):
        print("SEASON: " + str(i))
        # if no eaters left then break
        if len(plot.eaters) < 1:
            break

        # simulate a season
        sim_season(plot, 100, False)

        # uncomment line below to display season results
        # display_plot(plot)

        # get data from the end of the season
        container = DataContainer()
        container.update_eaters(plot.eaters)
        container.update_plants(plot.plants)
        containers[f"container_{i}"] = container

    # uncomment line below to display ending results
    # display_image(plot)

    # print some results for data analysis
    # print(containers["container_0"].gene_count)


if __name__ == "__main__":
    main()