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

```r
states <- c("FL", "FL", "GA", "SC")
```

* Using the `str` function we learned last time shows that this is a vector of 4 character strings

```r
str(states)
```

* Select pieces of a vector by slicing the vector (like slicing a pizza)
* Use square brackets `[]`
* In general `[]` in R means, "give me a piece of something"
* `states[1]` gives us the first value in the vector
* `states[1:3]` gives us the first through the third values
* `1:3` works by making a vector of the whole numbers 1 through 3.
* So, this is the same as `states[c(1, 2, 3)]`
* You can use a vector to get any subset or order you want `states[c(4, 1, 3)]`

* Many functions in R take a vector as input and return a value
* This includes the function `length` which determines how many items are in a vector

```r
length(states)
```

* We can also calculate common summary statistics
* For example, if we have a vector of population counts

```r
count <- c(9, 16, 3, 10)
mean(count)
max(count)
min(count)
sum(count)
```

> Do Exercise 6 - [Basic Vectors]({{ site.baseurl }}/exercises/Vectors-basic-vectors-R/).

### Null values

* So far we've worked with vectors that contain no missing values
* But most real world data has values that are missing for a variety of reasons
* For example, kangaroo rats don't like being caught by humans and are pretty good at escaping before you've finished measuring them
* Missing values, known as "null" values, are written in R as `NA` with no quotes, which is short for "not available"
* So a vector of 4 population counts with the third value missing would look like

```r
count_na <- c(9, 16, NA, 10)
```

* If we try to take the mean of this vector we get `NA`?

```r
mean(count_na)
```

* Hard to say what a calculation including `NA` should be
* So most calculations return `NA` when `NA` is in the data
* Can tell many functions to remove the `NA` before calculating
* Do this using an optional argument, which is an argument that we don't have to include unless we want to modify the default behavior of the function
* Add optional arguments by providing their name (`na.rm`), `=`, and the value that we want those arguments to take (`TRUE`)

```r
mean(count_na, na.rm = TRUE)
```

* We need the name because `na.rm` isn't the second argument, so if we just put `TRUE` we get an error

```r
mean(count_na, TRUE)
```

> Do [Nulls in Vectors]({{ site.baseurl }}/exercises/Vectors-nulls-in-vectors-R/).

### Working with multiple vectors

* Add information on area to our information on states and population counts

```r
states <- c("FL", "FL", "GA", "SC")
count <- c(9, 16, 3, 10)
area <- c(3, 5, 1.9, 2.7)
```

#### Vector math

* Perform the same mathematical operation on each value in a vector by treating it like we would a single value
* So if we wanted to double all of the values in the `area` vector

```r
area * 2
```

* When we run this, R multiplies the first value in the vector by 2, then multiplies the second value in the vector by 2, and so on
* Element-wise: operating on one element at a time

* Remember - this isn't saved unless we store it
* So `area` hasn't changed

```r
area
```

* To keep the results of the calculation store them in a new variable

```r
doubled_area <- area * 2
doubled_area
```

* We can also do element-wise math with multiple vectors of the same length
* Let's divide the count vector by the area vector to get a vector of the density of individuals in that area

```r
density <- count / area
```

* When we divide the two vectors, R divides the first value in the first vector by the first value in the second vector, then divides the second values in each vector, and so on
* Element-wise: operating on one element at a time

#### Filtering

* Subsetting or "filtering" is done using `[]`
* Like with slicing, the `[]` say "give me a piece of something"
* Selects parts of vectors based on "conditions" not position
* Get the density values for sites in Florida

```r
density[states == 'FL']
```

* `==` is how we indicate "equal to" in most programming languages.
* Not `=`. `=` is used for assignment.

* Can also do "not equal to"

```r
density[states != 'FL']
```

* Numerical comparisons like greater or less than
* Select states that meet conditions related to density

```r
states[density > 3]
states[density < 3]
states[density <= 3]
```

* Can subset a vector based on itself
* If we want to look at the densities greater than 3
* `density` is both the vector being subset and part of the condition

```r
density[density > 3]
```

> Do [Shrub Volume Vectors 1-3]({{ site.baseurl }}/exercises/Vectors-shrub-volume-vectors-R/).

* What's actually happening when we subset vectors this way?
* Let's look at the piece of the code inside the `[]`

```r
density > 3
```

* This does an element-wise check to see if each value is > 3
* If it is the result is `TRUE`, if not it is `FALSE`
* The `density[]` part of the code then keeps those values in the `density` vector where this inner vector is `TRUE`
* You don't need to remember this last piece now, we'll come back to it
