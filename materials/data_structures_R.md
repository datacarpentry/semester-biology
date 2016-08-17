---
layout: page
element: notes
title: Data Structures
language: R
--- 

### Vectors

* A sequence of values with the same type
* Assignment: 
    * `c()`

``` 
sites <- c("a", "a", "b", "b")
```

* Useful commands: 
    * `str(sites)` 
    * `length(sites)`
* Slicing: 
    * `sites[1]` 
    * `sites[1:3]`
        * `1:3` makes a vector. So, this is the same as
    * `sites[c(1, 2, 3)]` 
        * You can use a vector to get any subset or order you want
* Math:
    * `sum()`
    * `max()`

```
counts <- c(0, 2, 2, 6)
weights <- c(1.5, 2.6, 8.4, 0.2)
total_weight <- sum(weights)
```

* Subsetting:
    * `counts[sites == 'a']`
        * `==` means "equal to" in most languages. 
        * Not `=`. `=` is used for assignment.
        * `!=`, `<`, `>`

> Do [Exercise 1 - Basic Expressions]({{ site.baseurl }}/exercises/Expressions-and-variables-basic-expressions-R/).

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
* Subsetting rows: 
    * `subset(surveys, sites == 'a')`
* Subsetting values/blocks: 
    * `surveys[1,2]` 
    * `surveys[1:2,1:3]`

> Do [Exercise 3 - More Variables]({{ site.baseurl }}/exercises/Expressions-and-variables-more-variables-R/).

> Assign remaining exercises.
