---
layout: exercise
topic: Scientific
title: Tree Biomass Challenge
language: R
---

Understanding the total amount of biomass (the total mass of all individuals) in 
forests is important for understanding the global carbon budget and how the 
earth will respond to increases in carbon dioxide emissions.

We don't normally measure the mass of a tree, but take a measurement of the
diameter or circumference of the trunk and then estimate mass using equations
like M = 0.124 * D<sup>2.53</sup>.

1\. Estimate tree biomass for each species in a 96 hectare area of the Western Ghats
in India using the following steps.

  * [Download the data]({{ site.baseurl }}/data/Ramesh2010-macroplots.csv) and
    load the data into R.
  * Write a function that takes a vector of tree diameters as an argument and   
    returns a vector  of tree masses. (Thanks to vector math this function is
    basically just the equation above).
  * Create a `dplyr` pipeline that
    * Adds a new column (using `mutate` and your function) that contains masses
      calculated from the diameters
    * Groups the data frame into species using the `SpCode` column
    * And then calculates biomass (i.e., the `sum` of the masses) for each species
      (using `summarize`)
    * Stores the result as a data frame
  * Display the resulting data frame

2\. Plot a histogram of the species biomass values you just calculated.

  * Use 10 bins in the histogram (using the `bins` argument)
  * Use a log10 scale for the x axis (using `scale_x_log10`)
  * Change the x axis label to `Biomass` and the y axis label to `Number of Species` (using `labs`)