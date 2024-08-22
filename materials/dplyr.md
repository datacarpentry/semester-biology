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
install.packages(c('dplyr', 'readr'))
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

#### Loading and viewing the dataset

* Load these into `R` using `read_csv()`.

```r
library(readr)

surveys <- read_csv("surveys.csv")
species <- read_csv("species.csv")
plots <- read_csv("plots.csv")
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
* Even if we've installed a package it is automatically available to do analysis with
* This because different packages may have functions with the same names
* So don't want to have to worry about all of the packages we've installed every time we right a piece of code
* Using a package:
    * Load all of the functions in the package: `library("dplyr")`

### Basic `dplyr`

* Modern data manipulation library for R

#### Select

* Select a subset of columns.

```r
select(surveys, year, month, day)
```

* They can occur in any order.

```r
select(surveys, month, day, year)
```

> Do [Shrub Volume Data Basics 1-2]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).
> * Start your assignment file
> * Load the dplyr package
> * Load the shrub-volume-data.csv file
> * Do Parts 1 & 2

#### Mutate

* Add new columns with calculated values using `mutate()`

```r
mutate(surveys, hindfoot_length_cm = hindfoot_length / 10)
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

* We can reverse the order of the sort by "wrapping" `weight` in another function, `desc` for "descending

```r
arrange(surveys, desc(weight))
```

* We can also sort by multiple columns, so if we wanted to sort first by `plot_id` and then by date

```r
arrange(surveys, plot_id, year, month, day)
```

> Do [Shrub Volume Data Basics 3-4]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).

#### Filter 

* Use `filter()` to get only the rows that meet certain criteria.
* Combine the data frame to be filtered with a series of conditional statements.
* Column, condition, value
* To filter the data frame to only keep the data on species `DS`
    * Type the name of the function, `filter`
    * Parentheses
    * The name of the data frame we want to filter, `surveys`
    * The column the want to filter on, `species_id`
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
* So, to get the data on species "DS" for the year 1995:

```r
filter(surveys, species_id == "DS", year > 1995)
```

* Alternatively we can use the `&` symbol, which stands for "and"

```r
filter(surveys, species_id == "DS" & year > 1995)
```

* This approach is mostly useful for building more complex conditions

* "or" means that one or more of the conditions must be true
* Do this using `|`
* To get data on all of the *Dipodomys* species

```r
filter(surveys, species_id == "DS" | species_id == "DM" | species_id == "DO")
```

> Do [Shrub Volume Data Basics 5-7]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).


### Filtering null values

* One of the common tasks we use `filter` for is removing null values from data
* Based on what we learned before it's natural to think that we do this by using the condition `weight != NA`

```r
filter(surveys, weight != NA)
```

* Why didn't that work?
* Null values like `NA` are special
* We don't want to accidentally say that two "missing" things are the same
    * We don't know if they are
* So use special commands
* `is.na()` checks if the value is `NA`
* So if we wanted all of the data where the weigh is `NA`

```r
filter(surveys, is.na(weight))
```

* We'll learn more about why this works in the same way as the other conditional statements when we study conditionals in detail later in the course

* To remove null values we combine this with `!` for "not"

```r
filter(surveys, !is.na(weight))
```

* So `!is.na(weight)` is conceptually the same as "weight != NA"
* It is common to combine a null filter with other conditions using "and"
* For example we might want all of the data on a species that contains weights

```r
filter(surveys, species_id == "DS", !is.na(weight))
```

> Do [Shrub Volume Data Basics 8]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R).