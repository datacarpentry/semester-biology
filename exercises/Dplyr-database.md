---
layout: exercise
title: Dplyr Using Databases
subtitle: From Database to R Using Dplyr
language: R
---

This is a follow-up to
[Data Frames 2]({{ site.baseurl }}/exercises/Data-frames-2-R). In the previous
exercise we moved data from an SQLite database to R by creating an intermediate
file. That worked OK, but it meant we had to do some work by hand, so if we
needed to rerun the analysis after updating the database we'd have to do that
manual step all over again. It also increases the chance that we'll make a
mistake at some point when we're exporting the data from SQLite. So, let's
access the data directly from R instead.

Install the `RSQLite` package (and the `dplyr` package if you haven't already).

Either use an existing copy of the `portal_mammals.sqlite` database or download
a [new copy](http://files.figshare.com/1919743/portal_mammals.sqlite). You
should now be able to link to the surveys table in the database using:

```
portaldb <- src_sqlite("portal_mammals.sqlite")
surveys <- tbl(portaldb, "surveys")
```

`surveys` will be a `tbl_df`, which means that we won't need to worry about it
printing out huge numbers of rows in the answers below.

Using this table in the database:

1. Select the year, month, day, and species_id columns in that order
2. Create a new data frame with the year, species_id, and weight in kilograms of each
   individual, with no null weights.
3. Create a new data frame with the number of individuals counted in each year
   of the study. If you don't know how to count things using `dplyr` I'd
   recommend checking out the
   [`dplyr` vignette](https://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html).
   Vignette's can be a great way to learn how to use packages in R. If you're in
   a hurry you can also do a search for `count` in the page.
