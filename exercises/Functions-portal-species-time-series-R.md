---
layout: exercise
topic: Functions
title: Portal Species Time-Series
language: R
---

If [surveys.csv](https://ndownloader.figshare.com/files/2292172), [species.csv](https://ndownloader.figshare.com/files/3299483), and [plots.csv](https://ndownloader.figshare.com/files/3299474) are not available in your workspace download them:

Load them into R using `read_csv()`.

First, combine the `surveys` and `species` tables into a single data frame.

Then, write a function that:
  * Takes three arguments - a data frame (the combined table created in (1)), a `genus` name, and a `species` name
  * Uses `dplyr` to produce a data frame with a two columns: `year` and `count`, where `count` is the number of individuals (i.e., the number of rows) for the species indicated by `genus` and `species` in that `year`
  * Make a graph of the resulting time-series using `ggplot2` that has `year` on the x axis, `count` on the y axis, and displays the data as blue points (with size = 2) connected by blue lines (with linewidth = 1). Change the x-axis label to `Year` and the y-axis label to `Number of Individuals`

1. Use your function to plot the time-series for `genus` = `"Dipodomys"` and `species` = `"merriami"`
2. Use your function to plot the time-series for `genus` = `"Chaetodipus"` and `species` = `"penicillatus"` 