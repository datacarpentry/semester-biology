---
layout: page
element: notes
title: for loops
language: R
---

## Basic `for` loops

* Let us do the same thing for a number of different values

```
for (item in list_of_items) {
  commands
}
```

* When you run a for loop the first time through...

### Example

```
pets <- c("spot", "gigantor", "fluffy")
for (pet in pets) {
  paste(pet, "is the name of the class pet")
}
```

What this does:

```
pets <- c("spot", "gigantor", "fluffy")
pet <- pets[1]
paste(pet, "is the name of the class pet")
pet <- pets[2]
paste(pet, "is the name of the class pet")
pet <- pets[3]
paste(pet, "is the name of the class pet")
```

### Storing results

* Create something to store them
* Add your new values each trip through the loop

```
library(stringr)

pets <- c("spot", "gigantor", "fluffy")
output <- data.frame()
for (pet in pets) {
  pet_upper <- str_to_upper(pet)
  output <- rbind(output, data.frame(name = pet_upper,
                          namelength = str_length(pet_upper)))
}
```

### Looping over columns in data frames

```
biomass_data <- data.frame(exper1 = c(24, 32, 62),
                           exper2 = c(10, 9 , 5),
                           exper3 = c(1, 5, 3))

for (exp_biomass in biomass_data) {
  npp <- sum(19.3 * exp_biomass ** 2)
  print(npp)
}
```

***Complete through exercise 4***

## Apply

* Short cuts for simple loops

```
get_mass_from_length_theropoda <- function(length) {
  mass <- 0.73 * length ** 3.63
  return(mass)
}

lengths = c(5, 10, 15)
lapply(lengths, FUN = get_mass_from_length_theropoda)
sapply(lengths, FUN = get_mass_from_length_theropoda)
```

* There are also versions that allow you to pass multiple parameters or operate
  across either rows or columns
* Arguments for apply:
    * speed (avoid premature optimization)
    * readability

* Also keep in mind that many functions in R will be vectorized

```
get_mass_from_length(lengths, as, bs)
```

### MAKE SURE BASICS MAKE SENSE BEFORE COVERING THIS



## Dplyr

* Many kinds of looping over data can also be handled using functions in dplyr

```
estimate_mass <- function(hindfoot_length, weight){
  mass 
}
surveys <- read.csv("surveys.csv")
```

## Indexing

```
pets <- c("spot", "gigantor", "fluffy")
owners <- c("betty", "bob", "joe")
for (i in seq_along(pets)){
  print(paste(pets[i], "is ", owners[i], "'s pet"))
}
```


### Preallocating memory

```
library(stringr)

pets <- c("spot", "gigantor", "fluffy")
output <- data.frame(name = character(3), namelength = numeric(3),
                     stringsAsFactors = FALSE)
for (i in seq_along(pets)) {
  pet_upper <- str_to_upper(pets[i])
  output[i,] <- c(pet_upper, str_length(pet_upper))
}
```
