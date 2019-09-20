---
layout: exercise
topic: Graphing
title: Acacia and Ants Data Manipulation
language: R
---

An experiment in Kenya has been exploring the influence of large herbivores on plants.

Download the data on [Trees for the
experiment](http://www.esapubs.org/archive/ecol/E095/064/TREE_SURVEYS.txt)
into a `data` subdirectory. There are a number of problematic entries in this data so use the `readr` package to import it:

```r
library(readr)
trees <- read_tsv("data/TREE_SURVEYS.txt")
```

1. Add a new column to the `trees` data frame named `canopy_area` that contains
   the estimated canopy area calculated as the value in the `AXIS_1` column
   times the value in the `AXIS_2` column. Print out the `SURVEY`, `YEAR`,
   `SITE`, and `canopy_area` columns from data frame.
2. Make a scatter plot with `canopy_area` on the x axis and `HEIGHT` on the y
   axis. Color the points by `TREATMENT` and plot the points for each value in
   the `SPECIES` column in a separate subplot. Label the x axis "Canopy Area
   (m)" and the y axis "Height (m)". Make the point size 2.
3. That's a big outlier in the plot from (2). 50 by 50 meters is a little too
   big for a real Acacia, so filter the data to remove any values for `AXIS_1`
   and `AXIS_2` that are over 20 and update the data frame. Then remake the graph.
4. Find out how the abundance of each species has been changing through time.
   Use `group_by`, `summarize`, and `n` to make a data frame with `YEAR`,
   `SPECIES`, and an `abundance` column that has the number of individuals in
   each species in each year. Print out this data frame.
5. Make a line plot with points (by using `geom_line` in addition to
   `geom_point`) with `YEAR` on the x axis and `abundance` on the y axis with
   one subplot per species. To let you seen each trend clearly let the scale for
   the y axis vary among plots by adding `scales = "free_y"` as an optional argument to `facet_wrap`.
