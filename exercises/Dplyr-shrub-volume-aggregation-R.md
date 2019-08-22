---
layout: exercise
topic: dplyr
title: Shrub Volume Aggregation
language: R
---

This is a follow-up to [Shrub Volume Data Basics]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).

Dr. Granger wants some summary data of the plants at her sites and for her
experiments. Make sure you have her [shrub dimensions data]({{ site.baseurl }}/data/shrub-volume-data.csv).

This code calculates the average height of a plant at each site:

```r
shrub_dims <- read.csv('data/shrub-volume-data.csv')
by_site <- group_by(shrub_dims, site)
avg_height <- summarize(by_site, avg_height = mean(height))
```

1. Modify the code to calculate and print the average height of a plant in each
   experiment.
2. Use `max()` to determine the maximum height of a plant at each site.
