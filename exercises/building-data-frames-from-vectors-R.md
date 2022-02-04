---
layout: exercise
topic: dplyr
title: Building data frames from vectors
language: R
---

You have data on the length, width, and height of 10 individuals of the yew *Taxus baccata* stored in the following vectors:

```r
length <- c(2.2, 2.1, 2.7, 3.0, 3.1, 2.5, 1.9, 1.1, 3.5, 2.9)
width <- c(1.3, 2.2, 1.5, 4.5, 3.1, NA, 1.8, 0.5, 2.0, 2.7)
height <- c(9.6, 7.6, 2.2, 1.5, 4.0, 3.0, 4.5, 2.3, 7.5, 3.2)
```

Make a data frame that contains these three vectors as columns along with a `genus` column containing the name *Taxus* on all rows and a `species` column containing the word *baccata* on all rows.
