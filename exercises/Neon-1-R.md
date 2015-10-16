---
layout: exercise
title: NEON
subtitle: NEON Database
language: R
---

The [National Ecological Observatory Network](http://www.neoninc.org) has entered into the construction 
phase of development and they are already making their [data available](ttp://data.neoninc.org)! NEON 
collects ecological and environmental data for representative regions of the United States at local to continental scales, including, *of course!*, small mammal 
[box trapping](https://en.wikipedia.org/wiki/Sherman_trap).   

Download NEON's the existing [small mammal data]({{ site.baseurl }}/data/ordway_mammals.sqlite) from 
[Ordway-Swisher Biological Station](http://ordway-swisher.ufl.edu/). 

1. Connect to the database and familiarize yourself with its tables and structure.

2. Write a query to determine the total number of traps that have been disturbed 
at each plot. Plot a histogram of the results.

3. Determine the average hind foot length and weight of each species collected 
for each National Landcover Database (`nlcd`) class. Plot the average weight of all species with weight measurements from the woody wetlands.