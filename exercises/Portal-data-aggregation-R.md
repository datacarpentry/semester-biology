---

layout: exercise
topic: dplyr
title: Portal Data Aggregation
language: R
---

If the file [shrub-volume-data.csv](https://ndownloader.figshare.com/files/2292172) is not
already in your working directory download it.

Load `shrub-volume-data.csv` into R using `read.csv()`.

1. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species ID.
2. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species ID in each year.
3. Use the `filter()`, `group_by()`, and `summarize()` functions to get the mean
   mass of species `DO` in each year.