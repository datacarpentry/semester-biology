---
layout: exercise
topic: Graphing
title: Graphing Data From Multiple Tables
language: R
---

An experiment in Kenya has been exploring the influence of large herbivores on plants.

Check to see if `ACACIA_DREPANOLOBIUM_SURVEY.txt` and `TREE_SURVEYS.txt` is in your workspace.
If not, download [`ACACIA_DREPANOLOBIUM_SURVEY.txt`](https://esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt) and [`TREE_SURVEYS.txt`](https://ndownloader.figshare.com/files/5629536)
Install the `readr` package and use `read_tsv` to read in the data using the following commands:

```r
library(readr)
acacia <- read_tsv("ACACIA_DREPANOLOBIUM_SURVEY.txt",
                   na = c("dead"))
trees <- read_tsv("TREE_SURVEYS.txt",
                  col_types = list(HEIGHT = col_double(),
                                   AXIS_2 = col_double()))
```

We want to compare the circumference to height relationship in acacia on different treatments in the context of the same relationship for trees in the region. These data are stored in the two tables above. Make a graph with the relationship between `CIRC` and `HEIGHT` for the trees as gray points in the background and the same relationship for acacia as red points plotted on top of the tree points. There should be one subplot for each treatment. Include linear models for both sets of data. Provide clear labels for the axes.