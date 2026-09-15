---
layout: exercise
topic: dplyr
title: Penguins Data Aggregation
language: R
---

If the file [`penguins.csv`]({{ site.baseurl }}/data/penguins.csv) is not already in your working directory then download it into your working directory.

Load `penguins.csv` into R using `read_csv()`.

1. Use the `group_by()` and `summarize()` functions to get a count of the number
   of individuals in each species.
2. Use the `drop_na()`, `group_by()`, and `summarize()` functions to calculate the average `bill_length_mm` for each species.
3. Use the `drop_na()`, `group_by()`, and `summarize()` functions to calculate the maximum `flipper_length_mm` for each species on each island.
4. Use the `filter()`, `drop_na()`, `group_by()`, and `summarize()` functions to get the mean
   body mass of Chinstrap penguins on each island.
5. Find the mean bill ratio (bill length / bill depth) for each species on each island.
