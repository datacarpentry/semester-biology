---
layout: exercise
topic: dplyr Databases
title: NEON Mammals
language: R
---

The [National Ecological Observatory Network](http://www.neoninc.org) has entered into the construction phase of development and they are already making their [data available](http://data.neonscience.org/home)! NEON collects ecological and environmental data for representative regions of the United States at local to continental scales, including, *of course!*, small mammal [box trapping](https://en.wikipedia.org/wiki/Sherman_trap). We've retrieved NEON's existing small mammal data from [Ordway-Swisher Biological Station](http://ordway-swisher.ufl.edu/) [[NEON Data Use Policy](http://data.neonscience.org/data-policy)]. 

1. Create a SQLite database called `ordway_mammals.sqlite`. 
2. Download the three data tables ([capture]({{ site.baseurl }}/data/ordway-mammals-capture.csv), [plots]({{ site.baseurl }}/data/ordway-mammals-plots.csv), [traps]({{ site.baseurl }}/data/ordway-mammals-traps.csv)) and import them into the SQLite database. Familiarize yourself with the tables' structure.
3. Write a query to determine the total number of traps that have been disturbed 
at each plot. Plot a histogram of the results.
4. Determine the average hind foot length and weight of each species collected 
for each National Landcover Database class (`nlcdClass`). 
5. Plot the average weight of all species with weight measurements from the woody wetlands.
5. Create a scatter plot of the relationship between the total number of
disturbed traps and the average weight of *Podimus floridanus* for each sampling event (`eventID`).
