---
layout: exercise
topic: Loops
title: Size Estimates By Name Loop
language: R
---

If `dinosaur_lengths.csv` is not already in your working directory download a copy of the [data on dinosaur lengths with species names]({{ site.baseurl }}/data/dinosaur_lengths.csv). Load it into R.

The following function estimates a dinosaur’s mass based on its length and name of its taxonomic group:

```r
get_mass_from_length_by_name <- function(length, name){
  if (name == "Stegosauria"){
    mass = 10.95 * length ^ 2.64
  }
  else if (name == "Theropoda"){
    mass = 0.73 * length ^ 3.63
  }
  else if (name == "Sauropoda"){
    mass = 214.44 * length ^ 1.46
  }
  else {
    mass = NA
  }
  return(mass)
}
```

Update this function so that instead of returning `NA` when none of the species names matches it returns `mass = 25.37 * length ^ 2.49` instead.

1. Use this function and a for loop to calculate the estimated mass for each dinosaur in `dinosaur_lengths`, store the masses in a vector, and after all of the calculations are complete show the first few items in the vector using `head()`.
2. Add the results in the vector back to the original data frame and display  the new data frame.
3. Calculate the mean mass for each `species` using `dplyr`, using the data from you created in (2).
4. Use `ggplot2` to make a histogram of the masses from (2) with a separate subplot for each `species` (using `facet_wrap()`).
