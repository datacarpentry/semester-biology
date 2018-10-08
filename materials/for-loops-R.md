---
layout: page
element: notes
title: Iteration in R
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

shrub_vol1 <- 1.6
est_mass(shrub_vol1)
```

* Easy to find mass for other volumes

```
shrub_vol2 <- 5.6
est_mass(shrub_vol2)

shrub_vol3 <- 3.1
est_mass(shrub_vol3)
```

* But, this is tedious, error-prone, and impossible for large n
* Three ways to do something repeatedly in R
  * Vectorize
  * Apply/Map
  * Loop

### Vectorize

* Write functions that take a list of values & return a list
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

### Apply/Map functions

* Use `apply()` and `map()` functions are similar
* Don't require calculations to work on vectors

#### sapply

```
shrub_vols <- c(1.6, 5.6, 3.1)
sapply(shrub_vols, est_mass)
```

* Do same action on many things with single line of code! 
* Easily scales up

#### Other apply functions

* Handful of similar functions in `apply()` family
* Differ depending on type of input and output data
* `lapply()`like `sapply()` but returns list

```
lapply(shrub_vols, est_mass)
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
plant_vols <- c(1.6, 3, 8)
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
masses = mapply(est_mass_type, volume = plant_data$volume, veg_type = plant_data$veg_type)
plant_data$masess = masses
```

* Use `rowwise`

```
plant_data %>%
  rowwise() %>%
  mutate(masses = est_mass_type(volume, veg_type))
```

> Do [Crown Volume Calculation]({{ site.baseurl }}/exercises/Loops-crown-volume-calculation-R).


### For loops

> Set up R console:

```
library(stringr)
library(dplyr)
```

#### Basic `for` loop

* Do same action to each component of a list

```
waterbirds <- c("cygnus olor", "aix sponsa", "anas acuta")
waterbird <- waterbirds[1]
print(waterbird)
waterbird <- waterbirds[2]
print(waterbird)
waterbird <- waterbirds[3]
print(waterbird)
```

* This is tedious
* Use for loop to do same action repeatedly
* Easier & fewer errors

```
for (item in list_of_items) {
  do_something(item)
}
```

* Need `print()` to display values inside a loop, function, or conditional.

```
for (waterbird in waterbirds){
  print(waterbird)
}
```

* Do more actions

```
for (waterbird in waterbirds){
  waterbird_cap <- str_to_title(waterbird)
  print(waterbird_cap)
}
```
> Do [Basic Vector]({{ site.baseurl }}/exercises/Loops-basic-vector-R/).


#### Numeric values in `for` loops

* Do functions or math as actions within for loops
* Variable can be given any name, then refer to with that name in loop

```
for (num in 100:150){
  print(num * 10)
}
```

* Use `paste()` to put together strings and variables

```
for (num in 100:150){
  print(paste("My favorite number is", num * 10))
}
```

> Do [Basic Index]({{ site.baseurl }}/exercises/Loops-basic-index-R/) tasks 1-2.

> Do [DNA or RNA Iteration]({{ site.baseurl }}/exercises/Making-choices-dna-or-rna-iteration-R/). 

#### Storing results

* Create an empty object.

```
output <- c()
```

* Iteratively add new values to object. 

```
output <- c(1, 2, 3)
output <- c(output, 4)
```
* Use this method within a `for` loop to save outputs. 

```
waterbirds_cap_list <- c()
for (waterbird in waterbirds){
  waterbird_cap <- str_to_title(waterbird)
  waterbirds_cap_list <- c(waterbirds_cap_list, waterbird_cap)
  print(waterbirds_cap_list)
}
waterbirds_cap_list
```

> Do [Basic Index]({{ site.baseurl }}/exercises/Loops-basic-index-R/) task 3.

#### Looping in data frames

* Loops go over columns of dataframes

```
waterbirds <- data.frame(sci_name = c("cygnus olor", 
                                      "aix sponsa", 
                                      "anas acuta"), 
                         common_name = c("mute swan", 
                                         "wood duck", 
                                         "pintail"))
for (waterbird in waterbirds){
  print("Start new loop")
  print(waterbird)
}
```

* Can loop over rows of data frames using index

```
for (i in 1:nrow(waterbirds)){
  print(i)
}
```

* Index can be any letter/word, i is convention

```
for (r in 1:nrow(waterbirds)){
  print(r)
}
```

```
for (i in 1:nrow(waterbirds)){
  print(waterbirds$sci_name[i])
}
```

```
for (i in 1:nrow(waterbirds)){
  print(paste(waterbirds$sci_name[i], "is a", 
              waterbirds$common_name[i]))
}
```

* Less memory to create initial empty dataframe
* Creates copy of dataframe when adding rows

```
waterbirds_2 <- data.frame(capital_name = character(3), 
                           name_length = numeric(3), 
                           stringsAsFactors = FALSE)
for (i in 1:nrow(waterbirds)){
  common_name_cap <- str_to_title(waterbirds$common_name[i])
  sci_name_length <- str_length(waterbirds$sci_name[i])
  waterbirds_2[i,] <- c(common_name_cap, sci_name_length)
}
```

> Do [stringr]({{ site.baseurl }}/exercises/Loops-stringr-R/).

#### Looping over files

* Repeat same actions on many similar files
* Get names of satellite collar location files

```
download.file("http://www.datacarpentry.org/semester-biology/data/collar-data-2016-01.zip", 
              "collar_data.zip")
unzip("collar_data.zip")
collar_data_files = list.files(pattern = "collar-data-.*.txt", 
                               full.names = TRUE)
```

* Look at one of the files

* Three ways to do same thing: get number of samples in each file

1. With loop

	```
	numbers_vector_1 <- c()
	for (data_file in collar_data_files){
	  file <- read.csv(data_file)
	  number <- nrow(file)
	  numbers_vector_1 <- c(numbers_vector_1, number)
	}
	```

2. With function and loop

	```
	get_numbers <- function(data_file_name){
	  file <- read.csv(data_file_name)
	  number <- nrow(file)
	  return(number)
	}
	
	numbers_vector_2 <- c()
	for (data_file in collar_data_files){
	  numbers_vector_2 <- c(numbers_vector_2, get_numbers(data_file))
	}
	```

3. With function and `apply`

```
numbers_vector_3 <- unlist(lapply(collar_data_files, get_numbers))
```

* How to choose when there are many ways to do the same thing? 
    * Speed
        * Matters in few cases
        * Hard to identify bottlenecks
    * Readability
        * Easy to understand
    * Personal preference
* There is no “right” way to do anything

> Do [Multiple Files]({{ site.baseurl }}/exercises/Loops-multiple-files-R/).

> Do [Species Occurrences Elevation Histogram]({{ site.baseurl }}/exercises/Spatial-data-elevation-histogram-R/).
