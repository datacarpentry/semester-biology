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

```
summarize(surveys_by_species, abundance = n())
```

* Any function that returns a single value from a vector.
* E.g., mean.

```
species_weight <- summarize(surveys_by_species, avg_weight = mean(weight))
```

### Null values

* `mean(weight)` when `weight` has missing values (`NA`)
* Returns `NA`

* Use `filter()` to remove the `NA`s

```
surveys_by_species <- filter(surveys_by_species, !is.na(weight))
species_weight <- summarize(surveys_by_species, avg_weight = mean(weight))
```

* `na.omit()` filters out rows with `NA` in any column

```
sp_weight_nonull <- na.omit(species_weight)
```

> Do [Shrub Volume Aggregation]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-aggregation-R).