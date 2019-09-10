---
layout: page
element: notes
title: Working with Tabular Data
language: R
time: 1
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
```

* Add new columns with calculated values using `mutate()`

```
mutate(surveys, hindfoot_length_cm = hindfoot_length / 10)
```

* If we look at `surveys` now will it contain the new column?
* *Open `surveys`*
* All of these commands produce new values, data frames in this case
* To store them for later use we need to assign them to a variable

```
surveys_plus <- mutate(surveys,
                       hindfoot_length_cm = hindfoot_length / 10)
```

* Or we could overwrite the existing variable if we don't need it

```
surveys <- mutate(surveys,
                  hindfoot_length_cm = hindfoot_length / 10)
```

> Do [Shrub Volume Data Basics]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).
