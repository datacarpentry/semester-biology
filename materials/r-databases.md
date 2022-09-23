---
layout: page
element: notes
title: dplyr with Databases
language: R
---

> * Download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/2292171).
> * Make sure the copy you are going to use in class does not have the `SpeciesCounts` table or view.

* We can work with data in databases directly from `R`
* No need to export files from the database
* Lets the database do the heavy lifting
  * Faster
  * No RAM limits
* We can do this either directly using SQL and the `DBI` package
* Or work with the data just like we've done before using `dplyr`

### Installation

* `DBI` for general database functionality
* `RSQLite` for translating between R and SQLite
* `dbplyr` for integrating databases with `dplyr`

```r
install.packages(c("DBI", "dbplyr", "RSQLite"))
```

### Connect

```r
library(DBI)
library(RSQLite)
library(dplyr)

portaldb <- dbConnect(SQLite(), "portal.sqlite")
```

* It's most common for this code to be written as 

```r
portaldb <- dbConnect(RSQLite::SQLite(), "portal.sqlite")
portaldb
```

To avoid needing to load the `RSQLite` package using `library()`

### Check out database structure

* Once connected to a database we can list the tables

```r
dbListTables(portaldb)
```

* We can also look at the details of individual tables

```r
dbListFields(portaldb, "plots")
```

### Connecting to tables

* We can also connect to individual tables

```r
surveys <- tbl(portaldb, "surveys")
surveys
```

* The data is still in the database, not in `R`, so we can't tell how many rows it has or view it in the same way we would view a data frame.
* If we want to load all of the data from the table into an `R` data frame we use the `collect()` function

```r
surveys_df <- collect(surveys)
```

### Write a query

* We can interact with the data in the database in two ways
* First, we can write queries in SQL
* Write a query to extract counts for each `species_id`

```r
count_query <- "SELECT species_id, COUNT(*)
                FROM surveys
                GROUP BY species_id"

dbGetQuery(portaldb, count_query)
```

* This uses `DBI` to run the query and return it to the R as a data frame

* Alternatively we can use the `tbl()` function from dplyr to create a table based on the query

```r
tbl(portaldb, sql(count_query))
```

* The table is still stored in the database
* Number of rows is unknown as shown by `??`
* When we have the results we want we can use `collect()` to load them into `R` as a data frame

```r
count_data <- tbl(portaldb, sql(count_query)) %>%
              collect()
```


### Using `dplyr` pipelines with databases

* We can also use `dplyr` commands directly on databases
* To obtain the same results as our previous query using dplyr we use `group_by()` and `summarize()`

```r
species_counts <- surveys %>%
               group_by(species_id) %>%
               summarize(count = n())
```

* All of the calculation still happens in the databases
* So outside of RAM calculations are possible
* We can then bring the resulting data into `R` using `collect()` for further analysis

```r
species_counts <- surveys %>%
               group_by(species_id) %>%
               summarize(count = n()) %>%
               collect()
```

> Do [Links to Databases]({{ site.baseurl }}/exercises/Dplyr-link-to-databases-R).

### Write new information to database

* Can also move data we created in R into the database using `copy_to()`
* We can see that the current version of the database only has the three original tables

```r
dbListTables(portaldb)
```

* If we wanted to store our new `species_counts` table in the database

```r
copy_to(portaldb, species_counts, temporary=FALSE, 
        name="SpeciesCounts")
dbListTables(portaldb)
```

> * Do [Copy to Database]({{ site.baseurl }}/exercises/Dplyr-databases-copy-to-database-R/).
