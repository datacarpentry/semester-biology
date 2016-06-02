---
layout: exercise
topic: dplyr
title: Link to Databases
language: R
---

Let's access an SQL database directly from R. Install the `RSQLite` package (and 
the `dplyr` package if you haven't already).

Either use an existing copy of the `portal_mammals.sqlite` database or [download
a new copy](https://ndownloader.figshare.com/files/2292171). You
should now be able to link to the surveys table in the database using:

```
portaldb <- src_sqlite("portal_mammals.sqlite")
surveys <- tbl(portaldb, "surveys")
```

`surveys` will be a `tbl_df`, which means that we won't need to worry about it
printing out huge numbers of rows in the answers below.

Using this table in the database:

1. Use the `nrow()` function to determine how many records are represented in this 
   dataset.
2. Select the year, month, day, and species_id columns in that order
3. Create a new data frame with the year, species_id, and weight in kilograms 
   of each individual, with no null weights.
4. Use the `distinct()` function to print the species_id for each
   species in the dataset that have been weighed.
5. Calculate the average size of a *Neotoma Albigula* (`NL`) in this dataset.
6. Create a new data frame with the number of individuals counted in each year
   of the study. If you don't know how to count things using `dplyr` I'd
   recommend checking out the
   [`dplyr` vignette](https://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html).
   Vignette's can be a great way to learn how to use packages in R. If you're in
   a hurry you can also do a search for `count` in the page.
