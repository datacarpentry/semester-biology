---
layout: page
element: notes
title: Vectors
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

> Do [Basic Vectors]({{ site.baseurl }}/exercises/Vectors-basic-vectors-R/).

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

> Do [Nulls in Vectors]({{ site.baseurl }}/exercises/Vectors-nulls-in-vectors-R/).

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
