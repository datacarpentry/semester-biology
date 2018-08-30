---
layout: page
element: notes
title: Working with Tabular Data
language: R
time: 3
---

> Remember to:
>
> * Consider removing the `dplyr` package so you can demonstrate installing it.
>     * Linux users: you may not want to do this because the source install is slow

### Introduction to tabular data

* We will be working with data from the Portal Project.
    * Long-term experimental study of small mammals in Arizona.
    * Download `surveys`, `species`, and `plots` from `Datasets` into folder.
    * Need to know where the data is: Right click -> `Save link as`.

* Start/open a project (modeling good practice)

* Dataset is composed of three tables.
* Load these into `R` using `read.csv()`.

```
surveys <- read.csv("surveys.csv")
species <- read.csv("species.csv")
plots <- read.csv("plots.csv")
```

* Display data by clicking on it in `Environment`
* Three tables
    * `surveys` - main table, one row for each rodent captured, date on date,
      location, species ID, sex, and size
    * `species` - latin species names for each species ID + general taxon
    * `plots` - information on the experimental manipulations at the site

* Good tabular data structure
    * One table per type of data
        * Tables can be linked together to combine information.
    * Each row contains a single record.
        * A single observation or data point
    * Each column or field contains a single attribute.
        * A single type of information

### Packages

* Main way that reusable code is shared in R
* Combination of code, data, and documentation
* R has a rich ecosystem of packages for data manipulation & analysis
* Download and install packages with the R console:
    * `install.packages("dplyr")`
* Using a package:
    * Load all of the functions in the package: `library("dplyr")`

### Basic `dplyr`

* Modern data manipulation library for R

```
surveys <- read.csv("surveys.csv")
```

* Select a subset of columns.

```
select(surveys, year, month, day)
```

* They can occur in any order.

```
select(surveys, month, day, year)
```

* Use `filter()` to get only the rows that meet certain criteria.
    * Combine the data frame to be filtered with a series of conditional statements.
    * Column, condition, value
  
```
filter(surveys, species_id == "DS")
filter(surveys, species_id == "DS", year > 1995)
```

* Commas indicate `and`, use `|` for `or`.

```
filter(surveys, species_id == "DS" | species_id == "DM")
```

* Add new columns with calculated values using `mutate()`

```
mutate(surveys, hindfoot_length_cm = hindfoot_length / 10)
```

> Do [Shrub Volume Data Basics]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).

### Aggregation

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
* `mean(weight, na.rm=TRUE)`

```
species_weight <- summarize(surveys_by_species, avg_weight = mean(weight, na.rm = TRUE))
```

* `na.omit()` to remove `NA` from output

```
sp_weight_nonull <- na.omit(species_weight)
```

> Do [Shrub Volume Aggregation]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-aggregation-R).


### Joins

> Remember to:
>
> * display a fully joined version of the Portal data using:  
> `portal_bigtable <- inner_join(inner_join(surveys, species), plots)`

#### Why use multiple tables

* Not efficient to include all information in a single table.
* Redundant information makes it more difficult to update or revise data.
    * Make changes in one place, not hundreds of places.
* Use multiple tables
* Each table contains a single kind of information
    * `surveys`: information about individuals
    * `species`: information about species
    * `plots`: information about plots
* If a species name changes we only need to change it in the `species` table
* Connect tables using joins to describe relationships between tables

#### Basic join

* Joins combine two tables using one or more columns
* `inner_join` keeps information from both tables that share a join field value

```
species <- read.csv("species.csv")
combined <- inner_join(surveys, species, by = "species_id")
head(combined)
```

* One way to think about this join is that it adds the information in
  `species` to the `surveys` table

> Do [Shrub Volume Join]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-join-R).

#### Multi-table join

* Use multiple joins to link multiple tables

```
portal_full <- inner_join(combined, plots, by = "plot_id")
head(portal_full)
```

### Combining data manipulations

* Combine a series of data manipulation actions
* Do each action in sequential order

#### Intermediate variables

* Determine the mean weight of DS in each year

```
surveys_DS <- filter(surveys, species_id == "DS")
surveys_DS_by_yr <- group_by(surveys_DS, year)
avg_weight_DS_by_yr <- summarize(surveys_DS_by_yr,
                                 avg_weight = mean(weight, na.rm=TRUE))
```

> Do [Portal Data Manipulation Exercise 1-2]({{ site.baseurl }}/exercises/Portal-data-manip-R)

#### Pipes

* Intermediate variables can get cumbersome if their are lots of steps.
* `%>%` ("pipe") takes the output of one command and passes it as input to the
  next command
* `x %>% f(y)` translates to `f(x, y)`
* `surveys %>% filter(species_id == "DS")`

```
avg_weight_DS_by_yr <- surveys %>%
  filter(species_id == "DS") %>%
  group_by(year) %>%
  summarize(avg_weight = mean(weight, na.rm=TRUE))
```

> Do [Fix the Code]({{ site.baseurl }}/exercises/Dplyr-fix-the-code-R).
