---
layout: exercise
topic: dplyr
title: Shrub Volume Join
language: R
---

This is a follow-up to [Shrub Volume Aggregation]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-aggregation-R).

In addition to the main data table on shrub dimensions, Dr. Granger has two additional data tables.
The first describes the manipulation for each experiment.
The second provides information about the different sites.
Check if the files `shrub-volume-experiments.csv` and `shrub-volume-sites.csv` are in your work space (your instructor may have already added them).
If not download the [experiments data]({{ site.baseurl }}/data/shrub-volume-experiments.csv) and the [sites data]({{ site.baseurl }}/data/shrub-volume-sites.csv).

1. Import the experiments data and then use `inner_join` to combine it with the shrub dimensions data to add a `manipulation` column to the shrub data.
2. Import the sites data and then combine it with both the data on shrub dimensions and the data on experiments to produce a single data frame that contains all of the data.
