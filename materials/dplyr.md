---
layout: page
element: notes
title: Working with Tabular Data
language: R
--- 

> Remember to
> 
> * download [`surveys.csv`](https://ndownloader.figshare.com/files/2292172).
> * download [`species.csv`](https://ndownloader.figshare.com/files/3299483).
> * download [`portal_mammals.sqlite`](https://ndownloader.figshare.com/files/2292171).


### Packages

* Main way that reusable code is shared in R
* Combination of code, data, and documentation
* Download and install packages with the R console:
    * `install.packages("dplyr")`
* Using a package:
    * Load all of the functions in the package: `library("dplyr")`
        * Can result in namespace issues when different packages have functions with the same name 
        * `filter()` is the name of a function in `dplyr` and `stats` packages
    * Call a function in the package directly: `::`
        * No use of `library()` needed
        * `dplyr::filter()` vs. `stats::filter()`

### Basic `dplyr`

* Does a lot of the same things we've learned to do in SQL.

```
surveys <- read.csv("surveys.csv")
```

* Select: 
    * `select(surveys, year, month, day)`
* Filter: 
    * `filter(surveys, species_id == "DS")`
    * `filter(surveys, species_id == "DS", year > 1995)`
* Mutate: 
    * `mutate(surveys, weight_kg = weight / 1000)`

> Do [Exercise 2 - Shrub Volume Data Basics]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).

### Aggregation

* Group by: 
    * `group_by(surveys, species_id)`
    * Different looking kind of `data.frame` 
        * Source, grouping, and data type information

```
surveys_by_species <- group_by(surveys, species_id)
```

* Grouping with `summarize()`:
    * `summarize(surveys_by_species, avg_weight = mean(weight))`
    * Real data problem: 
        * `mean(weight)` when `weight` has missing values (`NA`) 
            * Returns `NA`
            * `mean(weight, na.rm=TRUE)`

> Do [Exercise 3 - Shrub Volume Aggregation]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-aggregation-R).

### Joins

* `inner_join` in `dplyr` works like `JOIN` in SQL

```
species <- read.csv("species.csv")
combined <- inner_join(surveys, species, by = "species_id")
head(combined)
```

> Do [Exercise 4 - Shrub Volume Join]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-join-R).

### Pipes

* Combine a series of data manipulation actions
* Intermediate variables
    * Step-wise approach 
    * Can get cumbersome with lots of variable objects in the environment

```
surveys_DS <- filter(surveys, species_id == "DS")
surveys_DS_by_yr <- group_by(surveys_DS, year)
avg_weight_DS_by_yr <- summarize(surveys_DS_by_yr, 
                                 avg_weight = mean(weight, na.rm=TRUE))
```

* Pipes:
    * Operator: 
        * `%>%`
    * Operation:
        * `%>%` takes the output of one command and passes it as input to the next command 
        * `x %>% f(y)` translates to `f(x, y)`
        * `surveys %>% filter(species_id == "DS")`

```
surveys %>%
  filter(species_id == "DS") %>%
  group_by(year) %>%
  summarize(avg_weight = mean(weight, na.rm=TRUE))
```

> Do [Fix the Code 1]({{ site.baseurl }}/exercises/Dplyr-fix-the-code-1-R).

### Using `dplyr` with databases

* We can also use `dplyr` to access data directly from a database.
    * No need to export files from the database
    * Lets the database do the heavy lifting
        * Faster
        * No RAM limits

```
portaldb <- src_sqlite("portal_mammals.sqlite")
surveys <- tbl(portaldb, "surveys")
surveys
query <- "SELECT year, month, day, genus, species
          FROM surveys JOIN species
          ON surveys.species_id = species.species_id"
tbl(portaldb, sql(query))
```

* Queries and data manipulation functions return similar results with various headings.

```
> tbl(portaldb, "surveys")
Source: sqlite 3.8.6 [portal_mammals.sqlite]
From: surveys

> tbl(portaldb, sql(query))
Source: sqlite 3.8.6 [portal_mammals.sqlite]
From: <derived table>

> surveys <- tbl(portaldb, "surveys")
> select(surveys, year, month, day)
Source: sqlite 3.8.6 [portal_mammals.sqlite]
From: surveys
```

* Queries and data manipulation results will remain in the external database.
* Use `collect()` to store results in a local data frame.
