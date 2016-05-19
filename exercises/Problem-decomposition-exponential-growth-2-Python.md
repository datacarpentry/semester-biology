---
layout: exercise
topic: Problem Decomposition
title: Exponential Growth 2
language: Python
---

One of you lab mates (you may remember them from the For Loops 2
problem) is busy working on insect population dynamics. Initial results
suggested that exponential growth was too simplistic for understanding
the observed dynamics, so now they need to look at logistic growth.
Logistic growth is a lot like exponential growth except that it slows
down as the population grows large and eventually asymptotes at a
carrying capacity. The basic recursive equation is:

`N(t+1)~ = N(t) + r * N(t) * ((K – N(t)) / K)`

N(t) is the abundance at a given time step, r is the reproductive rate,
and K is the carrying capacity (you can learn a bit more about logistic
population growth
[here](http://en.wikipedia.org/wiki/Logistic_function#In_ecology:_modeling_population_growth)).
Since we can't have partial individuals in the real world we should
round the calculation in each step up to the nearest integer using the
ceil function in the math module.

Your lab mate has compiled data from literature on the reproductive
rates and carrying capacity for a number of different individuals for a
variety of species. You've been teaching them about database structure
so they have broken the data into two tables: an [individuals
table](http://www.programmingforbiologists.org/sites/programmingforbiologists.org/files/individuals_table.csv)
and [species
table](http://www.programmingforbiologists.org/sites/programmingforbiologists.org/files/species_table.csv).
The database has information on several different taxonomic groups, but
for this project your lab mate is only interested in the data for the
insects.

Using the average reproductive rate and carrying capacity for each
insect species determine the time it takes for the species to reach
equilibrium (i.e., carrying capacity) when starting with an initial
population size of 10. Once you've determined the value for each
species, plot the time to equilibrium as a function of the reproductive
rate and (on a separate graph) the carrying capacity.

You can either break this problem down into manageable parts yourself
(you can use the [problem decomposition
steps](http://www.programmingforbiologists.org/problem-decomposition-steps)
to help) or follow [this
approach](http://www.programmingforbiologists.org/problem-decomposition-problem-decomposition).
Turn in the Python code and (if you use one) a database file with any
queries that you use.
