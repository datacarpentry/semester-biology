---
layout: page
element: notes
title: Converting Between Data Frames and Vectors
language: R
---

* We've learned about two general ways to store data, vectors and data frames
* Vectors store a single set of values with the same type
* Data frames store multiple sets of values, one in each column, that can have different types

* These two ways of storing data are related to one another
* A data frame is a bunch of equal length vectors that are grouped together
* So, we can extract vectors from data frames and we can also make data frames from vectors

### Extracting vectors from data frames

* There are several ways to extract a vector from a data frame
* Let's look at these using the Portal data
* We'll start by loading the `surveys` table into R

```r
surveys <- read.csv("surveys.csv")
```

* One common approach to extracting a column into a vector is to use the `$`
* The `$` in R means "give me a named piece of something"
* So, we start with the object we want a part of, our `surveys` data frame
* Then the `$` with no spaces around it
* The the name of the piece that we want, in our case, the column name
* Let's get the `species_id` column 

```r
surveys$species_id
```

* We can also do this using `[]`
* Remember that `[]` also mean "give me a piece of something"
* To extract a column as a vector we use two sets of `[]`
* So to extract the `species_id` column

```r
surveys[["species_id"]]
```

* "species_id" has to be in quotes because we we aren't using `dplyr`
* We have to use two sets of square brackets because one set gives us the column back as a data frame with one column

```r
surveys[["species_id"]]
```

### Combining vectors to make a data frame

* We can also combine vectors to make a data frame
* We'll use an example with vectors that contain data on sites and population densities

```r
sites <- c("a", "a", "b", "c")
density <- c(2.8, 3.2, 1.5, 3.8)
```

* We can make a data frame using the `data.frame` function
* It takes one argument for each column in the data frame
* So we give it the arguments `sites`, and `density`

```r
density_data <- data.frame(sites, density)
```

* If we look in the `Global Environment` we can see that there is a new data frame called `density_data` and it has our two vectors as columns

* We can also add columns to the data from that only include a single value without first creating a vector
* We do this by providing a name for the new column, an equals sign, and the value that we want to occur in every row
* For example, if all of this data was collected in the same year and we wanted to add that year as a column in our data frame we could do it like this

```r
density_data_year <- data.frame(year = 2000, sites, density)
```

* `year =` sets the name of the column in the data frame
* And 2000 is that value that will occur on every row of that column
* If we run this and look at the `density_data_year` data frame we'll see that it includes the year column with `2000` in every row 

### Summary

* So, that's the basic idea behind how vectors and data frames are related and how to convert between them.
* A data frame is a set of equal length vectors
* We can extract a column of a data frame into a vector using either `$` or two sets of `[]`
* We can combine vectors into data frames using the `data.frame` function, which takes a series of arguments, one vector for each column we want to create in the data frame.