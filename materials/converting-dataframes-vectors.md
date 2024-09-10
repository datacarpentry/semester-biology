---
layout: page
element: notes
title: Converting Between Data Frames and Vectors
language: R
---

### Setup

```r
install.packages('dplyr')
download.file("https://ndownloader.figshare.com/files/2292172", "surveys.csv")
download.file("https://ndownloader.figshare.com/files/3299474", "plots.csv")
download.file("https://ndownloader.figshare.com/files/3299483", "species.csv")
download.file("https://www.datacarpentry.org/semester-biology/data/shrub-volume-data.csv", "shrub-volume-data.csv")
```

### Introduction

* We've learned about two general ways to store data, vectors and data frames
* Vectors store a single set of values with the same type
* Data frames store multiple sets of values, one in each column, that can have different types

* These two ways of storing data are related to one another
* A data frame is a bunch of equal length vectors that are grouped together
* This is why when using `mutate()` and `summarize()` we can use any function that works on a vector
* As a result we can extract vectors from data frames and make data frames from vectors

### Extracting vectors from data frames

* There are several ways to extract a vector from a data frame
* Let's look at these using the Portal data
* We'll start by loading the `species` table into R

```r
surveys <- read_csv("species.csv")
```

* We do this using `[]`
* Remember that `[]` also mean "give me a piece of something" in R
* Let's get the `species_id` column
* `"species_id"` has to be in quotes because we we aren't using the tidyverse

```r
species["species_id"]
```

* This actually returns a one column data frame, not a vector
* To extract a single column as a vector we use two sets of `[]`
* Think of the second set of `[]` as getting the single vector from inside the one column data frame

```r
species[["species_id"]]
```

* We can also use the `$`
* Shorthand for `[[]]` in cases where the piece of something we want to get has a name
* So, we start with the object we want a part of, our `surveys` data frame
* Then the `$` with no spaces around it
* and then the name of the `species_id` column (without quotes, just to be confusing)

```r
species$species_id
```

* Finally, `dplyr` has a function called `pull()`

```r
pull(species, species_id)
```

* This is typically used at the end a dplyr pipeline

```r
species |>
  filter(taxa == "Rodent") |>
  pull(species_id)
```

### Combining vectors to make a data frame

* We can also combine vectors to make a data frame
* We can make a data frame using the `data.frame` function
* It takes one argument for each column in the data frame
* The argument includes the name of the column we want in the data frame, `=`, and the name of the vector whose values we want in that column
* Just like `mutate` and `summarize`

```r
states <- c("FL", "FL", "GA", "SC")
count <- c(9, 16, 3, 10)
area <- c(3, 5, 1.9, 2.7)
count_data <- data.frame(states = states, counts = count, regional_area = area)
```

* We can also add columns to the data from that only include a single value without first creating a vector
* We do this by providing a name for the new column, an equals sign, and the value that we want to occur in every row
* For example, if all of this data was collected in the same year and we wanted to add that year as a column in our data frame we could do it like this

```r
count_data_year <- data.frame(year = 2022, states = states, counts = count, regional_area = area)
```

* `year =` sets the name of the column in the data frame
* And `2000` is that value that will occur on every row of that column
* If we run this and look at the `count_data_year` data frame we'll see that it includes the year column with `2000` in every row

* We can add a vector as a new column to an existing data frame using `mutate()`

```r
library(dplyr)
elevation <- c(100, 65, 226, 152)
count_data_year_elev <- mutate(count_data_year, elevations = elevation)
```

### Summary

* So, that's the basic idea behind how vectors and data frames are related and how to convert between them.
* A data frame is a set of equal length vectors
* We can extract a column of a data frame into a vector using either `$` or two sets of `[]`
* We can combine vectors into data frames using the `data.frame` function, which takes a series of arguments, one vector for each column we want to create in the data frame.


> Do [Extracting vectors from data frames]({{ site.baseurl }}/exercises/extracting-vectors-from-data-frames-R/).
> Do [Building data frames from vectors]({{ site.baseurl }}/exercises/building-data-frames-from-vectors-R/).
