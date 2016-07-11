---
layout: page
element: notes
title: Working with Tabular Data
language: R
--- 

> Remember to
> 
> * download [`surveys.csv`](https://ndownloader.figshare.com/files/2292172).   
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

> Do [Exercise 2 - Shrub Volume 3]({{ site.baseurl }}/exercises/Scientific-shrub-volume-3-R), Tasks 1-6.

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

> Do [Exercise 2 - Shrub Volume 3]({{ site.baseurl }}/exercises/Scientific-shrub-volume-3-R), Tasks 7-8.

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
