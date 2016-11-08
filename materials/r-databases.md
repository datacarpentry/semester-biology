---
layout: page
element: notes
title: dplyr with Databases
language: R
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
