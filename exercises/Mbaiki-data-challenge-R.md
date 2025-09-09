---
layout: exercise
topic: Data Analysis
title: M'Baïki Data Challenge
language: R
---

A long-term study near M’Baïki in the Central African Republic has been monitoring tropical forest recovery from disturbance for 40 years.

Use the data on yearly tree measurements (in [mbaiki_measures.csv]({{ site.baseurl }}/data/mbaiki_measures.csv)), information on the individual trees (in [mbaiki_trees.csv]({{ site.baseurl }}/data/mbaiki_trees.csv)),
and the names of the species in the forest (in [mbaiki_species.csv]({{ site.baseurl }}/data/mbaiki_species.csv)) to answer the following questions (if isn't in your working directory download it).

1. Create a new data frame that contains the following information for each unique tree (each tree has a unique `id_tree`): The `id_tree`, the net growth (total change in diameter from the first year a tree is measured to the last year a tree is measured), the time period of sampling in years (number of years between the first and last measurement), and the growth rate (the net growth divided by the time period of sampling). Only include observations while the tree was alive in these calculations.
2. Starting with the data frame you created in (1) create a new data frame that contains the following information on the average growth rate of trees in each species in each subplot: The ID of the subplot, the scientific name of the species, the mean growth rate of all of the trees of that species in that subplot, and the sample size used to estimate the mean (i.e., the number of trees of that species in that subplot). Make sure the resulting data frame is not grouped.

*Find out more about this dataset by [accessing the full dataset](https://doi.org/10.18167/DVN1/QSATSX) or reading the associated paper:
[Bénédet, F., Gourlet-Fleury, S., Allah-Barem, F. et al. 2024. 40 years of forest dynamics and tree demography in an intact tropical forest at M’Baïki in central Africa. Sci Data 11, 734.](https://doi.org/10.1038/s41597-024-03577-6)*
