---
layout: page
element: notes
title: for loops
language: R
---

> Set up R console:

```
library(stringr)
library(dplyr)
```

### Basic `for` loop

* Repeats action for a number of different values

```
for (item in list_of_items) {
  do_something(item)
}
```

* Make sure you know what values you are calling in your loop.

```
pets <- c("spot", "gigantor", "fluffy")
for (pet in pets) {
  print(pet)
}
```

* Long-form expression of the previous loop

```
pets <- c("spot", "gigantor", "fluffy")
pet <- pets[1]
print(pet)
pet <- pets[2]
print(pet)
pet <- pets[3]
print(pet)
```

* Do more things.

```
pets <- c("spot", "gigantor", "fluffy")
for (pet in pets) {
  class_pet <- paste(pet, "is the name of the class pet")
  print(class_pet)
}
```

> Do [Exercise 4 - for Loop]({{ site.baseurl }}/exercises/Functions-for-loop-R).

> Make sure students get the basics before moving on.

### Storing results

* Create an empty object.
    * `output <- c()`
    * `output <- data.frame()`
    * `output <- data.frame(name = character(3))`
* Add the new values each trip through the loop.

```
pets <- c("spot", "gigantor", "fluffy")
output <- data.frame()
for (pet in pets) {
  pet_upper <- str_to_upper(pet)
  output <- rbind(output, data.frame(name = pet_upper,
                          namelength = str_length(pet_upper)))
}
```

> Assign [Exercise 5 - stringr]({{ site.baseurl }}/exercises/Loops-stringr-R).

### Looping over columns in data frames

```
biomass_data <- data.frame(exper1 = c(24, 32, 62),
                           exper2 = c(10, 9 , 5),
                           exper3 = c(1, 5, 3))

for (exp_biomass in biomass_data) {
  npp <- 19.3 * exp_biomass ** 2
  total_npp <- sum(npp)
  print(total_npp)
}
```

### Alternate loops

* [`apply()`](http://finzi.psych.upenn.edu/R/library/base/html/apply.html)
    * Short cut for simple loops over rows and columns
    * Other versions allow you various control options
        * [`lapply()`](http://finzi.psych.upenn.edu/R/library/base/html/lapply.html): Operate across lists and vectors
        * [`sapply()`](http://finzi.psych.upenn.edu/R/library/base/html/lapply.html): Simplify output to vector
        * [`mapply()`](http://finzi.psych.upenn.edu/R/library/base/html/mapply.html): Pass multiple variables or function arguments
    * Why use `apply()`:
        * Readability
            * Single line of code
            * Simple command structure
        * Speed?
            * Noticeable in complex operations ([some debate](https://stackoverflow.com/questions/2275896/is-rs-apply-family-more-than-syntactic-sugar))
            * [Avoid premature optimization](http://c2.com/cgi/wiki?PrematureOptimization).

```
get_mass_from_length_theropoda <- function(length) {
  mass <- 0.73 * length ** 3.63
  return(mass)
}

lengths = c(5, 10, 15)
lapply(lengths, FUN=get_mass_from_length_theropoda)
sapply(lengths, FUN=get_mass_from_length_theropoda)
```

* Many functions also work with vectors
    * No need to loop through the vector's values

```
get_mass_from_length_theropoda(lengths)
```

* `dplyr`
    * Must have tidy data
    * Use `group_by()` and `summarize()`

```
biomass_data <- data.frame(experiment = c(1, 1, 1, 2, 2, 2, 3, 3, 3),
                           biomass = c(24, 32, 62, 10, 9, 5, 1, 5, 3))

biomass_data %>%
  group_by(experiment) %>%
  summarize(total_npp = sum(19.3 * biomass ** 2))
```

* Indexing

```
pets <- c("spot", "gigantor", "fluffy")
owners <- c("betty", "bob", "joe")
for (i in seq_along(pets)){
  print(paste(pets[i], " is ", owners[i], "'s pet", sep =""))
}
```


* Preallocated memory with indexing

```
pets <- c("spot", "gigantor", "fluffy")
output <- data.frame(name = character(3), namelength = numeric(3),
                     stringsAsFactors = FALSE)
for (i in seq_along(pets)) {
  pet_upper <- str_to_upper(pets[i])
  pet_length <- str_length(pets[i])
  output[i,] <- c(pet_upper, pet_length)
}
```


