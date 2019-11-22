---
layout: page
element: notes
title: dplyr with Databases
language: R
---

> * Download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/2292171).
> * Make sure the copy you are going to use in class does not have the `SpeciesCounts` table or view.

* Can use `dplyr` to access data directly from a database.
  * No need to export files from the database
  * Lets the database do the heavy lifting
    * Faster
    * No RAM limits
* Need to install the `dbplyr` package

### Installation

```r
install.packages(c("DBI", "dbplyr", "RSQLite"))
```

### Connect

```r
library(dplyr)
portaldb <- src_sqlite("portal_mammals.sqlite")
```

### Check out database structure

```r
portaldb
src_tbls(portaldb)
tbl(portaldb, "plots")

surveys <- tbl(portaldb, "surveys") %>% collect()
surveys
colnames(surveys)
```

### Write a query

* Write a query to extract counts of each genus and species

```r
count_query <- "SELECT genus, species, COUNT(*)
                FROM surveys
                JOIN species
                USING (species_id)
                GROUP BY genus, species"

tbl(portaldb, sql(count_query))
```

* Queries and data manipulation functions return similar results with various
  headings (`Source: SQL`)
* Number of rows is unknown as shown by `??`

### Using `dplyr` with databases

* Can also use `dplyr` commands directly on databases 

```r
surveys <- tbl(portaldb, "surveys")
surveys
species <- tbl(portaldb, "species")
species_counts <- inner_join(surveys, species, by = "species_id") %>%
               group_by(genus, species) %>%
               summarize(count = n())
```

* All of the calculation still happens in the databases
* So outside of RAM calculations are possible

> Do [Links to Databases]({{ site.baseurl }}/exercises/Dplyr-link-to-databases-R).

### Move the final data into R

* Queries and data manipulation results remain in the external database.
* Some calculations can't be done in the database.
* Use `collect()` to load the results into R in a local data frame (tibble).

```r
species_counts <- inner_join(surveys, species, by = "species_id") %>%
               group_by(genus, species) %>%
               summarize(count = n()) %>%
               collect()
```

### Write new information to database

* Can also store tables from R in the database use `copy_to()`

> Show `species_counts` table *NOT* in `portal_mammals.sqlite`.

```r
copy_to(portaldb, species_counts, temporary=FALSE, 
        name="SpeciesCounts")
portaldb
```

> * Show `SpeciesCounts` table in `portal_mammals.sqlite` with new name.
> * Do [Copy to Database]({{ site.baseurl }}/exercises/Dplyr-databases-copy-to-database-R/).
