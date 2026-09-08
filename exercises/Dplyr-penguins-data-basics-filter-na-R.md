---
layout: exercise
topic: dplyr
title: Penguin Data Basics Filter NA
language: R
---

If the file [`penguins.csv`]({{ site.baseurl }}/data/penguins.csv) is not already in your working directory then download it into your working directory.

Load the data using `read_csv()` and use `dplyr` to complete the following tasks.

1. Remove rows with null values in the `body_mass_g` column.
2. Remove rows with null values in the `sex` column.
3. Create a new data frame called `penguin_masses` that includes all of the original data with no null body masses and a new column containing the body mass in kilograms (body mass in grams / 1000).
