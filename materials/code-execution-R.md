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
density <- number / area
number <- c(9, 16, 3, 10)
area <- c(3, 5, 1.9, 2.7)
```

* Returns an error because neither `number` or `area` exists yet

* Within a line code executes everything before assigning the output to a variable
* So it starts to the right of the assignment operator
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
* It is then stored or "assigned" to the variable `number`
* The second line then runs creating a vector and assigning it to the variable `area`
* The third line first looks up the variable `number` and replaces it with its value
* It then looks up the the variable `area` and replaces it with its value
* It then divides those two vectors and assigns the resulting vector to the variable `density`

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
