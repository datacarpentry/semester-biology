---
layout: exercise
title: Graphing - adult size vs. newborn size
---

It makes sense that larger organisms have larger offspring, but what the
exact mathematical form of this relationship shoudl be is unclear. Let's
look at the problem empirically for mammals.

1.  Download some [mammal life history
    data](http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt)
    from the web. You can do this either directly in the program using
    urllib or download the file to your computer using your browser and
    import it from there.
2.  Import the data into a numpy structured array using genfromtxt().
    There are some extra blank lines at the end of this file, so get rid
    of them by using the optional genfromtxt() argument, skip\_footer=4.
3.  Missing data in this file is specified by -999.00. To make sure that
    we don't run into this missing data get rid of the rows in the table
    where the 'massg' column is equal to -999.00 and where the
    'newborng' column is equal to -999.00.
4.  Graph adult mass vs. newborn mass. Label the axes.
5.  Graph the log (base 10) of adult mass vs. the log (base 10) of
    newborn mass. Lable the axes.
6.  Congratulate yourself on a job well done. Call it a day. And be
    ready to come back tomorrow and do some statistical analysis.

