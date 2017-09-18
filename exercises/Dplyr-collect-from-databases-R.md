---
layout: exercise
topic: dplyr
title: Collect from Databases
language: R
---

This is a follow-up to [Link to Databases]({{ site.baseurl }}/exercises/Dplyr-link-to-databases-R).

Make sure you have an existing copy of the `portal_mammals.sqlite` database or
[download a new copy](https://ndownloader.figshare.com/files/2292171).

Notice how the solution to [Link to Databases]({{ site.baseurl }}/exercises/Dplyr-link-to-databases-R) 
task 3 is a `lazy query` (or maybe a `query`) and that the number of rows is unknown (`??`).

1. Take this `lazy query` and make it a local data frame using `collect()`
   and determine how many rows it has.
2. Calculate the average weight in kilograms of a *Neotoma Albigula* (`NL`) in `surveys` and
   store the result in a local data frame.
3. Create a local data frame with the number of individuals counted in each year
   of the study. *If you don't know how to count things using `dplyr`, take
   another look at the
   [`dplyr` vignette](https://cran.r-project.org/web/packages/dplyr/vignettes/dplyr.html).
   Vignettes are a great way to reference packages in R if you don't know the 
   name of a function you need but you know the package has that capability. In
   this case, you will want to search for 'count'.*

*Want a challenge?*: Create a local data frame containing the average size of each rodent
   species for individuals captured on the `Control` plots. You can do this by
   either creating a connection to the `species` and `plots` tables and using
   `inner_join` in `dplyr` or by writing the query in `SQL` and using
   `tbl(portaldb, sql(query))`, where `query` is a string containing the SQL you
   want to run. Better yet try doing it both ways.
