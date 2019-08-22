---
layout: exercise
topic: Vectors
title: Shrub Volume Vectors
language: R
---

You have data on the length, width, and height of 10 individuals of the yew
[*Taxus baccata*](https://en.wikipedia.org/wiki/Taxus_baccata) stored in the
following vectors:

```
length <- c(2.2, 2.1, 2.7, 3.0, 3.1, 2.5, 1.9, 1.1, 3.5, 2.9)
width <- c(1.3, 2.2, 1.5, 4.5, 3.1, NA, 1.8, 0.5, 2.0, 2.7)
height <- c(9.6, 7.6, 2.2, 1.5, 4.0, 3.0, 4.5, 2.3, 7.5, 3.2)
```

Copy these vectors into an R script and then determine the following:

1. The volume of each shrub (i.e., the length times the width times the height).
   *storing this in a variable will make some of the next problems easier*
2. The total volume of all of the shrubs.
3. A vector of the height of shrubs with lengths greater than 2.5.
4. A vector of the height of shrubs with heights greater than 5.
5. A vector of the heights of the first 5 shrubs.
6. A vector of the volumes of the first 3 shrubs.

*Challenge*: A vector of the volumes of the last 5 shrubs with the code written
so that it will return the last 5 values regardless of the length of the vector (i.e., it will give the last 5 values if their are 10, 20, or 50 individuals).