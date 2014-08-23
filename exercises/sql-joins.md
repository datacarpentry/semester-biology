---
layout: exercise
title: SQL - Joins
---

The Plots table in the Portal database can be joined to the main table
by joining `plot` to `PlotID` and the species table can be joined to
the main table by joining `species` to `new_code`.

The Portal mammal data include data from a number of different
experimental manipulations. You want to do a time-series analysis of the
natural population dynamics of all of the rodent species at the site, so
write a query that returns the year, month, day, and full species name
of every individual captured on the control plots. Exclude all
non-rodent species (i.e., species for which the Rodent field in the
species table is equal to 0) and all individuals that have not been
identified to species (i.e., species for which the Unknown field in the
species table is equal to 1). Save this query as `Data From Controls`.
