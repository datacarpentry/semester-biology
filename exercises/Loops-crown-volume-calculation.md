---
layout: exercise
topic: Loops
title: Crown Volume Calculation
language: R
---

The
[UHURU experiment](http://www.esapubs.org/archive/ecol/E095/064/metadata.php) in
Kenya has conducted a survey of *Acacia* and other tree species in ungulate
exclosure treatments. Data for the tree data is
available [here](http://www.esapubs.org/archive/ecol/E095/064/TREE_SURVEYS.txt)
in a tab delimited (`"\t"`) format. Each of the individuals surveyed were
measured for tree height (`HEIGHT`) and canopy size in two directions (`AXIS_1`
and `AXIS_2`).

You want to estimate the crown volumes for the different species and have
developed equations for species in the *Acacia* genus:

```
volume = 0.16 * HEIGHT^0.8 * pi * AXIS_1 * AXIS_2
```

and the *Balanites* genus:

```
volume = 1.2 * HEIGHT^0.26 * pi * AXIS_1 * AXIS_2
```

For all other genera you'll use a general equation developed for trees:

```
volume = 0.5 * HEIGHT^0.6 * pi * AXIS_1 * AXIS_2
```

1. Write a function that takes a single value for each of SPECIES, HEIGHT,
   AXIS_1, and AXIS_2 as inputs and calculates a canopy volume using the
   appropriate equation. You can do this using an if/else if/else statement. The
   `SPECIES` column includes both species and genus information for *Acacia*. To
   figure out if the genus is *Acacia* you can use the `str_detect` function
   from
   the
   [`stringr` package](https://cran.r-project.org/web/packages/stringr/vignettes/stringr.html). `str_detect(species,
   "Acacia")` will return `TRUE` if string stored in the variables `species`
   contains the work "Acacia" and `FALSE` if it does not.
2. Use this function to calculate the canopy volumes for every individual in the
   UHURU tree data and create a new data frame that adds this as a column to the
   UHURU data.
