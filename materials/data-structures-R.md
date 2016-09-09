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
sites <- c("a", "a", "b", "b")
```

* Functions:
    * `str(sites)` 
    * `length(sites)`
	
* Slicing:
    * `sites[1]` 
    * `sites[1:3]`
        * `1:3` makes a vector. So, this is the same as
    * `sites[c(1, 2, 3)]` 
        * You can use a vector to get any subset or order you want

* Math functions:

```
density_ha <- c(2.8, 3.2, 1.5, 3.8)
mean(density_ha)
max(density_ha)
min(density_ha)
sum(density_ha)
```

* Vector math combines values in the same position

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

> Do [Exercise 9 - Shrub Volume 1]({{ site.baseurl }}/exercises/Vectors-shrub-volume-1-R/).


### Matrices (if linear algebra folks)

* A two-dimensional set of values with a single data type

```
x <- matrix(1:6, 2)
y <- matrix(1:3, ncol = 1)
x %*% y
```

### Data frames

* A list of equal length vectors grouped together
* Assignment: 
    * `data.frame()`
    * `read.csv()`

```
surveys <- data.frame(sites, counts, weights)
```

* Useful commands: 
    * `str(surveys)`
    * `length(surveys)`
    * `nrow(surveys)`, `ncol(surveys)`
* Subsetting columns:
    * `surveys["sites"]`
    * `surveys[c("counts", "weights")]`
    * `surveys$sites`
    * `surveys[["sites"]]`


> Assign remaining exercises.
