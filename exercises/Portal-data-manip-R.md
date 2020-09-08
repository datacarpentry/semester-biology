---
layout: exercise
topic: dplyr
title: Portal Data Manipulation
language: R
---

Download a copy of the
[Portal Teaching Database surveys table](https://ndownloader.figshare.com/files/2292172) (*If you are using RStudio Cloud in a class it may have already been added to your workspace for you*)
and load it into R using `read.csv()`.

***Do not use pipes for this exercise.***

1. Use `select()` to create a new data frame with just the `year`, `month`,
   `day`, and `species_id` columns in that order.
2. Use `mutate()`, `select()`, and `filter()` with `!is.na()` to create a new
   data frame with
   the `year`, `species_id`, and weight **in kilograms** of each individual,
   with no null weights. The weight in the table is given in grams so you will
   need to create a new column for weight in kilograms by dividing the weight column by 1000.
3. Use the `filter()` function to get all of the rows in the data frame for the
   species ID `SH`.
