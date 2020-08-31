---

layout: exercise
topic: dplyr
title: Portal Data Aggregation
language: R
---

Download a copy of the
[Portal Teaching Database surveys table](https://ndownloader.figshare.com/files/2292172)
and load it into R using `read.csv()`.

1. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species ID.
2. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species ID in each year.
3. Use the `filter()`, `group_by()`, and `summarize()` functions to get the mean
   mass of species `DO` in each year.