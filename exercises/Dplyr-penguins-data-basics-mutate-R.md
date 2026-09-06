---
layout: exercise
topic: dplyr
title: Penguin Data Basics Mutate
language: R
---

If the file [`penguins.csv`]({{ site.baseurl }}/data/penguins.csv) is not already in your working directory then download it into your working directory.

Load the data using `read_csv()` and use `dplyr` to complete the following tasks.

1. Add a new column named `bill_ratio` containing the ratio of the penguin's bill length to its bill depth (bill length / bill depth).
2. Sort the data by body mass.
