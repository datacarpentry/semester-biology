---
layout: exercise
topic: Reproduction
title: Climate Space
language: R
---

Figuring out how particular factors influence species distribution can be aided by determining which areas of the available climate space they currently occupy. To do so, you're interested in showing how much and what part of the available global temperature and precipitation range is occupied by several common tree species. 

1. Create a scatterplot of global mean annual temperature and mean annual precipitation. Get these data from the [WorldClim dataset](http://worldclim.org/version2) using `getData`, setting the resolution to 10 minutes and the variable to bio. You need only two of the 19 bioclim variables in a single dataframe, and will want to plot a random subset of 10,000 points (see `sample_n`) to limit the time it takes to generate. Choose good labels and make the points transparent to see their density. Why are the temperature values so large? Storing decimal values uses more space than integers, so the WorldClim creators provide temperature values multiplied by 10. For example, 19.5 is stored as 195. Display temperature on the plot correctly. See more information about WorldClim units [here](http://www.worldclim.org/formats1). 

2. Plot the temperature-precipitation value for each of 1,000 occurrences onto this climate space for the following species: *Quercus alba*, *Picea glauca*, and *Ceiba pentandra*. Get a dataframe for each of the three species' occurrences from GBIF using `spocc`, then look up the corresponding climate values for each occurrence. In order to get climate values, the occurrences dataframe must contain only longitude and latitude columns. 
