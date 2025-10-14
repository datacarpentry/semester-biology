---
layout: exercise
topic: Loops
title: Size Estimates By Name Apply
language: R
---

If the [data on dinosaur lengths with species names]({{ site.baseurl }}/data/dinosaur_lengths.csv) is not in your working directory then download it. Import it using `read_csv()`.

The following function estimates a dinosaur's mass based on its length and name of its taxonomic group:

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

1. Copy this function into your code and then use this function and `mapply()` to calculate the estimated mass for each dinosaur.
You'll need to pass the data to `mapply()` as single vectors or columns, not the whole data frame.

2. Using `dplyr`, add a new `masses` column to the data frame (using `rowwise()`, `mutate()` and your function) and print the result to the console.

3. Using `ggplot`, make a histogram of dinosaur masses with one subplot for each species (using `facet_wrap()`).
