---
layout: page
element: notes
title: Working with Tabular Data
language: R
time: 1
---

> Remember to:
>
> * If teaching with Posit Cloud or RStudio Server pre-load `surveys.csv`, `species.csv`, and `plots.csv` into the student's working directory
> * Consider removing the `dplyr` package so you can demonstrate installing it.
>     * Linux users: you may not want to do this because the source install is slow

### Setup

```r
install.packages(c('dplyr', 'readr', 'tidyr'))
download.file("https://ndownloader.figshare.com/files/2292172", "surveys.csv")
download.file("https://ndownloader.figshare.com/files/3299474", "plots.csv")
download.file("https://ndownloader.figshare.com/files/3299483", "species.csv")
download.file("https://www.datacarpentry.org/semester-biology/data/shrub-volume-data.csv", "shrub-volume-data.csv")
```

### Introduction to tabular data

* We will be working with data from the Portal Project.
* Long-term experimental study of small mammals in Arizona.

#### Setup local RStudio

* Download `surveys`, `species`, and `plots` from `Datasets` into folder.
* Need to know where the data is: Right click -> `Save link as`.
* Start/open a project (modeling good practice)

#### Setup Posit Cloud

* Go to the class space on Posit Cloud
* Click on this weeks assignment

#### Dataset

* The dataset is composed of three tables
* Each table is stored in a `csv` file
* `csv` stands for "comma separated values"
* This is common way of storing data that can be used across programming and data management software
* _Click on species.csv and View File_
* If we look at one of these files we can see that
    * It is plain text, so any program can read it
    * The first row is the header row, with different column headers separated by commas
    * All of the other rows are the data, again with different columns separated by commas
    * And so each of the values is separated by commas, hence "comma separated values"

### Packages

* Main way that reusable code is shared in R
* Combination of code, data, and documentation
* R has a rich ecosystem of packages for data manipulation & analysis
* We are going to load data using the `readr` package, so let's install it
* Download and install packages with the R console:
    * `install.packages("readr")`
* Even if we've installed a package it is not automatically available to do work with
* This because different packages may have functions with the same names
* So don't want to have to worry about all of the packages we've installed every time we right a piece of code
* Using a package:
    * Load all of the functions in the package: `library(readr)`

#### Loading and viewing the dataset

* Let's load our data into `R` using `read_csv()` from `readr`

```r
library(readr)

surveys <- read_csv("surveys.csv")
species <- read_csv("species.csv")
plots <- read_csv("plots.csv")
```

* Display data by clicking on it in `Environment`
* Three tables
    * `surveys` - main table, one row for each rodent captured, data on date,
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

### Basic `dplyr`

* Modern data manipulation library for R
* Let's install it from the console

```r
install.packages("dplyr")
```

* We typically install from the console because we only need to install a package once
* We don't want to install it every time we run our code
* Now let's load it for use in this script

```r
library(dplyr)
```

* We want all of our package loading to occur at the top of the file
* This makes it clear which packages are being used and where the functions come from

#### Select

* Select a subset of columns.

```r
select(surveys, year, month, day)
```

* They can occur in any order.

```r
select(surveys, month, day, year)
```

> Do [Exercise 1, Shrub Volume Data Basics 1-2]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).
> * Start your assignment file
> * Load the readr and dplyr packages
> * Load the shrub-volume-data.csv file using `read_csv`
> * Do Parts 1 & 2

#### Mutate

* Add new columns with calculated values using `mutate()`

```r
mutate(surveys, hindfoot_length_cm = hindfoot_length / 10)
```

* We can't see the new column because it is the last column and R has run out of space
* We can place columns at locations other than the end by using `.before` or `.after`

```r
mutate(surveys, hindfoot_length_cm = hindfoot_length / 10, .before = "hindfoot_length")
```

* If we look at `surveys` now will it contain the new column?
* *Open `surveys`*
* All of these commands produce new values, data frames in this case
* To store them for later use we need to assign them to a variable

```r
surveys_plus <- mutate(surveys,
                       hindfoot_length_cm = hindfoot_length / 10)
```

* Or we could overwrite the existing variable if we don't need it

```r
surveys <- mutate(surveys,
                  hindfoot_length_cm = hindfoot_length / 10)
```

#### Arrange

* We can sort the data in the table using `arrange`
* To sort the surveys table by by weight

```r
arrange(surveys, weight)
```

* We can reverse the order of the sort by "wrapping" `weight` in another function, `desc` for "descending"

```r
arrange(surveys, desc(weight))
```

* We can also sort by multiple columns, so if we wanted to sort first by `plot_id` (descending) and then by date

```r
arrange(surveys, desc(plot_id), year, month, day)
```

> Do [Exercise 1, Shrub Volume Data Basics 3-4]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).

#### Filter

* Use `filter()` to get only the rows that meet certain criteria.
* Combine the data frame to be filtered with a series of conditional statements.
* Column, condition, value
* To filter the data frame to only keep the data on species `DS`
    * Type the name of the function, `filter`
    * Parentheses
    * The name of the data frame we want to filter, `surveys`
    * The column to filter on, `species_id`
    * The condition, which is `==` for "is equal to"
    * And then the value, `"DS"`
    * `DS` here is a string, not a variable or a column name, so we enclose it in quotation marks

```r
filter(surveys, species_id == "DS")
```

* Like with vectors we can have a condition that is "not equal to" using "!="
* So if we wanted the data for all species except "DS

```r
filter(surveys, species_id != "DS")
```

* We can also filter on multiple conditions at once
* In computing we combine conditions in two ways "and" & "or"
* "and" means that all of the conditions must be true
* Do this in `dplyr` using additional comma separate arguments
* So, to get the data on species "DS" starting after 1995:

```r
filter(surveys, species_id == "DS", year > 1995)
```

* Alternatively we can use the `&` symbol, which stands for "and"

```r
filter(surveys, species_id == "DS" & year > 1995)
```

* Note that there is no comma in this case
* The entire clause is a single combined condition
* This approach is mostly useful for building more complex conditions

* "or" means that one or more of the conditions must be true
* Do this using `|`
* To get data on all of the *Dipodomys* species

```r
filter(surveys, species_id == "DS" | species_id == "DM" | species_id == "DO")
```

> Do [Shrub Volume Data Basics 5-7]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).

* There is also a shorter way to write these kinds of `or` conditions for a single column

```r
filter(surveys, species_id %in% c("DS", "DM", "DO"))
```


### Dropping null values

* One of the common tasks in data processing is removing null values from data
* Based on what we learned before it's natural to think that we do by filtering using the condition `weight != NA`

```r
filter(surveys, weight != NA)
```

* Why didn't that work?
* Null values like `NA` are special
* We don't want to accidentally say that two "missing" things are the same
    * We don't know if they are
* So use special commands
* Need a new package called `tidyr`, which is used for tidying up data

```r
install.packages('tidyr')
```

* Remember, we want all of our package loading to occur at the top of the file

```r
library(tidyr)
```

* `tidyr`'s `drop_na()` function removes rows with null values
* To drop all rows that have `NA` in any column

```r
drop_na(surveys)
```

* To drop only rows with `NA` in specific columns also provide the names of those columns

```r
drop_na(surveys, hindfoot_length)
```

```r
drop_na(surveys, hindfoot_length, weight)
```

> Do [Exercise 1, Shrub Volume Data Basics 8]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).
