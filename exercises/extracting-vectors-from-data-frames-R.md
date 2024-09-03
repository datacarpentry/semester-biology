---
layout: exercise
topic: dplyr
title: Extracting vectors from data frames
language: R
---

Using the Portal data `surveys` table ([download a copy](https://ndownloader.figshare.com/files/2292172) if it's not in your working directory):

1. Use `$` to extract the `weight` column into a vector
2. Use `[]` to extract the `month` column into a vector
3. Extract the `hindfoot_length` column into a vector using `pull()` and use this vector to calculate the mean hindfoot length ignoring null values