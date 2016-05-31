---
layout: exercise
topic: Graphing
title: Adult vs Newborn Size 1
language: Python
---

It makes sense that larger organisms have larger offspring, but what the
mathematical form of this relationship should be is unclear. Let's
look at the problem empirically for mammals.

Download some
[mammal life history data](http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt)
from the web. You can do this either directly in the program using `urllib` or
download the file to your computer using your browser and import it from there.

Import the data into a Pandas data frame. There are some extra blank lines at
the end of this file, so get rid of them by using the optional `read_csv()`
argument, `skip_footer=7`.

Missing data in this file is specified by -999 and -999.00. Tell Pandas that
these are null values using the optional `read_csv()` argument,
`na_values=['-999', '-999.00']`. This will stop them from being plotted.

1. Graph adult mass vs. newborn mass. Label the axes.
2. Graph the log (base 10) of adult mass vs. the log (base 10) of
   newborn mass. Label the axes.
3. For data where `order` is `Rodentia`, graph the log (base 10) of adult mass
   vs. the log (base 10) of newborn mass. Label the axes.
