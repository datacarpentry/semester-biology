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
* Let's group it by `year`
* `group_by`
* Arguments: 1) table to work on; 2) columns to group by 

```r
group_by(surveys, year)
```

* Different looking kind of `data.frame`
    * Source, grouping, and data type information
* Store the data frame in a variable to use in the next step

```r
surveys_by_year <- group_by(surveys, year)
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
year_counts <- summarize(surveys_by_year, abundance = n())
```

* Can group by multiple columns
* Count the number of individuals in each plot in each year

```r
surveys_by_plot_year <- group_by(surveys, plot_id, year)
plot_year_counts <- summarize(surveys_by_plot_year, abundance = n())
```

* Just like with other `dplyr` functions we could write this using pipes instead

```r
plot_year_counts <- surveys |>
  group_by(plot_id, year) |>
  summarize(abundance = n())
```

> Do [Portal Data Aggregation 1-2]({{ site.baseurl }}/exercises/Portal-data-aggregation-R/).


* We can also do multiple calculations using summarize
* Use any function that returns a single value from a vector.
* E.g., mean, max, min
* We'll calculate the number of individuals in each plot year combination and their average weight

```r
plot_year_count_weight <- surveys |>
  group_by(plot_id, year) |>
  summarize(abundance = n(), avg_weight = mean(weight))
```

* *Open table*
* Why did we get `NA`?
    * `mean(weight)` returns `NA` when `weight` has missing values (`NA`)
* Can fix using `mean(weight, na.rm = TRUE)`

```r
plot_year_count_weight <- surveys |>
  group_by(plot_id, year) |>
  summarize(abundance = n(),
            avg_weight = mean(weight, na.rm = TRUE))
```

* Still has `NaN` for species that have never been weighed
* Can filter using `!is.na`

```r
plot_year_count_weight <- surveys |>
  group_by(plot_id, year) |>
  summarize(abundance = n(),
            avg_weight = mean(weight, na.rm = TRUE)) |>
  filter(!is.na(avg_weight))
```

> Do [Portal Data Aggregation 3]({{ site.baseurl }}/exercises/Portal-data-aggregation-R/).
