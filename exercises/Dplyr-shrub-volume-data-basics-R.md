---
layout: exercise
topic: dplyr
title: Shrub Volume Data Basics
language: R
---

Dr. Morales is interested in studying the factors controlling the size and
carbon storage of shrubs. She has conducted an experiment looking at the effect
of three different treatments on shrub volume at four different locations. She
has placed the data file on the web for you to download:

If the file [`shrub-volume-data.csv`]({{ site.baseurl }}/data/shrub-volume-data.csv) is not already in your working directory (it probably is if you're taking this class using Posit Cloud) then download it into your working directory.

Get familiar with the data by importing it using `read_csv()` and use `dplyr` to complete the following tasks.

1. Select the data from the length column (using `select`).
2. Select the data from the site and experiment columns (using `select`).
3. Add a new column named `area` containing the area of the shrub, which is the length times the width (using `mutate`).
4. Sort the data by length (using `arrange`).
5. Filter the data to include only plants with heights greater than 5 (using `filter`).
6. Filter the data to include only plants with heights greater than 4 and widths greater than 2 (using `,` or `&` to include two conditions).
7. Filter the data to include only plants from Experiment 1 or Experiment 3 (using `|` for "or").
8. Remove rows with null values in the `height` column (using `drop_na`)
9. Create a new data frame called `shrub_volumes` that includes all of the original data and a new column containing the volumes (length * width * height), and display it.