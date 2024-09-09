---
layout: exercise
topic: dplyr
title: Portal Data Manipulation Pipes
language: R
---

If the file [`surveys.csv`](https://ndownloader.figshare.com/files/2292172) is not already in your working directory then download a copy.

Load the file into R using `read_csv()`.

Use pipes (either `|>` or `%>%`) to combine the following operations to manipulate the data.

1. Use `mutate()`, `select()`, and `drop_na()` to create a new data frame with
   the `year`, `species_id`, and weight **in kilograms** of each individual,
   with no null weights.
2. Use the `filter()` and `select()` to get the `year`, `month`, `day`, and
   `species_id` columns for all of the rows in the data frame where `species_id`
   is `SH`.
