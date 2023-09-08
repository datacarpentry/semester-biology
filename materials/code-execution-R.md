---
layout: page
element: notes
title: Code Execution
language: R
---

### Code executes top to bottom

* When we run a chunk of code it runs from top to bottom in order
* It runs the first line, then the second line, and so on
* This means that order is important
* Write code to calculate a total number from density and area

```r
density <- number / area
number <- c(9, 16, 3, 10)
area <- c(3, 5, 1.9, 2.7)
```

* Returns an error because neither `number` or `area` exists yet
* Code executes starting on the right side
* Looks up the value for `number `
* Can't find the variable and so errors

* Rearrange the code so that all variables are created before they are used

```r
number <- c(9, 16, 3, 10)
area <- c(3, 5, 1.9, 2.7)
density <- number / area
```

* This executes in the following sequence
* The right hand side of the first line creates a vector
* It is then stored or "assigned" to the variable `density`
* The second line then runs creating a vector and assigning it to the variable `area`
* The third line first looks up the variable `density` and replaces it with its value
* It then looks up the the variable area and replaces it with its value
* It then multiplies those two vectors and assigns them to the variable `total_number` 

### Code executes left to right

> Instructors note: This is a slight fudge since it actually demonstrates that the code is read not executed left to right

* R looks up values and executes code from left to right on a line
* If we accidentally added an `s` to each vector name when calculating density we'll get an error

```r
numbers / areas
```

* The code tries to look up `numbers` and then errors telling use that the variable `numbers` doesn't existing the Environment
* If we switch the order of the line

```r
areas / numbers
```

* The error message tells us that `areas` isn't found and that's because it is the first thing R tries to work with because it is on the left

### Code executes inside to outside

* Code that is enclosed by brackets or parentheses executes before the surrounding code

```r
density[density > 3]
```

* So this line is the same as

```r
density_filter <- density > 3
density[density_filter]
```
