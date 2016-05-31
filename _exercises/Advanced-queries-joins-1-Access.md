---
layout: exercise
topic: Advanced Queries
title: Joins 1
language: Access
---

In a new database import the main table from the Portal database (remember that
wgt and hfl need to have their types changes to integer). Now download and
import the [Plots table]({{ site.baseurl }}/data/PortalMammals_plots.csv) and the
[Species table]({{ site.baseurl }}/data/PortalMammals_species.csv) (if you don't remember how to
import tables see the details in the
[Importing Tables problem]({{ site.baseurl }}/exercises/Database-control-importing-tables-Access). We will use this
database for all of the exercises on joins, database structure, and nested
queries. Remember to check that the fields in each table have reasonable
types. The Plots table can be joined to the main table by joining `plot` to
`PlotsID` and the species table can be joined to the main table by joining
`species` to `new_code`.

The Portal mammal data include data from a number of different
experimental manipulations. You want to do a time-series analysis of the
natural population dynamics of all of the rodent species at the site, so
write a query that returns the year, month, day, and full species name
of every individual captured on the control plots. Exclude all
non-rodent species (i.e., species for which the Rodent field in the
species table is equal to 0) and all individuals that have not been
identified to species (i.e., species for which the Unknown field in the
species table is equal to 1). Save this query as `Data From Controls`.
