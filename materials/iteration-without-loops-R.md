---
layout: page
element: notes
title: Iteration without Loops in R
language: R
---

### Repetition

* Computers are great at doing things repeatedly
* We've learned to use functions to find mass for one volume

```
est_mass <- function(volume){
  mass <- 2.65 * volume^0.9
  return(mass)
}

est_mass(1.6)
```

* Easy to find mass for other volumes

```
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

* Write functions that take a vector of values & return a vector
* Use only calculations that are vectorized
* E.g., vector math
* Our current function already works on a vector

```
est_mass <- function(volume){
  mass <- 2.65 * volume ^ 0.9
  return(mass)
}

est_mass(c(1.6, 5.6, 3.1))
```

* Many things in R are vectorized

### Apply/Map functions

* Use `apply()` and `map()` functions
* Take a function
* Apply it to each item in a list
* Return a list of the same size
* Doesn't require calculations to work on vectors


#### sapply

```
plant_vols <- c(1.6, 5.6, 3.1)
sapply(plant_vols, est_mass)
```

* Do same action on many things with single line of code! 
* Easily scales up

#### Other apply functions

* Handful of similar functions in `apply()` family
* Differ depending on type of input and output data
* `lapply()`like `sapply()` but returns list

```
lapply(plant_vols, est_mass)
```

* `apply()` works on multi-dimensional data
* `mapply()` for functions with multiple arguments

* Vegetation type specific equations

```
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

```
mapply(est_mass_type, volume = plant_vols, veg_type = plant_types)
```

* First argument is function, rest are function arguments
* Use `map` functions from `purrr` package are similar to apply

> Do [Use and Modify with Apply]({{ site.baseurl }}/exercises/Loops-use-modify-apply-R).


### Integrating with `dplyr`

```
plant_data <- data.frame(volume = plant_vols, veg_type = plant_types)
```

* Directly use vectorized functions with `mutate`

```
mutate(plant_data, masses = est_mass(volume))
```

* Use apply functions and add the results as a new column

```
masses = mapply(est_mass_type,
                volume = plant_data$volume,
                veg_type = plant_data$veg_type)
plant_data$masess = masses
```

* Use `rowwise`

```
plant_data %>%
  rowwise() %>%
  mutate(masses = est_mass_type(volume, veg_type))
```

> Do [Crown Volume Calculation]({{ site.baseurl }}/exercises/Loops-crown-volume-calculation-R).