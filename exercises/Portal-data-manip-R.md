---
layout: exercise
topic: dplyr
title: Portal Data Manipulation
language: R
---

Download a copy of the
[Portal Teaching Database surveys table](https://ndownloader.figshare.com/files/2292172)
and load it into R using `read.csv()`.

***Do not use pipes for this exercise.***

1. Use `select()` to create a new data frame with just the `year`, `month`,
   `day`, and `species_id` columns in that order.
2. Use `mutate()`, `select()`, and `na.omit()` to create a new data frame with
   the `year`, `species_id`, and weight **in kilograms** of each individual,
   with no null weights. The weight in the table is given in grams so you will
   need to divide it by 1000.
3. Use the `filter()` function to get all of the rows in the data frame for the
   species ID `SH`.
4. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species ID.
5. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species ID in each year.
6. Use the `filter()`, `group_by()`, and `summarize()` functions to get the mean
   mass of species `DO` in each year.