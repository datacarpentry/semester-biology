---
layout: page
element: notes
title: Data Structures
language: R
--- 

### Vectors

* A sequence of values with the same type
* Create using `c()`, which stands for "combine"

```
sites <- c("a", "a", "b", "c")
```

* `str(sites)` 
	
* Slicing:
    * Use `[]`
    * In general `[]` in R means, "give me a piece of something"
    * `sites[1]` 
    * `sites[1:3]`
        * `1:3` makes a vector. So, this is the same as
    * `sites[c(1, 2, 3)]` 
    * `sites[c(4, 1, 3)]`
        * You can use a vector to get any subset or order you want


* Math functions:

```
length(sites)
density_ha <- c(2.8, 3.2, 1.5, 3.8)
mean(density_ha)
max(density_ha)
min(density_ha)
sum(density_ha)
```

> Do [Bird Banding 1-4]({{ site.baseurl }}/exercises/Vectors-bird-banding-R/).

### Null values

* So far we've worked with data with no missing values
* How many of you have missing values in your data?

```
density_ha <- c(2.8, 3.2, 1.5, NA)
mean(density_ha)
```
* Why did we get `NA`?
    * Hard to say what a calculation including `NA` should be
    * So most calculations return `NA` when `NA` is in the data
* Can tell many functions to remove the `NA` before calculating

```
mean(density_ha, na.rm = TRUE)
```

### Working with multiple vectors

* Vector math combines values in the same position
* Element-wise: operating on one element at a time

```
density_ha <- c(2.8, 3.2, 1.5, 3.8)
area_ha <- c(3, 5, 1.9, 2.7)
total_number <- density_ha * area_ha
```

* Subsetting is done using `[]`, like slicing

```r
area[sites == 'a']
```

* `==` means "equal to" in most languages.
* Not `=`. `=` is used for assignment.

* Can also do "not equal to"

```r
area[sites != 'a']
```

* Greater or less than

```r
sites[area_ha > 3]
sites[area_ha >= 3]
sites[area_ha < 3]
```

* And we can subset a vector based on itself

```r
sites[sites != 'a']
```

> Do [Shrub Volume Vectors 1-3]({{ site.baseurl }}/exercises/Vectors-shrub-volume-vectors-R/).

### Data frames

* A list of equal length vectors grouped together

* `data.frame()`

```
surveys <- data.frame(sites, density_ha, area_ha)
```

* Useful commands: 
    * `str(surveys)`
    * `length(surveys)`
    * `nrow(surveys)`, `ncol(surveys)`
* Subsetting:
    * [row, column]
    * `surveys[1, 2]`
    * `surveys[1:2, 2:3]`
    * `surveys[, 3]`
    * `surveys[“area_ha”]`
    * `surveys[c(“area_ha”, “sites”)]`
    * `surveys$area_ha`
    * `surveys[[“area_ha”]]`


### Reading in external data

* `read.csv()`
    * Main argument is the location of the data - url or path on computer
    * Go to `Datasets` page on site and copy `Shrub dimensions` url
  
```
shrub_data <- read.csv('https://datacarpentry.org/semester-biology/data/shrub-dimensions-labeled.csv')
```

### Factors

```
str(shrub_data)
```

* The `shrubID` column has type `Factor`
* Special data type in R for categorical data
* Useful for statistics, but can mess up some aspects of computation
* Can eliminate during imports with `stringsAsFactors`

```
shrub_data <- read.csv('https://datacarpentry.org/semester-biology/data/shrub-dimensions-labeled.csv', stringsAsFactors = FALSE)
str(shrub_data)
```

> Start [Shrub Volume Data Frame]({{ site.baseurl }}/exercises/Data-frames-shrub-volume-data-frame-R/), but just use the url instead of downloading the file.