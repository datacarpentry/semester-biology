---
layout: exercise
topic: Graphing
title: Adult vs Newborn Size 1
language: R
---

It makes sense that larger organisms have larger offspring, but what the
mathematical form of this relationship should be is unclear. Let's look at the
problem empirically for mammals.

Download some
[mammal life history data](http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt) from the web. 
You can do this either directly in the program using `read.csv()` or download 
the file to your computer using your browser, save it in the `data`
subdirectory, and import it from there.

When you import the data there are some extra blank lines at
the end of this file. Get rid of them by using the optional `read.csv()`
argument `nrows = 1440` to select the valid 1440 rows.

Missing data in this file is specified by `-999` and `-999.00`. Tell R that
these are null values using the optional `read.csv()` argument,
`na.strings = c("-999", "-999.00")`. This will stop them from being plotted.

1. Graph adult mass vs. newborn mass. Label the axes with clearer labels than
   the column names.
2. It looks like there's a regular pattern here, but it's definitely not
   linear. Let's see if log-transformation straightens it out. Graph adult mass
   vs. newborn mass, with both axes scaled logarithmically. Label the axes.
3. This looks like a pretty regular pattern, so you wonder if it varies among
   different groups. Graph adult mass vs. newborn mass, with both axes scaled
   logarithmically, and the data points colored by order. Label the axes.
4. Coloring the points was useful, but there are a lot of points and it's kind
   of hard to see what's going on with all of the orders. Use `facet_wrap` to
   create subplot for each order.
5. Now let's visualize the relationships between the variables using a simple
   linear model. Create a new graph like your faceted plot, but using
   `geom_smooth` to fit a linear model to each order. You can do this using the
   optional argument `method = "lm"` in `geom_smooth`.
