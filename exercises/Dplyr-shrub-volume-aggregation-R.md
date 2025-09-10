---
layout: exercise
topic: dplyr
title: Shrub Volume Aggregation
language: R
---

Dr. Morales wants some summary data of the plants at her sites and for her experiments.
If the file [shrub-volume-data.csv]({{ site.baseurl }}/data/shrub-volume-data.csv) is not already in your work space download it.
Load the data using `read_csv`.

1. Use `drop_na`, `group_by` and `summarize` to calculate and print the **average height** of a plant in each **experiment**, while ignoring plants that have a height of `NA` when calculating the average.
2. Use `drop_na`, `group_by` and `summarize` to determine the **maximum height** of a plant at each **site**, while ignoring plants that have a height of `NA` when calculating the maximum.
3. Use `mutate`, `drop_na`, `group_by` and `summarize` to determine the **average volume** (volume = length \* width \* height) of a plant in each **site**, while ignoring plants that have volumes of `NA` when calculating the average.
4. Use `mutate`, `drop_na`, `group_by` and `summarize` to determine both the **average volume** and the **number of plants** in each **experiment**, while ignoring plants that have volumes of `NA` when calculating the average and when counting plants.
