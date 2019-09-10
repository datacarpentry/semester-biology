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
* First, group the data frame.

```
group_by(surveys, species_id)
```

* Different looking kind of `data.frame`
    * Source, grouping, and data type information

```r
surveys_by_species <- group_by(surveys, species_id)
```

* Use `summarize()` to calculate values for each group.
* Count the number of rows for each group (individuals in each species).

```r
summarize(surveys_by_species, abundance = n())
```

* Can group by multiple columns

```r
surveys_by_species_plot <- group_by(surveys, species_id, plot_id)
summarize(surveys_by_species, abundance = n())
```

* Use any function that returns a single value from a vector.
* E.g., mean, max, min

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
* Can use `na.omit()` to drop rows with `NA` or `NaN` in any column

```
na.omit(surveys_weight)
```

> Do [Shrub Volume Aggregation]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-aggregation-R).
