---
layout: exercise
topic: Graphing
title: Acacia and Ants
language: R
---

An experiment in Kenya has been exploring the influence of large herbivores on plants.

If [`ACACIA_DREPANOLOBIUM_SURVEY.txt`](https://esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt) is not in your workspace download it.
Read it into R using the following command:

```r
acacia <- read_tsv("ACACIA_DREPANOLOBIUM_SURVEY.txt", na = c("dead"))
```

1. Make a scatter plot with `CIRC` on the x axis and `AXIS1` (the maximum canopy
   width) on the y axis. Label the x axis "Circumference" and the y axis "Canopy
   Diameter".
2. Make a scatter plot with `AXIS1` on the x axis and `AXIS2` on the y axis
   (the two measurements of canopy diameter). Set the point `size` to 2 and
   `color` to `"darkgreen"`. Label the x axis "Canopy Diameter Axis 1" and the
   y axis "Canopy Diameter Axis 2".
3. Look at the relationship between `AXIS1` and `AXIS2` on only the full herbivore
   exclosures by: filtering the data so that it only contains the plots "S1TOTAL",
   "S2TOTAL", and "S3TOTAL", using `drop_na()` to remove rows where either `AXIS1`
   or `AXIS2` are `NA`, and making a scatter plot of this filtered data with `AXIS1`
   on the x axis and `AXIS2` on the y axis. Label the x axis "Canopy Diameter Axis 1" and the
   y axis "Canopy Diameter Axis 2".
