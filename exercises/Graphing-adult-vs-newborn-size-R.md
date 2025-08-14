---
layout: exercise
topic: Graphing
title: Adult vs Newborn Size
language: R
---

Larger organisms have larger offspring. We want to explore the form of this
relationship in mammals.

Check to see if `Mammal_lifehistories_v2.txt` is in your working directory.
If not [download it](https://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt)
from the web.
This is tab delimited data, so you'll want to
use `read_tsv()`.

Missing data in this file is specified by `-999` and `-999.00`. Tell R that
these are null values using the optional `read_tsv()` argument,
`na = c("-999", "-999.00")`. This will stop them from being plotted.

Some of the column names have parentheses in them.
E.g., `mass(g)`.
To work with column names like this we enclose them in back ticks.
E.g., `` `mass(g)` ``
Back ticks are typically on the same key as the ~ and look like a slanted single quotation mark.

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
   create a subplot for each order.
5. Now let's visualize the relationships between the variables using a simple
   linear model. Create a new graph like your faceted plot, but using
   `geom_smooth` to fit a linear model to each order. You can do this using the
   optional argument `method = "lm"` in `geom_smooth`.
