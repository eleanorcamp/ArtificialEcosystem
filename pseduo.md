Problem statement:

Simulate some version of a simple artificial ecosystem. As an example:

Artificial life simulation 
Everything takes place in a 100 meter by 100 meter square

Laws of physics: each season enough sunlight falls for exactly 100 new 
plants to grow, randomly distributed.

There is space for 1000 eaters. An eater coming within 2 m of a plant eats 
it all and gets 100 cal of energy. The most an eater can store is 200 cal. 
It takes 1 cal to move 2 m and 20 to have an offspring. 
Eaters live at most 20 seasons.

Invent a 4 gene eater in which the genes code for movement and reproduction
control. 
Simulate 100 time periods per season. 
In one time period an eater can move and eat or reproduce.


Questions from problem statement:
1) Do all plants grow at start of season, or randomly throughout the season?
2) Do eaters need to be near another eater to reproduce?
3) What should these 4 genes actually look like?
4) Do eaters move randomly? Or towards food source?
5) What happens when two+ eaters get to the same plant?



What we'll need:

    Eater class
        - 4 genes
            1. dictates movement
            2. dictates reproduction
            3. not sure yet
            4. not sure yet
        - energy 'meter'
        - age count

        for my intrigue:
            - total plants eaten
            - total distance moved
            - direct number of offspring (kids but not grand-kids)

    Plant class
        - age ?


    Plot class (the actual 100x100 m square)
        - list of all eaters and their locations
        - list of all plants and their locations

        function to limit number of eaters (problem states there is room for 1000)


    Function to make new plants every season
        new_plants():
            get points where new plants *can* grow
            grow 100 **new** pants in the available points


    Overarching simulate 100 time periods
        sim_season():
            for i in range(100):
                sim_period

    Simulation of a single time period
        sim_period():
            go through Plot's list of eaters:
                pick whether to move or reproduce
                adjust eater/plant list accordingly

    Metrics to keep track of
    - Average eater health at end of season
    - Number of plants remaining 
    - Population changes over time
