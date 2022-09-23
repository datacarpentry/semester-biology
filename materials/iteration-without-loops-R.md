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

> Do [Size Estimates Vectorized]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R).

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

* We'll start with `sapply()`
* This function take two arguments
* The first is a single vector
* The second is the function that we want to "apply" to each element of that vector (or list)
* So if we use our `volumes` vector and our new `est_mass()` function
* `sapply()` will run the `est_mass` function on each value in `volumes`, one value at a time

```r
sapply(volumes, est_mass)
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
lapply(volumes, est_mass)
```

* This is a more complicated, but also more flexible, data structure that we don't see much in this class, but it's useful to know the difference between `lapply` and `sapply`.
* Both of these functions can also take a list as input allowing you to accomplish more complicated things

> Do [Size Estimates With Maximum]({{ site.baseurl }}/exercises/Loops-size-estimates-with-maximum-R).

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
plant_types = c("shrub", "tree", "tree")
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

> Do Task 1 in [Size Estimates By Name Apply]({{ site.baseurl }}/exercises/Loops-size-estimates-by-name-apply-R/).

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

* We can also integrate both our vectorized and non-vectorized functions with `dplyr`
* This lets us use them to repeat calculations either for each row in a data from or each group using `group_by`
* Let's convert our `volume` and `plant_type` vectors into a data frame

```r
plant_data = data.frame(volumes, plant_type)
```

#### One result per row

* To apply vectorized functions to each row in a table we can use `mutate`

```r
mutate(plant_data, masses = est_mass(volumes))
```

* This is just like we've seen using other R functions, but it works with the vectorized functions we write as well
* This won't work with non-vectorized functions

```r
plant_data %>%
  mutate(masses = est_mass_type(volumes, plant_types))
```

* In our case this is because the conditional attempts to evaluate if the entire column is equal to "tree"
* That doesn't really make sense the `if` statement just checks the first value and returns `NA`
* To get around this we add the function `rowwise` to our `dplyr` pipeline
* This tells `dplyr` to work with the data one row at a time, like an `apply` function

```r
plant_data %>%
  rowwise() %>%
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
plant_data %>%
  group_by(plant_types) %>%
  summarize(biomass = get_biomass(volumes))
```
