---
layout: page
element: notes
title: Integrating R and SQL
language: R
---

* Already seen how to connect to database using `dplyr`
* What if we want to do this outside of a `dplyr` context
* Use `DBI` and `RSQLite` (or other appropriate DBMS plugin)

## Connect

```
library(DBI)
library(RSQLite)
portalDB <- "portal_mammals.sqlite"
conn <- dbConnect(SQLite(), portalDB)
```

## Checkout the database

```
dbListTables(conn)
dbListFields(conn, "plots")
dbListFields(conn, "surveys")
```

## Run queries

```
query <- "SELECT genus, species, COUNT(*)
          FROM surveys JOIN species
		  ON surveys.species_ID = species.species_ID
		  GROUP BY genus, species"
species_counts <- dbGetQuery(conn, query)
```

**Exercise 1**


## Write new information to database

```
dbWriteTable(conn, "SpeciesCounts", species_counts)
```

* Show that this table now exists in the database
* Alternatively we could make a view

```
viewquery <- paste("CREATE VIEW SpeciesCounts AS", query)
dbSendQuery(conn, viewquery)
```

* Show the view in the DB


**Exercise 3**
