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
sites <- c("a", "a", "b", “c”)
```

* Functions:
    * `str(sites)` 
    * `length(sites)`
	
* Slicing:
    * `sites[1]` 
    * `sites[1:3]`
        * `1:3` makes a vector. So, this is the same as
    * `sites[c(1, 2, 3)]` 
    * `sites[c(4, 1, 3)]`
        * You can use a vector to get any subset or order you want


* Math functions:

```
density_ha <- c(2.8, 3.2, 1.5, 3.8)
mean(density_ha)
max(density_ha)
min(density_ha)
sum(density_ha)
```

> Do [Bird Banding 1-4]({{ site.baseurl }}/exercises/Vectors-shrub-volume-vectors-R/).

### Working with multiple vectors

* Vector math combines values in the same position
* Element-wise: operating on one element at a time

```
density_ha <- c(2.8, 3.2, 1.5, 3.8)
area_ha <- c(3, 5, 1.9, 2.7)
total_number <- density_ha * area_ha
```

* Subsetting:
    * `total_number[sites == 'a']`
        * `==` means "equal to" in most languages. 
        * Not `=`. `=` is used for assignment.
        * `!=`, `<`, `>`

> Do [Shrub Volume Vectors]({{ site.baseurl }}/exercises/Vectors-shrub-volume-vectors-R/).


### Matrices (if linear algebra folks)

* A two-dimensional set of values with a single data type

```
x <- matrix(1:6, 2)
y <- matrix(1:3, ncol = 1)
x %*% y
```

### Data frames

* A list of equal length vectors grouped together

* `data.frame()`

```
surveys <- data.frame(sites, density_ha, area_ha)
```

* `read.csv()`
    * Main argument is the location of the data - url or path on computer
    * Go to `Datasets` page on site and copy `Shrub dimensions` url
  
```
shrub_data <- read.csv('https://datacarpentry.org/semester-biology/data/shrub-dimensions-labeled.csv')
```

* Useful commands: 
    * `str(surveys)`
    * `length(surveys)`
    * `nrow(surveys)`, `ncol(surveys)`
* Subsetting columns:
    * `surveys[“area_ha”]`
    * `surveys[c(“area_ha”, “sites”)]`
    * `surveys$area_ha`
    * `surveys[[“area_ha”]]`

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

> Start [Shrub Volume Data Frame]({{ site.baseurl }}/exercises/Shrub-volume-data-frame-R/), but just use the url instead of downloading the file.