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
* Let's take a look at an example using the `stringr` package, which makes work with strings or characters easier

```r
library(stringr)
```

* `stringr` has a `str_to_sentence()` function that will capitalize the first letter of the first word in a sentence
* We could use this to capitalize the first letter of a genus like we typically want to do

```r
str_to_sentence("dipodomys")
```

* This function is vectorized so it automatically works on vectors of strings

```r
str_to_sentence(c("dipodomys", "chaetodipus"))
```

* Let's say we had data on genus and species stored separately

```r
genus <- c("dipodomys", "chaetodipus", "dipodomys")
species <- c("ordii", "baileyi", "spectabilis")
```

* And we want to combine these into a single set of values that combine separate `genus` and `species` vectors and capitalize the first letter of each genus
* We'll do this by writing a function that combines `str_to_sentence()` with another vectorized function `paste()` 

```r
combine_genus_species <- function(genus, species) {
  genus_cap <- str_to_sentence(genus)
  genus_species <- paste(genus_cap, species)
  return(genus_species)
}
```

* Since all of the functions used inside of `combine_genus_species` are vectorized, we can run this function on our vectors

```r
combine_genus_species(genus, species)
```

* We can also use it with data frames by sending the columns of a data frame to the function

```r
data <- data.frame(genus, species)
combine_genus_species(data$genus, data$species)
```

> Do [Vectorized Genus Extraction]({{ site.baseurl }}/exercises/Loops-vectorized-genus-extraction-R).

### Apply/Map functions

* Use `apply()` and `map()` functions
* Take a function
* Apply it to each item in a list of items
* Return a list of the same size
* Doesn't require calculations to work on vectors

* Let's look at this with a version of our function that only calculates mass for volumes greater than a minimum size

```r
est_mass <- function(volume){
  if (volume > 5) {
    mass <- 2.65 * volume ^ 0.9
  } else {
    mass <- NA
  }
  return(mass)
}
```

* If we try to run this function on our volume it won't work because the `if` statements are designed for a single value, not a vector

```r
est_mass(volumes)
```

* Instead we can use one of the `apply()` functions

#### sapply & lapply

* We'll start with `sapply()` and `lapply()`
* These functions take two arguments
* The first is a single vector (or list)
* The second is the function that we want to "apply" to each element of that vector (or list)
* So if we use our `volumes` vector and our new `est_mass()` function
* The `sapply()` will run the `est_mass` function on each value in `volumes`, one value at a time

```r
sapply(X = volumes, FUN = est_mass)
```

* Under the surface this is that same as running our `est_mass()` function on the first item in `volumes`
* Then running it on the second value in `volumes` and then the third value in `volumes`
* And the storing those values together in a vector

```r
c(est_mass(volumes[1]), est_mass(volumes[2]), est_mass(volumes[3]))
```

* This lets us do the same action on many things with single line of code

* The `s` in `sapply` stands for "simplify"
* It will try to return the simplest object possible, in this case a vector
* `lapply` returns a "list"

```r
lapply(X = volumes, FUN = est_mass)
```

* This is a more complicated, but also more flexible, data structure that we don't see much in this class, but it's useful to know the difference between `lapply` and `sapply`.

> SOMETHING SIMPLER THAT DOESN'T REQUIRE USING REGEX HERE Do [Vectorized Genus Extraction]({{ site.baseurl }}/exercises/Loops-species-name-capitalization-apply-R).

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
