from Organisms import *
from ecosystem import *
from DataContainer import *
import seaborn as sns


def plot_gene_averages(containers: dict):
    food_seeking_avg = []
    strength_avg = []
    mating_score_avg = []
    mating_focus_avg = []

    for container in containers.values():
        food_seeking_avg.append(sum(container.gene_count["food_seeking"]) / len(container.gene_count["food_seeking"]))
        strength_avg.append(sum(container.gene_count["strength"]) / len(container.gene_count["strength"]))
        mating_score_avg.append(sum(container.gene_count["mating_score"]) / len(container.gene_count["mating_score"]))
        mating_focus_avg.append(sum(container.gene_count["mating_focus"]) / len(container.gene_count["mating_focus"]))

    seasons = list(range(len(containers)))

    plt.figure(figsize=(10, 6))
    plt.plot(seasons, food_seeking_avg, label="Food Seeking", color='blue')
    plt.plot(seasons, strength_avg, label="Strength", color='green')
    plt.plot(seasons, mating_score_avg, label="Mating Score", color='red')
    plt.plot(seasons, mating_focus_avg, label="Mating Focus", color='purple')

    plt.xlabel('Season')
    plt.ylabel('Average Gene Value')
    plt.title('Gene Averages Over Seasons')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_gene_distributions(containers: dict, gene_name: str):
    plt.figure(figsize=(10, 6))

    # Iterate over each container and its index in the dictionary
    for i, container in enumerate(containers.values()):
        plt.hist(container.gene_count[gene_name], bins=20, alpha=0.5, label=f'Season {i+1}')

    plt.xlabel(f'{gene_name} Value')
    plt.ylabel('Frequency')
    plt.title(f'Distribution of {gene_name} Over Seasons')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_gene_averages_with_secondary_axis(containers: dict):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot the first two genes on the primary y-axis (0-1 scale)
    for i, container in enumerate(containers.values()):
        ax1.plot(container.gene_count["food_seeking"], label=f'Food Seeking (Season {i})', alpha=0.7)
        ax1.plot(container.gene_count["mating_focus"], label=f'Mating Focus (Season {i})', alpha=0.7)

    ax1.set_xlabel('Generation')
    ax1.set_ylabel('Gene Value (0-1)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create a secondary y-axis to plot genes with higher values
    ax2 = ax1.twinx()
    for i, container in enumerate(containers.values()):
        ax2.plot(container.gene_count["strength"], label=f'Strength (Season {i})', alpha=0.7, linestyle='--')
        ax2.plot(container.gene_count["mating_score"], label=f'Mating Score (Season {i})', alpha=0.7, linestyle='--')

    ax2.set_ylabel('Gene Value (1-20)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    plt.title('Gene Averages Over Seasons (With Secondary Axis)')
    fig.tight_layout()  # To prevent label overlap
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()

def plot_energy_levels(containers: dict):
    energy_avg = []

    for container in containers.values():
        energy_avg.append(sum(container.energy_list) / len(container.energy_list))

    seasons = list(range(len(containers)))

    plt.figure(figsize=(10, 6))
    plt.plot(seasons, energy_avg, label="Average Energy", color='orange')

    plt.xlabel('Season')
    plt.ylabel('Average Energy')
    plt.title('Energy Levels Over Seasons')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_pie_chart(container: DataContainer, title: str):
    data = container.get_pie_chart_data()
    labels = ['Reproduction', 'Death', 'Survival']
    sizes = [data['reproduction'], data['death'], data['survival']]
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title(f'{title} - Reproduction, Death, Survival')
    plt.show()


def normalize_data(data):
    min_val = np.min(data)
    max_val = np.max(data)
    return (data - min_val) / (max_val - min_val)


# def plot_gene_averages(containers: dict):
#     plt.figure(figsize=(10, 6))
#
#     # Iterate over each container and calculate the average of each gene
#     for i, container in enumerate(containers.values()):
#         # Normalize each gene before plotting
#         food_seeking = normalize_data(np.array(container.gene_count["food_seeking"]))
#         strength = normalize_data(np.array(container.gene_count["strength"]))
#         mating_score = normalize_data(np.array(container.gene_count["mating_score"]))
#         mating_focus = normalize_data(np.array(container.gene_count["mating_focus"]))
#
#         plt.plot(food_seeking, label=f'Food Seeking (Season {i})', alpha=0.7)
#         plt.plot(strength, label=f'Strength (Season {i})', alpha=0.7)
#         plt.plot(mating_score, label=f'Mating Score (Season {i})', alpha=0.7)
#         plt.plot(mating_focus, label=f'Mating Focus (Season {i})', alpha=0.7)
#
#     plt.xlabel('Generation')
#     plt.ylabel('Gene Value (Normalized)')
#     plt.title('Gene Averages Over Seasons (Normalized)')
#     plt.legend(loc='upper right')
#     plt.grid(True)
#     plt.show()

def plot_gene_averages(containers: dict):
    # Initialize lists to store average values for each gene across all seasons
    food_seeking_avg = []
    strength_avg = []
    mating_score_avg = []
    mating_focus_avg = []

    # Iterate over each container and calculate the average of each gene for the season
    for container in containers.values():
        # Calculate the average value for each gene
        food_seeking_avg.append(np.mean(container.gene_count["food_seeking"]))
        strength_avg.append(np.mean(container.gene_count["strength"]))
        mating_score_avg.append(np.mean(container.gene_count["mating_score"]))
        mating_focus_avg.append(np.mean(container.gene_count["mating_focus"]))

    # Plot the averages for each gene across the seasons
    plt.figure(figsize=(10, 6))
    plt.plot(food_seeking_avg, label='Food Seeking', marker='o', linestyle='-', alpha=0.7)
    plt.plot(strength_avg, label='Strength', marker='o', linestyle='-', alpha=0.7)
    plt.plot(mating_score_avg, label='Mating Score', marker='o', linestyle='-', alpha=0.7)
    plt.plot(mating_focus_avg, label='Mating Focus', marker='o', linestyle='-', alpha=0.7)

    plt.xlabel('Season')
    plt.ylabel('Gene Average')
    plt.title('Gene Averages Over Seasons')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


def plot_gene_averages_with_twin_axes(containers: dict):
    # Initialize lists to store average values for each gene across all seasons
    food_seeking_avg = []
    strength_avg = []
    mating_score_avg = []
    mating_focus_avg = []

    # Iterate over each container and calculate the average of each gene for the season
    for container in containers.values():
        # Calculate the average value for each gene
        food_seeking_avg.append(np.mean(container.gene_count["food_seeking"]))
        strength_avg.append(np.mean(container.gene_count["strength"]))
        mating_score_avg.append(np.mean(container.gene_count["mating_score"]))
        mating_focus_avg.append(np.mean(container.gene_count["mating_focus"]))

    # Create the plot
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot food_seeking and mating_focus on the left y-axis (ax1)
    ax1.plot(food_seeking_avg, label='Food Seeking', marker='o', linestyle='-', alpha=0.7, color='blue')
    ax1.plot(mating_focus_avg, label='Mating Focus', marker='o', linestyle='-', alpha=0.7, color='green')

    ax1.set_xlabel('Season')
    ax1.set_ylabel('Gene Average (0 to 1)', color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    # Create a second y-axis to plot strength and mating_score (right side)
    ax2 = ax1.twinx()
    ax2.plot(strength_avg, label='Strength', marker='o', linestyle='-', alpha=0.7, color='red')
    ax2.plot(mating_score_avg, label='Mating Score', marker='o', linestyle='-', alpha=0.7, color='orange')

    ax2.set_ylabel('Gene Average (1 to 20)', color='black')
    ax2.tick_params(axis='y', labelcolor='black')

    # Move the legends outside the plot
    ax1.legend(loc='upper left', bbox_to_anchor=(0.0, 1.15))
    ax2.legend(loc='upper left', bbox_to_anchor=(0.8, 1.15))

    # Title and grid
    plt.title('Gene Averages Over Seasons')
    plt.grid(True)

    # Adjust the layout to prevent clipping
    plt.tight_layout()

    # Show the plot
    plt.show()

def plot_gene_cdf(containers: dict, gene_name: str):
    # Plot CDF for each season's gene data
    plt.figure(figsize=(10, 6))

    for season, container in containers.items():
        data = container.gene_count[gene_name]
        data_sorted = np.sort(data)
        cdf = np.arange(1, len(data) + 1) / len(data)
        plt.plot(data_sorted, cdf, label=f'Season {season}')

    plt.title(f'{gene_name} CDF Across Seasons')
    plt.xlabel(gene_name)
    plt.ylabel('CDF')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_gene_kde(containers: dict, gene_name: str):
    # Prepare data for KDE plot
    data = [container.gene_count[gene_name] for container in containers.values()]

    # Plot KDE for each season
    plt.figure(figsize=(10, 6))
    for season_data in data:
        sns.kdeplot(season_data, fill=True, label=f'Season {data.index(season_data)}')

    plt.title(f'{gene_name} Distribution Across Seasons')
    plt.xlabel(gene_name)
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_reproduction_and_death(containers: dict):
    seasons = [f"S-{i+1}" for i in range(len(containers))]
    reproduce_counts = [container.reproduce_count for container in containers.values()]
    death_counts = [container.death_count for container in containers.values()]

    # Set up the figure and axis
    fig, ax = plt.subplots(figsize=(10, 6))

    # Bar plot for reproduction and death counts
    bar_width = 0.35
    index = range(len(seasons))

    # Plot reproduction and death counts as bar charts
    bar1 = ax.bar(index, reproduce_counts, bar_width, label='Reproduced', color='green')
    bar2 = ax.bar([i + bar_width for i in index], death_counts, bar_width, label='Died', color='red')

    # Set labels and title
    ax.set_xlabel('Season')
    ax.set_ylabel('Count')
    ax.set_title('Eaters Reproduced and Died per Season')
    ax.set_xticks([i + bar_width / 2 for i in index])
    ax.set_xticklabels(seasons)
    ax.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()



def plot_reproduction_and_death_trends(containers: dict):
    seasons = [f"S-{i+1}" for i in range(len(containers))]
    reproduce_counts = [container.reproduce_count for container in containers.values()]
    death_counts = [container.death_count for container in containers.values()]

    # Line plot for reproduction and death counts
    plt.figure(figsize=(10, 6))

    plt.plot(seasons, reproduce_counts, label='Reproduced', marker='o', color='green')
    plt.plot(seasons, death_counts, label='Died', marker='x', color='red')

    # Set labels and title
    plt.xlabel('Season')
    plt.ylabel('Count')
    plt.title('Eaters Reproduction and Death Trends Across Seasons')
    plt.legend()

    # Display the plot
    plt.tight_layout()
    plt.show()

def main():
    plot_size: int = 100
    plot = setup_plot(plot_size, 100, 50)
    # display_image(plot)

    containers = dict()


    # simulate the seasons
    for i in range(20):

        # if no eaters left then break
        if len(plot.eaters) < 1:
            break

        # simulate a season
        sim_season(plot, 100, False)
        print("SIMULATED SEASON: " + str(i))
        # display_plot(plot)
        # get data from the end of the season
        container = DataContainer()
        container.update_eaters(plot.eaters)
        container.update_plants(plot.plants)
        container.update_energy_levels(plot.eaters)


        container.update_mated_list(plot)
        container.update_dead_eaters(plot.dead_eaters)
        plot.clear_mated_list()
        plot.clear_dead_list()
        containers[f"container_{i}"] = container
    display_image(plot)

    plot_gene_averages_with_twin_axes(containers)
    plot_reproduction_and_death_trends(containers)
    plot_gene_kde(containers, "food_seeking")
    plot_gene_kde(containers, "mating_focus")
    plot_gene_kde(containers, "mating_score")
    plot_gene_kde(containers, "strength")
    plot_energy_levels(containers)


if __name__ == "__main__":
    main()
