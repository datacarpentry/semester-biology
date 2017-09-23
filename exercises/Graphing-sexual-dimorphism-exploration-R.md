---
layout: exercise
topic: Graphing
title: Sexual Dimorphism Exploration
language: R
---

You are interested in understanding whether sexual size dimorphism is a general
pattern in birds.

Download and import a
[large publicly available dataset of bird size measures](http://www.esapubs.org/archive/ecol/E088/096/avian_ssd_jan07.txt)
created by [Lislevand et al. 2007](https://doi.org/10.1890/06-2054).

Import the data into R. It is tab delimited so you'll want to use `sep = "\t"`
as an optional argument when calling `read.csv()`. The `\t` is how we indicate a
tab character to R (and most other programming languages).

Using `ggplot`:

1. Create a histogram of female masses (they are in the `F_mass` column). Change
   the x axis label to `"Female Mass(g)"`.
2. A few really large masses dominate the histogram so create a `log10` scaled
   version. Change the x axis label to `"Female Mass(g)"` and the color of the
   bars to blue (using the `fill = "blue"` argument).
3. Now let's add the data for male birds as well. Create a single graph with
   histograms of both female and male body mass. *Due to the way the data is
   structured you'll need to add a 2nd `geom_histogram()` layer that specifies a
   new aesthetic. To make it possible to see both sets of bars you'll need
   to make them transparent with the optional argument `alpha = 0.3`.*
4. These distributions seem about the same, but this is all birds together so it
   might be difficult to see any patterns. Use `facet_wrap()` to make one
   subplot for each family.
5. Make the same graph as in the last task, but for wing size instead of
   mass. Do you notice anything strange? If so, you may have gotten caught by
   the use of non-standard null values. If you already noticed and fixed this,
   Nice Work! If not, you can use the optional `na.strings = c(“-999”, “-999.0”)`
   argument in `read.csv()` to tell R what value(s) indicated nulls in a
   dataset.
