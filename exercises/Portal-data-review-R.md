---
layout: exercise
topic: dplyr
title: Portal Data Review
language: R
---

If `surveys.csv`, `species.csv`, and `plots.csv` are not available in your workspace download them:

* [`surveys.csv`](https://ndownloader.figshare.com/files/2292172)
* [`species.csv`](https://ndownloader.figshare.com/files/3299483)
* [`plots.csv`](https://ndownloader.figshare.com/files/3299474)

Load them into R using `read.csv()`.

1. Create a data frame with only data for the `species_id` `DO`, with the columns `year`, `month`, `day`, `species_id`, and `weight`.
2. Create a data frame with only data for species IDs `PP` and `PB` and for years starting in 1995, with the columns `year`, `species_id`, and `hindfoot_length`, with no null values for `hindfoot_length`.
3. Create a data frame with the average `hindfoot_length` for each `species_id` in each `year` with no null values.
4. Create a data frame with the `year`, `genus`, `species`, `weight` and `plot_type` for all cases where the `genus` is `"Dipodomys"`.
5. Make a scatter plot with `weight` on the x-axis and `hindfoot_length` on the y-axis. Use a `log10` scale on the x-axis. Color the points by `species_id`. Include good axis labels.
6. Make a histogram of weights with a separate subplot for each `species_id`. Do not include species with no weights. Set the `scales` argument to `"free_y"` so that the y-axes can vary. Include good axis labels.
7. (Challenge) Make a plot with histograms of the weights of three species, `PP`, `PB`, and `DM`, colored by `species_id`, with a different facet (i.e., subplot) for each of three `plot_type`'s `Control`, `Long-term Krat Exclosure`, and `Short-term Krat Exclosure`. Include good axis labels and a title for the plot. Export the plot to a `png` file.