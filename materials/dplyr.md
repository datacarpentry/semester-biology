---
layout: page
element: notes
title: Working with Tabular Data
language: R
--- 

## Packages

* Packages are the main way that reusable code is shared in R
* Combination of code, data, and documentation
* Install to get the package on your computer
* Tell programs that you want to use the package

* Installing packages: `install.packages('dplyr')`
* Using a package
  * Load all of the functions: `library('dplyr')`
  * Can result in namespace issues: different packages same name
  * An alternative is to call the package directly using `::`
  * `stats::filter()` vs. `dplyr::filter()`, no import needed

## Basic Dplyr

Does a lot of the same things we've learned to do in SQL.

`surveys <- read.csv("surveys.csv")`

* Select: `select(surveys, year, month, day)`
* Filter: `filter(surveys, species_id = 'DS')`, `filter(surveys, species_id = 'DS', year > 1995)`
* Mutate: `mutate(surveys, weight_kg = weight / 1000)`

***Problem 3, 1-5***

## Group and Summarize

Like in SQL we can also group by and aggregate

* Group by: `surveys_by_species <- group_by(surveys, species_id)`
* Different looking kind of data frame, and it has groups
* To use those groups we use summarize:

`summarize(surveys_by_species, avg_weight = mean(weight))`

***Problem 3, 6-7***

## Pipes

* Combine a bunch of these kinds of manipulation
* Standard approach is intermediate variables

```
surveys_DS <- filter(surveys, species_id == 'DS')`
surveys_DS_by_yr <- group_by(surveys_DS, year)
surveys_DS_by_yr_avg_weight <- summarize(surveys_DS_by_yr, avg_weight = mean(weight))
```

* This can get a little cumbersome
* Pipes are an alternative
* Pipe `%>%` takes the output of the one command and passes it as input to next
  command, so `x %>% f(y) == f(x, y)`

`surveys %>% filter(species_id == 'DS')`

```
surveys %>% filter(species_id == 'DS') %>% group_by(year) %>% summarize(avg_weight = mean(weight))
```

```
surveys %>%
  filter(species_id == 'DS') %>%
  group_by(year) %>%
  summarize(avg_weight = mean(weight))
```

## Using Dplyr with databases

We can also use Dplyr to access data directly from a database.

* No need to export files from the database
* Let's the database do the heavy lifting: faster, no RAM limits

```
portaldb <- src_sqlite("portal_mammals.sqlite")
surveys <- tbl(portaldb, "surveys")
surveys
query <- "SELECT year, month, day, genus, species
          FROM surveys JOIN species
          ON surveys.species_id = species.species_id"
tbl(portaldb, sql(query))
```
