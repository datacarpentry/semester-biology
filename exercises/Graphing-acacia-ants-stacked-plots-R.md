---
layout: exercise
topic: Graphing
title: Acacia and Ants Stacked Plots
language: R
---

An experiment in Kenya has been exploring the influence of large herbivores on plants.

If [`ACACIA_DREPANOLOBIUM_SURVEY.txt`](https://esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt) is not in your workspace download it.
Read it into R using the following command:

```r
acacia <- read_tsv("ACACIA_DREPANOLOBIUM_SURVEY.txt", na = c("dead"))
```

1. Make a **non-stacked** histogram of the height of acacia (using the `HEIGHT` column) colored by the `TREATMENT`.
   Set the transparency (using `alpha`) to 0.5 so that you can see all of the bars.
   Label the x-axis "Height (m)" and the y-axis "Count of Acacia".
   Set the binwidth to 0.5.
2. Make a **non-stacked** histogram of the circumference of acacia (using the `CIRC` column) colored by the `ANT` column.
   Set the transparency (using `alpha`) to 0.5 so that you can see all of the bars.
   Label the x-axis "Circumference (cm)" and the y-axis "Count of Acacia".
   Set the binwidth to 5.
