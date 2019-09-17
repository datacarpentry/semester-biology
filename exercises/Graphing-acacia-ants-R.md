---
layout: exercise
topic: Graphing
title: Acacia and Ants
language: R
---

An experiment in Kenya has been exploring the influence of large herbivores on plants.

Download the data on [Acacia for the
experiment](http://www.esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt)
into a `data` subdirectory and read it into R using the following command:

```r
acacia <- read.csv("data/ACACIA_DREPANOLOBIUM_SURVEY.txt", sep="\t", na.strings = c("dead"))
```

1. Make a scatter plot with `CIRC` on the x axis and `AXIS1` (the maximum canopy
   width) on the y axis. Label the x axis "Circumference" and the y axis "Canopy
   Diameter".
2. The same plot as (1), but with points colored based on the `ANT` column (the species of ant symbiont living with the acacia)
3. The same plot as (2), but instead of different colors show different species of ant (values of `ANT`) each in a separate subplot.
4. The same plot as (3) but including a simple model by adding `geom_smooth`.
