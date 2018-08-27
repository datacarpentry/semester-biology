---
layout: exercise
topic: dplyr
title: Portal Data Joins
language: R
---

Download copies of the following Portal Teaching Database tables:

* [surveys](https://ndownloader.figshare.com/files/2292172)
* [species](https://ndownloader.figshare.com/files/3299483)
* [plots](https://ndownloader.figshare.com/files/3299474)

Load them into R using `read.csv()`.

1. Use `inner_join()` to create a table that contains the information from both
   the `surveys` table and the `species` table.
2. Use `inner_join()` twice to create a table that contains the information from
   all three tables.
3. Use `inner_join()` and `filter()` to get a data frame with the information
   from the `surveys` and `plots` tables where the `plot_type` is `Control`.
4. We want to do an analysis comparing the size of individuals on the `Control`
   plots to the `Long-term Krat Exclosures`. Create a data frame with the
   `year`, `genus`, `species`, `weight` and `plot_type` for all cases where the
   plot type is either `Control` or `Long-term Krat Exclosure`. Only include
   cases where `Taxa` is `Rodent`. Remove any records where the `weight` is
   missing.