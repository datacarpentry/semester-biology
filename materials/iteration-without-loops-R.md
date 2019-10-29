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

est_mass(c(1.6, 5.6, 3.1))
```

* Many functions in R are vectorized

```r
library(stringr)
str_to_upper(c('katherine johnson', 'mary jackson', 'dorothy vaughan'))
```

* Work on vectors or lists (sometimes columns of data frames)

```r
nasa_scientists <- data.frame(name = c('katherine johnson', 'mary jackson', 'dorothy vaughan'),
                              job = c('mathematician', 'engineer', 'mathematician'))
toupper(nasa_scientists["name"])
toupper(nasa_scientists$name)
nasa_scientists$names_upper = toupper(nasa_scientists$name)
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
plant_vols <- c(1.6, 5.6, 3.1)
sapply(X = plant_vols, FUN = est_mass)
```

* Same as

```r
c(est_mass(plant_vols[1]), est_mass(plant_vols[2]), est_mass(plant_vols[3]))
```

* Do same action on many things with single line of code

* The `s` in `sapply` stands for "simplify"
* It will try to return the simplest object possible, in this case a vector
* `lapply` returns a "list"

```r
lapply(X = plant_vols, FUN = est_mass)
```

> Do [Vectorized Genus Extraction]({{ site.baseurl }}/exercises/Loops-species-name-capitalization-apply-R).

#### Other apply functions

* Handful of similar functions in `apply()` family
* Differ depending on type of input and output data

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
plant_types <- c("tree", "grass", "tree")
est_mass_type(plant_vols, plant_types) # Warning & wrong result
```

* Doesn't vectorize, but works with `mapply()`

```r
mapply(FUN = est_mass_type, volume = plant_vols, veg_type = plant_types)
```

* First argument is function, rest are function arguments
* Use `map` functions from `purrr` package are similar to apply

> Do [Use and Modify with Apply]({{ site.baseurl }}/exercises/Loops-use-modify-apply-R).


### Integrating with `dplyr`

```r
plant_data <- data.frame(volume = plant_vols, veg_type = plant_types)
```

* Directly use vectorized functions with `mutate`

```r
mutate(plant_data, masses = est_mass(volume))
```

* Use apply functions and add the results as a new column

```r
masses = mapply(est_mass_type,
                volume = plant_data$volume,
                veg_type = plant_data$veg_type)
plant_data$masess = masses
```

* Use `rowwise`

```r
plant_data %>%
  rowwise() %>%
  mutate(masses = est_mass_type(volume, veg_type))
```

> Do [Crown Volume Calculation]({{ site.baseurl }}/exercises/Loops-crown-volume-calculation-R).