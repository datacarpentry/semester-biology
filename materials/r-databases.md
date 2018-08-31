---
layout: page
element: notes
title: dplyr with Databases
topic: R
---

> Remember to
>    
> * download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/2292171).
> * open `portal_mammals.sqlite` in SQLite Manager. 
> * make sure the copy you are going to use in class does not have the `SpeciesCounts` table or view.

* We've already seen briefly how to work with databases using `dplyr`.
* Let's get more familiar with the `dplyr` software for databases.
* `dplyr` uses 'low-level' database management libraries (`DBI`, `RSQLite`)
  for powerful and cohesive interaction with databases. 

### Connect

```
library(dplyr)
portaldb <- src_sqlite("portal_mammals.sqlite")
```

### Check out database structure

```
portaldb
tbl(portaldb, "plots")

surveys <- tbl(portaldb, "surveys") %>% collect()
surveys
surveys$ops$vars
```

### Run queries review

```
query <- "SELECT genus, species, COUNT(*)
          FROM surveys JOIN species
          ON surveys.species_id = species.species_id
          GROUP BY genus, species"
species_counts <- tbl(portaldb, sql(query))
```

> Do [Exercise 1 - Source and Query]({{ site.baseurl }}/exercises/Dplyr-databases-source-and-query-R/).

> Do [Exercise 2 - Manipulate Query]({{ site.baseurl }}/exercises/Dplyr-databases-manipulate-query-R/).


### Write new information to database

> Show the original `portal_mammals.sqlite` in SQLite Manager.

```
copy_to(portaldb, species_counts)
```

> Show `species_counts` table *NOT* in `portal_mammals.sqlite`.

```
copy_to(portaldb, species_counts, temporary=FALSE, 
        name="SpeciesCounts")
```

> Show `SpeciesCounts` table in `portal_mammals.sqlite` with new name.


> Do [Exercise 3 - Copy to Database]({{ site.baseurl }}/exercises/Dplyr-databases-copy-to-database-R/).

> Assign remaining exercises.


### Using `dplyr` with databases

* We can also use `dplyr` to access data directly from a database.
    * No need to export files from the database
    * Lets the database do the heavy lifting
        * Faster
        * No RAM limits
* Need to install the `dbplyr` package

```
library(DBI)
portaldb <- dbConnect(RSQLite::SQLite(), "portal_mammals.sqlite")
surveys <- tbl(portaldb, "surveys")
surveys
species <- tbl(portaldb, "species")
portal_data <- inner_join(surveys, species, by = "species_id") %>%
               select(year, month, day, genus, species)
```

* Can also extract data directly using SQL

```
query <- "SELECT year, month, day, genus, species
          FROM surveys JOIN species
          USING(species_id)"
portal_data <- dbGetQuery(portaldb, query)
```

* Either of these runs the query in the database

> Do [Exercise 6 - Links to Databases]({{ site.baseurl }}/exercises/Dplyr-link-to-databases-R).

* Speed example using Breeding Bird Survey of North America data
    * ~85 million cells (>250 MB)

```
# Loading from SQLite completes instantly
bbs_sqlite <- dbConnect(RSQLite::SQLite(), "bbs.sqlite")
bbs_counts <- tbl(bbs_sqlite, "breed_bird_survey_counts")
bbs_counts

# Loading from csv takes 30 seconds
bbs_counts_csv <- read.csv("BBS_counts.csv")
```

* Queries and data manipulation functions return similar results with various
  headings (`Source: SQL`)
* Number of rows is unknown as shown by `??`
* Queries and data manipulation results will remain in the external database.
* Use `collect()` to store results in a local data frame (`# A tibble`).

```
portal_data <- inner_join(surveys, species, by = "species_id") %>%
               select(year, month, day, genus, species) %>%
			   collect()
```


* If you want to store a table from R in the database use `copy_to()`
