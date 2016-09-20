---
layout: exercise
topic: dplyr
title: Shrub Volume Join
language: R
---

This is a follow-up to [Shrub Volume Aggregation]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-aggregation-R).

Dr. Granger has kept a separate table that describes the `manipulation` for each
`experiment`. Add the [experiments data]({{ site.baseurl }}/data/shrub-volume-experiments-table.csv)
to your `data` folder.

Import the experiments data and then use `inner_join` to combine it with the
shrub dimensions data to add a `manipulation` column to the shrub data.
