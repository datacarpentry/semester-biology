---
layout: exercise
topic: Making Choices
title: Choice Operators
language: R
---

Create the following variables.

```r
w <- 10.2
x <- 1.3
y <- 2.8
z <- 17.5
colors <- c("red", "blue", "green")
dna1 <- "attattaggaccaca"
dna2 <- "attattaggaacaca"
```

Use them to print whether or not the following statements are `TRUE` or `FALSE`.

1. `w` is greater than 10
2. `"green"` is in `colors`
3. `x` is greater than `y`
4. `w` is greater than `x`, or `x` is greater than `y`
5. `x` times `w` is between 13.2 and 13.5 (there is no way to indicate "between" in R so to do this we have to separately check if the number is greater than the minimum value and less than the maximum value, combining these two conditions with `&`)
6. `z` is `NA`
7. `z` is not `NA`
8. `dna1` is the same as `dna2`
9. `dna1` is not the same as `dna2`
