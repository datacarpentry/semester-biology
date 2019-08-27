---
layout: exercise
topic: dplyr
title: Portal Data Manipulation Pipes
language: R
---

Download a copy of the
[Portal Teaching Database surveys table](https://ndownloader.figshare.com/files/2292172)
and load it into R using `read.csv()`.

Use pipes (`%>%`) to combine the following operations to manipulate the data.

1. Use `mutate()`, `select()`, and `na.omit()` to create a new data frame with
   the `year`, `species_id`, and weight **in kilograms** of each individual,
   with no null weights.
2. Use the `filter()` and `select()` to get the `year`, `month`, `day`, and
   `species_id` columns for all of the rows in the data frame where `species_id`
   is `SH`.
3. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species ID.
4. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species ID in each year.
5. Use the `filter()`, `group_by()`, and `summarize()` functions to get the mean
   mass of species `DO` in each year.