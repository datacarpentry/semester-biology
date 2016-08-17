---
layout: page
element: notes
title: Integrating R and SQL
language: R
---

> Remember to
>    
> * download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/2292171).
> * open `portal_mammals.sqlite` in SQLite Manager. 
> * make sure the copy you are going to use in class does not have the `SpeciesCounts` table or view.

* We've already seen how to connect to databases using `dplyr`.
* What if we want to work outside of a `dplyr` context?
* Use `DBI` and `RSQLite`.
    * also other database management systems plugins

### Connect

```
library(DBI)
library(RSQLite)
portalDB <- "portal_mammals.sqlite"
conn <- dbConnect(SQLite(), portalDB)
```

### Check out database structure

```
dbListTables(conn)
dbListFields(conn, "plots")
dbListFields(conn, "surveys")
```

### Run queries

```
query <- "SELECT genus, species, COUNT(*)
          FROM surveys JOIN species
          ON surveys.species_ID = species.species_ID
          GROUP BY genus, species;"
species_counts <- dbGetQuery(conn, query)
```

> Do [Exercise 1 - Connect and Query]({{ site.baseurl }}/exercises/R-sql-connect-and-query-R).


### Write new information to database

> Show the original `portal_mammals.sqlite` in SQLite Manager.

* Write as a table

```
dbWriteTable(conn, "SpeciesCounts", species_counts)
dbListTables(conn)
```

> Show `SpeciesCounts` table in `portal_mammals.sqlite`.

* Write as a view

```
viewquery <- paste("CREATE VIEW SpeciesCounts AS", query)
dbSendQuery(conn, viewquery)
```

> Show the `SpeciesCounts` view in `portal_mammals.sqlite`.


> Do [Exercise 3 - Export to Database]({{ site.baseurl }}/exercises/R-sql-export-to-database-R).

> Assign remaining exercises.
