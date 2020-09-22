---
layout: page
element: notes
title: dplyr Aggregation
language: R
time: 30
---

> Remember to
> 
> * Load `surveys.csv` data into `surveys`

### Basic aggregation

* Aggregation combines rows into groups based on one of more columns.
* Calculates combined values for each group.
* First step, group the data frame.
* Let's group it by `species_id`
* `group_by`
* Arguments: 1) table to work on; 2) columns to group by 

```
group_by(surveys, species_id)
```

* Different looking kind of `data.frame`
    * Source, grouping, and data type information
* Store the data frame in a variable to use in the next step

```r
surveys_by_species <- group_by(surveys, species_id)
```

* After grouping a data frame use `summarize()` to calculate values for each group.
* Count the number of rows for each group (individuals in each species).
* `summarize`
* Arguments
  * Table to work on, which needs to be a grouped table
  * One additional argument for each calculation we want to do for each group
    * New column name to store calculated value
    * `=`
    * Calculation that we want to perform for each group
    * We'll use the function `n` which is a special function that counts the rows in the table

```r
summarize(surveys_by_species, abundance = n())
```

* Can group by multiple columns
* Count the number of individuals in each species and plot

```r
surveys_by_species_plot <- group_by(surveys, species_id, plot_id)
species_plot_counts <- summarize(surveys_by_species_plot, abundance = n())
```

* Use any function that returns a single value from a vector.
* E.g., mean, max, min
* We'll calculate the average weight of each species on each plot

```r
species_weight <- summarize(surveys_by_species_plot, avg_weight = mean(weight))
```

* *Open table*
* Why did we get `NA`?
    * `mean(weight)` returns `NA` when `weight` has missing values (`NA`)
* Can fix using `mean(weight, na.rm = TRUE)`

```
species_weight <- summarize(surveys_by_species,
                            avg_weight = mean(weight, na.rm = TRUE))
```

* Still has `NaN` for species that have never been weighed
* Can filter using `!is.na`

```
filter(species_weight, !is.na(avg_weight))
```

> Do [Shrub Volume Aggregation]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-aggregation-R).
