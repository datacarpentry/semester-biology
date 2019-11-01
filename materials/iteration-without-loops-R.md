---
layout: page
element: notes
title: Iteration without Loops in R
language: R
---

### Repetition

* Computers are great at doing things repeatedly
* We've learned to use functions to find mass for one volume

```r
est_mass <- function(volume){
  mass <- 2.65 * volume^0.9
  return(mass)
}

est_mass(1.6)
```

* Easy to find mass for other volumes

```r
est_mass(5.6)
est_mass(3.1)
```

* But, this is tedious, error-prone, and impossible for large n
* Multiple ways to do something repeatedly in R
  * Vectorize
  * Apply/Map
  * dplyr + functions
  * Loop

### Vectorize

* Write functions that take a vector of values, do elementwise calculations, and return a vector of the results
* Any function that only uses calculations that are vectorized
* E.g., vector math
* Our current function already works on a vector

```r
est_mass <- function(volume){
  mass <- 2.65 * volume ^ 0.9
  return(mass)
}

volumes = c(1.6, 5.6, 3.1)
est_mass(volumes)
```

* Many functions in R are vectorized

```r
library(stringr)

str_to_upper("tree")
plant_types <- c("tree", "grass", "tree")
str_to_upper(plant_types)
```

* Work on vectors or lists (sometimes columns of data frames)

```r
plant_data <- data.frame(volumes, plant_types)
str_to_upper(plant_data["plant_types"])
str_to_upper(plant_data$plant_types)
plant_data$veg_type_upper = toupper(plant_data$plant_types)
```

> Do [Vectorized Genus Extraction]({{ site.baseurl }}/exercises/Loops-vectorized-genus-extraction-R).

### Apply/Map functions

* Use `apply()` and `map()` functions
* Take a function
* Apply it to each item in a list of items
* Return a list of the same size
* Doesn't require calculations to work on vectors

#### sapply & lapply

* Work on a single vector or list

```r
sapply(X = volumes, FUN = est_mass)
```

* Same as

```r
c(est_mass(volumes[1]), est_mass(volumes[2]), est_mass(volumes[3]))
```

* Do same action on many things with single line of code

* The `s` in `sapply` stands for "simplify"
* It will try to return the simplest object possible, in this case a vector
* `lapply` returns a "list"

```r
lapply(X = volumes, FUN = est_mass)
```

> Do [Vectorized Genus Extraction]({{ site.baseurl }}/exercises/Loops-species-name-capitalization-apply-R).

#### Other apply functions

* Handful of similar functions in `apply()` family
* Differ depending on type of input and output data

* `mapply()` for functions with multiple arguments
* Vegetation type specific equations

```r
est_mass_type <- function(volume, veg_type){
  if (veg_type == "tree"){
    mass <- 2.65 * volume^0.9
  } else {
    mass <- NA
  }
  return(mass)
}

est_mass_type(1.6, "tree")
est_mass_type(volumes, plant_types) # Warning & wrong result
```

* Doesn't vectorize, due to conditionals
* Use an `apply` function instead
* `mapply()` because "multiple" inputs

```r
mapply(FUN = est_mass_type, volume = volumes, veg_type = plant_types)
```

* First argument is function
* All other arguments are named arguments for the function

> Do [Size Estimates Vectorized 1-2]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R/).

* `map` functions from `purrr` package are similar to apply

#### apply (**optional**)

* `apply()` works on multi-dimensional data
* Set `MARGIN` to tell it which dimension to calculate along
* `1` for rows
* `2` for columns

```r
counts = data.frame(sp1 = c(5, 4, 7, 6), sp2 = c(6, 2, 6, 9), sp3 = c(8, 16, 1, 0))
counts
apply(X = counts, MARGIN = 1, FUN = sum)
apply(X = counts, MARGIN = 2, FUN = sum)
```

### Integrating with `dplyr`

#### One result per row

* Remember our data frame

```r
plant_data
```

* Directly use vectorized functions with `mutate`

```r
mutate(plant_data, masses = est_mass(volumes))
```

* Use `rowwise`

```r
plant_data %>%
  rowwise() %>%
  mutate(masses = est_mass_type(volumes, plant_types))
```

> Do [Size Estimates By Name]({{ site.baseurl }}/exercises/Loops-size-estimates-by-name-apply-R/).

#### One result per group

* Custom summarizing functions also work with `dplyr`
* Need to take a vector as input and return a single value as output

```r
get_biomass <- function(volumes){
  masses <- est_mass(volumes)
  biomass <- sum(masses)
  return(biomass)
}

plant_data %>%
  group_by(plant_types) %>%
  summarize(biomass = get_biomass(volumes))
```
