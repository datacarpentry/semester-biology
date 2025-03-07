---
layout: exercise
topic: dplyr
title: Portal Data dplyr Review
language: R
---

If [surveys.csv](https://ndownloader.figshare.com/files/2292172), [species.csv](https://ndownloader.figshare.com/files/3299483), and [plots.csv](https://ndownloader.figshare.com/files/3299474) are not available in your workspace download them:

Load them into R using `read_csv()`.

We want to do an analysis comparing the size of individuals on the `Control`
plots to the `Long-term Krat Exclosures`. Create a data frame with the
`year`, `genus`, `species`, `weight` and `plot_type` for all cases where the
plot type is either `Control` or `Long-term Krat Exclosure`. Only include
cases where `Taxa` is `Rodent`. Remove any records where the `weight` is
missing.