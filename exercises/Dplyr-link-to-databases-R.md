---
layout: exercise
topic: dplyr
title: Link to Databases
language: R
---

Let's access an SQL database directly from R using `dplyr`.

Either use an existing copy of the `portal_mammals.sqlite` database or [download
a new copy](https://ndownloader.figshare.com/files/2292171). You
should be able to link to the `surveys` table in the database using:

```
portaldb <- src_sqlite("portal_mammals.sqlite")
surveys <- tbl(portaldb, "surveys")
```

`surveys` will be a `tbl_sqlite`, which means that the table remains external to 
the R environment. *Also, we won't need to worry about it printing out huge 
numbers of rows when we look at it.*

1. Use the `nrow()` function to determine how many records are represented in
   `surveys`.
2. Select the `year`, `month`, `day`, and `species_id` columns in that order.
3. Create a new data frame with the `year`, `species_id`, and weight in
   kilograms of each individual, with no null weights.
4. Use the `distinct()` function to print the `species_id` for each
   species in the dataset that has been weighed. Name this table `species_ids`.
5. Determine how many rows are in `species_ids`. *You will have to take this
   `<derived table>` and make it a local data frame (`tbl_df`) using
   `collect()`.*
6. Calculate the average size of a *Neotoma Albigula* (`NL`) in `surveys` and
   store the result in a local data frame.
7. Create a local data frame with the number of individuals counted in each year
   of the study. *If you don't know how to count things using `dplyr`, take
   another look at the
   [`dplyr` vignette](https://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html).
   Vignettes are a great way to reference packages in R if you don't know the 
   name of a function you need but you know the package has that capability. In
   this case, you will want to search for 'count'.*

*Want a challenge?*: Create a local data frame containing the average size of each rodent
   species for individuals captured on the `Control` plots. You can do this by
   either creating a connection to the `species` and `plots` tables and using
   `inner_join` in `dplyr` or by writing the query in `SQL` and using
   `tbl(portaldb, sql(query))`, where `query` is a string containing the SQL you
   want to run. Better yet try doing it both ways.
