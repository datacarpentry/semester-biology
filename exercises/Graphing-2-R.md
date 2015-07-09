---
layout: exercise
title: Graphing 2
subtitle: Adult Size vs. Newborn Size
language: R
---

It makes sense that larger organisms have larger offspring, but what the
mathematical form of this relationship should be is unclear. Let's
look at the problem empirically for mammals.

Download some
[mammal life history data](http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt) from the web. 
You can do this either directly in the program using `read.csv()` or download 
the file to your computer using your browser and import it from there.

When you import the data there are some extra blank lines at
the end of this file. Get rid of them by using the optional `read.csv()`
argument `nrows = 1440` to select the valid 1440 rows.

Missing data in this file is specified by `-999` and `-999.00`. Tell R that
these are null values using the optional `read.csv()` argument,
`na.strings = c("-999", "-999.00")`. This will stop them from being plotted.

1. Graph adult mass vs. newborn mass. Label the axes.
2. Graph the log (base 10) of adult mass vs. the log (base 10) of
   newborn mass. Label the axes.
3. For data where `order` is `"Rodentia"`, graph the log (base 10) of adult mass
   vs. the log (base 10) of newborn mass. Label the axes.
