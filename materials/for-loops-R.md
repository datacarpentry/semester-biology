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

est_mass(1.6)
```

* Easy to find mass for other volumes

```
est_mass(5.6)
est_mass(3.1)
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

* Use `apply()` and `map()` functions
* Take a function
* Apply it to each item in a list
* Return a list of the same size
* Don't require calculations to work on vectors


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


### For loops

#### Basic `for` loop

* Fundamental structure for repetition in programming
* Do same action to each component of a list

```
for (item in list_of_items) {
  do_something(item)
}
```

* Need `print()` to display values inside a loop, function, or conditional.

```
volumes = c(1.6, 3, 8)
for (volume in volumes){
  print(2.65 * volume^0.9)
}
```

* This does the same exact thing as

```
volume <- volumes[1]
print(2.65 * volume ^ 0.9)
volume <- volumes[2]
print(2.65 * volume ^ 0.9)
volume <- volumes[3]
print(2.65 * volume ^ 0.9)
```

* Can have many rows in a loop body

```
for (volume in volumes){
   mass <- 2.65 * volume ^ 0.9
   mass_lb <- mass * 2.2
   print(mass_lb)
}
```

> Do Task 1 in [Use and Modify with Loops]({{ site.baseurl }}/exercises/Loops-use-modify-loop-R/).


#### Looping with an index

* Loop over values only let's you access values from a single list
* Loop over index let's you access values from multiple lists

```
for (i in seq_along(volumes)){
   mass <- 2.65 * volumes[i] ^ 0.9
   print(mass)
}
```

* `seq_along()` generates a vector of numbers from 1 to `length(volumes)`
* Use this "index" to get the values at that position
* Can use the "index" for multiple vectors

```
b0 <- c(2.65, 1.28, 3.29)
b1 <- c(0.9, 1.1, 1.2)
for (i in seq_along(volumes)){
   mass <- b0[i] * volumes[i] ^ b1[i]
   print(mass)
}
```

#### Storing results

* Looping with an index also makes it easy to store results
* First create an empty vector the length of the results
* Then add each result in the right position

```
b0 <- c(2.65, 1.28, 3.29)
b1 <- c(0.9, 1.1, 1.2)
masses <- vector(mode="numeric", length=length(volumes))
for (i in seq_along(volumes)){
   mass <- b0[i] * volumes[i] ^ b1[i]
   masses[i] <- mass
}
```

* Walk through iteration in debugger

> Do Tasks 2-3 in [Use and Modify with Loops]({{ site.baseurl }}/exercises/Loops-use-modify-loop-R/).


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
* Write a function to handle a single file
* Use a loop to run the function for each file

* Calculate the number of observations in each file

	```
	get_counts <- function(data_file_name){
	  file <- read.csv(data_file_name)
	  count <- nrow(file)
	  return(count)
	}
	
	results <- vector(length = length(collar_data_files))
	for (i in seq_along(collar_data_files){
	  results[i] <- get_numbers(collar_data_files[i])
	}
	```

* With `apply`

```
results <- unlist(lapply(collar_data_files, get_numbers))
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
