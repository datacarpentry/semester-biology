---

layout: exercise
topic: Graphing
title: Acacia and Ants Histograms
language: R
---

An experiment in Kenya has been exploring the influence of large herbivores on plants.

Check to see if `ACACIA_DREPANOLOBIUM_SURVEY.txt` is in your workspace.
If not, [download it](https://esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt).
Read it into R using the following command:

```r
acacia <- read_tsv("data/ACACIA_DREPANOLOBIUM_SURVEY.txt", na = c("dead"))
```

1. Make a bar plot of the number of acacia with each mutualist ant species (using the `ANT` column).
2. Make a histogram of the height of acacia (using the `HEIGHT` column). Label
   the x axis "Height (m)" and the y axis "Number of Acacia".
3. Make a plot that shows histograms of both `AXIS1` and `AXIS2`. Due to the way
   the data is structured you’ll need to add a 2nd geom_histogram() layer that
   specifies a new aesthetic. To make it possible to see both sets of bars
   you’ll need to make them transparent with the optional argument alpha = 0.3.
   Set the color for `AXIS1` to "red" and `AXIS2` to "black" using the `fill`
   argument. Label the x axis "Canopy Diameter(m)" and the y axis "Number of Acacia".
4. Use `facet_wrap()` to make the same plot as (3) but with one subplot for each
   treatment. Set the number of bins in the histogram to 10.