---
layout: exercise
topic: dplyr
title: Shrub Volume Join
language: R
---

Dr. Morales has data in three tables in the files:

a. [`shrub-volume-data.csv`]({{ site.baseurl }}/data/shrub-volume-data.csv) with data on shrub dimensions
b. [`shrub-volume-experiments.csv`]({{ site.baseurl }}/data/shrub-volume-experiments.csv) with data on experimental manipulations
c. [`shrub-volume-sites.csv`]({{ site.baseurl }}/data/shrub-volume-sites.csv) with data on different sites

If the files aren't available in your work space use the links above to download them.
Load the data using `read_csv`.

1. Use `inner_join` to combine the experiments data with the shrub volume data.
2. Combine the sites data with both the data on shrub volume and the data on experiments to produce a single data frame that contains all of the data.
