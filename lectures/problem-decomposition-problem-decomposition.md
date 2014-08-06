--- layout: post title: Problem Decomposition Problem Decomposition
created: 1320086761 categories: [] ---

### Data {style="margin-bottom: 0in;"}

1.  Download the tables holding the data on reproductive rates and
    carrying capacities
2.  Create a database of these values
3.  Write a query to get the average reproductive rate, carrying
    capacity, and starting population size for each **insect** species
4.  Export the results of this query to a csv file
5.  Import to Python

### Code {style="margin-bottom: 0in;"}

1.  Write a logistic\_growth\_next\_step() function that returns the
    value of N~t+1~ given the values for N~t~, r, and K)
2.  Write a logistic\_growth\_time\_to\_equil() function that returns
    the time it takes to reach an equilibrium (or K)
3.  Write a series of commands to loop over the parameter values for
    each species using logistic\_growth\_time\_to\_equil() to determine
    the time to equilibrium for each species. Store these values, along
    the the values of r and K used to generate them in a list of lists
    as you loop over the species.
4.  Plot the time to equilibrium as a function of reproductive rate and
    carrying capacity.

