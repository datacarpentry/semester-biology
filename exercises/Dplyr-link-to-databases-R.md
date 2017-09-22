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
library(DBI)
portaldb <- dbConnect(RSQLite::SQLite(), "portal_mammals.sqlite")
surveys <- tbl(portaldb, "surveys")
```

`surveys` is actually a connection to the database, which means that the table
remains external to the R environment. *Also, we won't need to worry about it
printing out huge numbers of rows when we look at it.*

1. Select the `year`, `month`, `day`, and `species_id` columns in that order.
2. Create a new data frame with the `year`, `species_id`, and weight **in
   kilograms** of each individual, with no null weights.
3. Use the `distinct()` function to print the `species_id` for each
   species in the dataset that has been weighed.
