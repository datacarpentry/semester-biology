---
layout: exercise
topic: Reproduction
title: Climate Space
language: R
---

You're interested in determining how much and what part of the available global temperature and precipitation range is occupied by several common tree species. 

1. Create a scatterplot of global mean annual temperature and mean annual precipitation. Get these data from the [WorldClim dataset](http://worldclim.org/version2) using `getData`, setting the resolution to 10 minutes and the variable to bio. You need only two of the 19 bioclim variables in a single dataframe, and will want to plot a random subset of 10,000 points (see `sample_n`) to limit the time it takes to generate. Choose good labels and make the points transparent to see their density. Why are the climate values so large? 

2. Plot the temperature-precipitation value for each of 1,000 occurrences onto this climate space for the following species: Quercus alba, Picea glauca, and Ceiba pentandra. Get a dataframe for each of the three species' occurrences from GBIF using `spocc`. Then look up the corresponding climate values for each occurrence. In order to plot the occurrences for all species, they will need to be combined into a single dataframe, with an additional column for species (hint: think about how to name and subset columns of each dataframe before combining). 
