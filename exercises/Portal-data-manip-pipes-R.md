---
layout: exercise
topic: dplyr
title: Portal Data Manipulation Pipes
language: R
---

If the file [`surveys.csv`](https://ndownloader.figshare.com/files/2292172) is not already in your working directory then download a copy.

Load the file into R using `read_csv()`.

Use pipes (`|>`) to combine the following operations to manipulate the data.

1. Use `select()` and `arrange()` to create a new data frame with just the `year`, `month`,
   `day`, `species_id`, and `plot_id` columns with the rows sorted by `species_id`.
2. Use `mutate()`, `select()`, and `drop_na()` to create a new
   data frame with
   the `year`, `species_id`, and `hindfoot_length` **in cm** of each individual,
   with no null hindfoot lengths. The hindfoot length in the table is given in mm so you will
   need to create a new column for hindfoot length in cm by dividing the `hindfoot_length` column by 10.
3. Use `filter()` and `select()` to get the `year`, `month`, `day`, and `species_id`
   columns for all of the rows in the data frame where species_id is `"OT"`.
4. Use `select()` and `filter()` to produce a data frame with `plot_id`,
   `species_id`, `weight`, and `hindfoot_length`, where the species is `"DM"` or `"DS"`
   and `hindfoot_length` is greater than 35. Exclude NA values for both `weight` and `hindfoot_length`.
