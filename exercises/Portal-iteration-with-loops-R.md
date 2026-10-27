---
layout: exercise
topic: Loops
title: Portal Data Iteration With Loops
language: R
---

This exercise revisits some of the functions from [Portal Data Iteration Without Loops]({{ site.baseurl }}/exercises/Portal-iteration-without-loops-R), but this time you'll use `for` loops to do the iteration.

If [surveys.csv](https://ndownloader.figshare.com/files/2292172) is not in your working directory then download it.
Load it using `read_csv`.

The following function classifies an individual based on its weight:

```r
classify_by_weight <- function(weight) {
  if (is.na(weight)) {
    weight_class <- "unknown"
  } else if (weight < 20) {
    weight_class <- "small"
  } else if (weight <= 50) {
    weight_class <- "medium"
  } else {
    weight_class <- "large"
  }
  return(weight_class)
}
```

1\. Use `classify_by_weight` and a `for` loop to determine the weight class for each value in the following vector, store the weight classes in a vector, and after the loop display the vector.

```r
weights <- c(15, 25, 35, 45, NA, 70, 72)
```

2\. Use `classify_by_weight` and a `for` loop to determine the weight class for each individual in `surveys` and store the weight classes in a vector.
Add this vector to `surveys` as a new column named `weight_class` and then use `dplyr` to count the number of individuals in each weight class.

3\. The following function estimates daily energy needs based on an individual's genus and weight:

```r
energy_budget <- function(genus, weight) {
  if (genus == "Dipodomys") {
    energy <- 0.065 * weight ^ 0.75 * 24
  } else if (genus == "Chaetodipus") {
    energy <- 0.080 * weight ^ 0.75 * 24
  } else {
    energy <- 0.073 * weight ^ 0.75 * 24
  }
  return(energy)
}
```

Use `energy_budget` and a `for` loop to estimate the energy budget for each pair of values in the following vectors, store the energy budgets in a vector, and after the loop display the vector.

```r
genera <- c("Dipodomys", "Chaetodipus", "Neotoma", "Dipodomys")
weights <- c(45, 22, 156, 38)
```
