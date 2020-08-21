---
layout: page
element: notes
title: Vectors
language: R
--- 

### Vectors Basics

* Remember that all values in R have a type
* A vector is a sequence of values that all have the same type
* Create using the `c()` function, which stands for "combine"

```
sites <- c("a", "a", "b", "c")
```

* Using the `str` function we learned last time shows that this is a vector of 4 character strings 

```
str(sites)
```

* Select pieces of a vector by slicing the vector (like slicing a pizza)
* Use square brackets `[]`
* In general `[]` in R means, "give me a piece of something"
* `sites[1]` gives us the first value in the vector
* `sites[1:3]` gives us the first through the third values
* `1:3` works by makeing a vector of the whole numbers 1 through 3.
* So, this is the same as `sites[1:3]` is the same as `sites[c(1, 2, 3)]` 
* You can use a vector to get any subset or order you want `sites[c(4, 1, 3)]`

* Many functions in R take a vector as input and return a value
* This includes the function `length` which determines how many items are in a vector

```
length(sites)
```

* We can also calculate common summary statistics
* For example, if we have a vector of population densities

```
density <- c(2.8, 3.2, 1.5, 3.8)
mean(density)
max(density)
min(density)
sum(density)
```

> Do [Basic Vectors]({{ site.baseurl }}/exercises/Vectors-basic-vectors-R/).

### Null values

* So far we've worked with vectors that contain no missing values
* But most real world data has values that are missing for a variety of reasons
* For example, kangaroo rats don't like being caught by humans and are pretty good at escaping before you've finished measuring them
* Missing values, known as "null" values, are written in R as `NA` with no quotes
* So a vector of 4 population densities with the third value missing would look like

```
density <- c(2.8, 3.2, NA, 3.8)
```

* If we try to take the mean of this vector we get `NA`?

```
mean(density)
```

* Hard to say what a calculation including `NA` should be
* So most calculations return `NA` when `NA` is in the data
* Can tell many functions to remove the `NA` before calculating

```
mean(density, na.rm = TRUE)
```

* Null values are how we indicate missing data in R
* We write nulls using `NA`
* Can remove them in many calculations using the optional argument `na.rm = TRUE`

> Do [Nulls in Vectors]({{ site.baseurl }}/exercises/Vectors-nulls-in-vectors-R/).

### Working with multiple vectors

* Build on example where we have information on sites and population densities by adding areas

```
sites <- c("a", "a", "b", "c")
density <- c(2.8, 3.2, 1.5, 3.8)
area <- c(3, 5, 1.9, 2.7)
```

#### Vector math

* Vector math combines values in the same position
* Element-wise: operating on one element at a time

* We can multiple the density and area vectors together to get a vector of the number of individuals we expect in that area

```
number <- density * area
```

* This works because when we multiply vectors, R multiples the first values in each vector, then multiplies the second values in each vector, and so on

#### Filtering

* Subsetting or "filtering" is done using `[]`
* Like with slicing, the `[]` say "give me a piece of something"
* Selects parts of vectors based on "conditions" not position
* Get the density values in site a

```r
density[sites == 'a']
```

* `==` is how we indicate "equal to" in most programming languages.
* Not `=`. `=` is used for assignment.

* Can also do "not equal to"

```r
density[sites != 'a']
```

* Numerical comparisons like greater or less than
* Select sites that meet with some restrictions on density

```r
sites[density > 3]
sites[density < 3]
sites[density <= 3]
```

* Can subset a vector based on itself
* If we want to look at the densities greater than 3
* `density` is both the vector being subset and part of the condition

```r
density[density > 3]
```

* Multiple vectors can be used together to perform element-wise math, where we do the same calculation for each position in the vectors
* We can also filter the values in vector based on the values in another vector or itself

> Do [Shrub Volume Vectors 1-3]({{ site.baseurl }}/exercises/Vectors-shrub-volume-vectors-R/).
