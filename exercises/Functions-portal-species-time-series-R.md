---
layout: exercise
topic: Functions
title: Portal Species Time-Series
language: R
---

If [surveys.csv](https://ndownloader.figshare.com/files/2292172), [species.csv](https://ndownloader.figshare.com/files/3299483), and [plots.csv](https://ndownloader.figshare.com/files/3299474) are not available in your workspace download them:

Load them into R using `read.csv()`.

Do the following (no output is expected for (1) or (2)):

1. Combine the `surveys` and `species` tables into a single data frame
2. Write a function that
    * Takes three arguments - a data frame (the combined table created in (1)), a `genus` name, and a `species` name
    * Uses `dplyr` to produce a data frame with a two columns: `year` and `count`, where `count` is the number of individuals (i.e., the number of rows) for the species indicated by `genus` and `species` in that `year`
    * Returns the resulting data frame
3. Use your function to get the time-series for `genus` = `"Dipodomys"` and `species` = `"merriami"` and then make a graph of this time-series using `ggplot` that has `year` on the x axis, `count` on the y axis, and displays the data as points.
4. Use your function to get the time-series for `genus` = `"Chaetodipus"` and `species` = `"penicillatus"` and then make a graph of this time-series using `ggplot` that has `year` on the x axis, `count` on the y axis, and displays the data as blue points (with size = 1) connected by blue lines (with size = 2). Change the x axis label to `Year` and the y axis label to `Number of Individuals`