---
layout: page
element: notes
title: Iteration without Loops in R
language: R
---

### Repetition in R

* Computers are great at doing things repeatedly
* We've learned to use functions to find mass for one volume

```r
est_mass <- function(volume){
  mass <- 2.65 * volume^0.9
  return(mass)
}

est_mass(1.6)
```

* This makes it easier to find mass for other volumes

```r
est_mass(5.6)
est_mass(3.1)
```

* But, this is tedious, error-prone, and impossible for large numbers of volumes
* There are multiple ways to do something repeatedly in R and we'll talk about all of them over the next several lessons
* These include
  * Vectorize - where we right functions that take a vector of values, do elementwise calculations, and return a vector of results
  * Using Apply/Map - which takes a function and applies it to each item in a list of items
  * Combining our own functions with dplyr - which we can do using both vectorized and non-vectorized functions
  * Loops - which provide us with complete control to perform of any kind of repetition we want

### Vectorize

* Write functions that take a vector of values, do elementwise calculations, and return a vector of the results
* Any function that only uses calculations that are vectorized
* E.g., vector math

```r
c(1, 2, 3) * 2
```

* Our current function already works on a vector

```r
est_mass <- function(volume){
  mass <- 2.65 * volume ^ 0.9
  return(mass)
}

volumes = c(1.6, 5.6, 3.1)
est_mass(volumes)
```

* Many functions in R are vectorized which means that we can often repeated things using only this vectorization
* We can also use use vectorized functions with data frames by sending the individual columns of a data frame to the function

```r
data <- data.frame(volumes, plant_id = c(1, 2, 3))
data
est_mass(data$volumes)
est_mass(data[['volumes']])
```

> Do [Size Estimates Vectorized 1]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R).

#### Multiple Arguments

* Let's modify our function to take the coefficient (the value that is currently set as 2.65) as an argument
* We'll call it `a`

```r
est_mass_coef <- function(volume, a){
  mass <- a * volume ^ 0.9
  return(mass)
}

est_mass_coef(volumes, 2.56)
```

* Because we only provided a single value of `a`, that value gets used for every value of `volume` when doing the calculation
* But multiplication is also vectorized for two vectors

```r
c(1, 2, 3) * c(1, 2, 3)
```

* So we can also pass the function a vector of values for `a`

```r
as <- c(2.56, 1, 3.2)
est_mass_coef(volumes, as)
```

#### Integrating with `dplyr`

* We can also integrate our vectorized functions with `dplyr`
* This lets us use them to repeat calculations for each row in a data frame
* Let's convert our `volume` and `as` vectors into a data frame

```r
plant_data = data.frame(volume = volumes, a = as)
```

* To apply vectorized functions to each row in a table we can use `mutate`

```r
plant_data |>
  mutate(masses = est_mass_coef(volume, a))
```

* This is just like we've seen using other R functions, but it works with the vectorized functions we write as well

> Do [Size Estimates Vectorized 2-3]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R).


### Apply/Map functions

* Not all functions in R are vectorized
* So we need a way to repeatedly run these non-vectorized functions
* Use `apply()` and `map()` functions
* We'll learn the `apply` family of functions since they are very common, but `map` is a very similiar tidyverse option

* These functions take two arguments
* The first is a vector of values that we want to run a function on
* The second is the function that we want to run on each value in the vector
* The `apply` functions then "apply" the function each item in the vector
* Return a list of the same size
* Doesn't require calculations to work on vectors

* Let's look at this with a version of our function that only calculates mass for volumes less than a maximum size

```r
est_mass_max <- function(volume){
  if (volume < 5) {
    mass <- 2.56 * volume ^ 0.9
  } else {
    mass <- NA
  }
  return(mass)
}
```

* If we try to run this function on our volume it won't work because the `if` statements are designed for a single value, not a vector

```r
est_mass_max(volumes)
```

* Instead we can use one of the `apply()` functions

#### sapply & lapply

* We'll start with `sapply()`
* This function take two arguments
* The first is a single vector
* The second is the function that we want to "apply" to each element of that vector (or list)
* So if we use our `volumes` vector and our new `est_mass_max()` function
* `sapply()` will run the `est_mass_max` function on each value in `volumes`, one value at a time

```r
sapply(volumes, est_mass_max)
```

* Under the surface this is that same as running our `est_mass()` function on the first item in `volumes`
* Then running it on the second value in `volumes` and then the third value in `volumes`
* And the storing those values together in a vector

```r
c(est_mass_max(volumes[1]), est_mass_max(volumes[2]), est_mass_max(volumes[3]))
```

* This lets us do the same action on many things with single line of code

