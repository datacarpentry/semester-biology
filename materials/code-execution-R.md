---
layout: page
element: notes
title: Code Execution
language: R
---

### Basic code execution

* When we run a chunk of code it runs from top to bottom in order
* It runs the first line, then the second line, and so on
* This means that order is important
* Write code to calculate a total number from density and area

```r
density <- count / area
count <- c(9, 16, 3, 10)
area <- c(3, 5, 1.9, 2.7)
```

* Returns an error because neither `count` or `area` exists yet
* Code executes starting on the right side
* Looks up the value for `count`
* Can't find the variable and so errors

* Rearrange the code so that all variables are created before they are used

```r
count <- c(9, 16, 3, 10)
area <- c(3, 5, 1.9, 2.7)
density <- count / area
```

* This executes in the following sequence
* The right hand side of the first line creates a vector
* It is then stored or "assigned" to the variable `density`
* The second line then runs creating a vector and assigning it to the variable `area`
* The third line first looks up the variable `density` and replaces it with its value
* It then looks up the the variable area and replaces it with its value
* It then multiplies those two vectors and assigns them to the variable `total_number` 
