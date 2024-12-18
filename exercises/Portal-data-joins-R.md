---
layout: exercise
topic: dplyr
title: Portal Data Joins
language: R
---

If [surveys.csv](https://ndownloader.figshare.com/files/2292172), [species.csv](https://ndownloader.figshare.com/files/3299483), and [plots.csv](https://ndownloader.figshare.com/files/3299474) are not available in your workspace download them:

Load them into R using `read_csv()`.

1. Use `inner_join()` to create a table that contains the information from both
   the `surveys` table and the `species` table.
2. Use `inner_join()` twice to create a table that contains the information from
   all three tables.
3. Use `inner_join()` and `filter()` to get a data frame with the information
   from the `surveys` and `plots` tables where the `plot_type` is `Control`.
