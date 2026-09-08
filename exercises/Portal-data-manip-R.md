---
layout: exercise
topic: dplyr
title: Portal Data Manipulation
language: R
---

If the file [`surveys.csv`](https://ndownloader.figshare.com/files/2292172) is not already in your working directory then download a copy.

Load the file into R using `read_csv()`.

***Do not use pipes for this exercise.***

1. Use `select()` and `arrange()` to create a new data frame with just the `year`, `month`,
   `day`, and `species_id` columns with the rows sorted by `plot_id`.
2. Use `mutate()`, `select()`, and `drop_na()` to create a new
   data frame with
   the `year`, `species_id`, and weight **in kilograms** of each individual,
   with no null weights. The weight in the table is given in grams so you will
   need to create a new column for weight in kilograms by dividing the weight column by 1000.
3. Use `filter()` and `select()` to get the `year`, `month`, `day`, and `species_id`
   columns for all of the rows in the data frame where species_id is SH.
4. Use `select()`, `filter()`, and `arrange()` to produce a data frame with `plot_id`,
   `species_id`, `weight`, and `hindfoot_length`, where the species is `"PB"` or `"PP"`
   and `weight` is less than 40. Exclude NA values for both `weight` and `hindfoot_length`.
