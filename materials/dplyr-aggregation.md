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

```
surveys_by_species <- group_by(surveys, species_id)
```

* Use `summarize()` to calculate values for each group.
* Count the number of rows for each group (individuals in each species).

```r
summarize(surveys_by_species, abundance = n())
```

* Can group by multiple columns
* Use any function that returns a single value from a vector.
* E.g., mean, max, min

```r
surveys_by_species_plot <- group_by(surveys, species_id, plot_id)
summarize(surveys_by_species_plot, avg_weight = mean(weight))
```

* Why did we get `NA`?
    * `mean(weight)` returns `NA` when `weight` has missing values (`NA`)
* Can fix using `mean(weight, na.rm = TRUE)`

```
species_weight <- summarize(surveys_by_species,
                            avg_weight = mean(weight, na.rm = TRUE))
```

* Or us `na.omit()` to drop rows with `NA` in any column

```
na.omit(surveys_by_species)
```

> Do [Shrub Volume Aggregation]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-aggregation-R).

### Filtering by aggregated properties

* You can also filter based on aggregated values
* If we wanted to estimate species weights only for species with > 100 individuals

```r
filter(surveys_by_species, n() > 100)
```

```r
surveys_by_species_100plus <- filter(surveys_by_species, n() > 100)
species_weight <- summarize(surveys_by_species_100plus,
                            avg_weight = mean(weight, na.rm = TRUE))
```