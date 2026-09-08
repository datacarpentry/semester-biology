---
layout: exercise
topic: dplyr
title: Shrub Volume Data Basics Filter NA
language: R
---

Dr. Morales is interested in studying the factors controlling the size and
carbon storage of shrubs. She has conducted an experiment looking at the effect
of three different treatments on shrub volume at four different locations. She
has placed the data file on the web for you to download:

If the file [`shrub-volume-data.csv`]({{ site.baseurl }}/data/shrub-volume-data.csv) is not already in your working directory (it probably is if you're taking this class using Posit Cloud) then download it into your working directory.

Get familiar with the data by importing it using `read_csv()` and use `dplyr` to complete the following tasks.

1. Remove rows with null values in the `height` column (using `drop_na`).
2. Remove rows with null values in the `height` and `width` columns (using `drop_na`).