* Handful of similar functions in `apply()` family
* Differ depending on type of input and output data
* The `s` in `sapply` stands for "simplify"
* It will try to return the simplest object possible, in this case a vector
* `lapply` returns a "list"

```r
lapply(volumes, est_mass_max)
```

* This is a more complicated, but also more flexible, data structure that we don't see much in this class, but it's useful to know the difference between `lapply` and `sapply`.
* We can store anything in a list, so if you had a function that made a bunch of graphs or a bunch of data frames `lapply` would let you work with them
* Likewise both of these functions can also take a list as input allowing you to accomplish more complicated things

> Do [Size Estimates With Maximum]({{ site.baseurl }}/exercises/Loops-size-estimates-with-maximum-R).

#### Apply with multiple arguments

* `mapply()` for functions with multiple arguments
* Vegetation type specific equations

```r
est_mass_type <- function(veg_type, volume){
  if (veg_type == "shrub"){
    mass <- 2.65 * volume^0.9
  } else {
    mass <- NA
  }
  return(mass)
}

est_mass_type(1.6, "shrub")
plant_types = c("shrub", "tree", "shrub")
est_mass_type(plant_types, volumes) # Error
```

* Doesn't vectorize, due to conditionals
* Use an `apply` function instead
* `mapply()` because "multiple" inputs

```r
mapply(est_mass_type, plant_types, volumes)
```

* First argument is function
* All other arguments are arguments for the function
* Names in the output, come from the first vector if it has names or is a char vector
* Can remove them using `USE.NAMES = FALSE`

```r
mapply(est_mass_type, plant_types, volumes, USE.NAMES = FALSE)
```

> Do Task 1 in [Size Estimates By Name Apply]({{ site.baseurl }}/exercises/Loops-size-estimates-by-name-apply-R/).

* `map` functions from `purrr` package are similar to apply

#### Integrating with dplyr

* Let's update our `plant_data` data frame to include our plant types

```r
plant_type_data = data.frame(volume = volumes,
                        plant_type = plant_types)
```

* The basic integration with dplyr we used for vectorized functions won't work with non-vectorized functions

```r
plant_type_data |>
  mutate(masses = est_mass_type(volume, plant_type))
```

* Error because `est_mass_type` isn't vectorized
* By default `dplyr` runs this function by converting the individual columns to vectors and running the function on those vectors
* Just like when we tried to run the function on the vectors
* To get around this we add the function `rowwise` to our `dplyr` pipeline
* This tells `dplyr` to work with the data one row at a time, like an `apply` function

```r
plant_data |>
  rowwise() |>
  mutate(masses = est_mass_type(volumes, plant_types))
```

> Do Task 2 in [Size Estimates By Name Apply]({{ site.baseurl }}/exercises/Loops-size-estimates-by-name-apply-R/).

#### One result per group

* We can also combine functions with `group_by` and `summarize` to repeat a calculation for each group
* These functions need to take a vector as input and return a single value as output
* So, let's write a function that calculates the biomass (the sum of the individual masses) for each plant type

```r
get_biomass <- function(volumes){
  masses <- est_mass(volumes)
  biomass <- sum(masses)
  return(biomass)
}
```

* This function takes a vector of volumes as input and returns a single value, the biomass
* We can then group our data by `plant_types`
* And summarize by our function to calculate the biomass for each group

```r
plant_data |>
  group_by(plant_types) |>
  summarize(biomass = get_biomass(volumes))
```

#### Using lapply with files and data frames (**optional**)

* `lapply()` will always return a list
* We can store anything we want in a list
* Let's download some (made up) satellite collar data where the data for each collar is stored in one file

```r
download.file("https://www.datacarpentry.org/semester-biology/data/locations.zip",
              "locations.zip")
unzip("locations.zip")
data_files = list.files(pattern = "locations-")
```

* Since we can store anything in a list we can store entire data frames
* Use `lapply()` to load all of the files into data frames

```r
library(readr)

data_frames = lapply(data_files, read_csv)
```

* We applied the `read_csv()` function to each data file
* And get back a list of data frames
* Now we can use `lapply()` again to do something to each data frame

```r
library(readr)

get_unique_locations <- function(df){
  unique_locations <- df |>
    select(lat, long) |>
    distinct()
  return(unique_locations)
}

unique_locations <- lapply(data_frames, get_unique_locations)
```

#### Other apply functions (**optional**)

* There are a few other apply functions
* `vapply()` works like `sapply()`, but you have to tell it what type the returned vector will be
* `tapply()` works like `sapply()`, but lets you provide a single grouping field (kind of like `group_by()` in dplyr)

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
