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

* Need `print()` to display values inside a loop, function, or conditional.
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
  pet_upper <- str_to_upper(pet)
  print(pet_upper)
}
```
> Do [Exercise 1 - Basic Index]({{ site.baseurl }}/exercises/Loops-basic-index-R/) and [Exercise 2 - Basic Vector]({{ site.baseurl }}/exercises/Loops-basic-vector-R/).

> Make sure students get the basics before moving on.

> Do [Exercise 3.1 - for Loop]({{ site.baseurl }}/exercises/Functions-for-loop-R).

### Storing results

* Create an empty object.
    * `output <- c()`
* Add the new values with vector combination each trip through the loop.
    * `c(c(1, 2, 3), 4) -> [1] 1 2 3 4`

```
pets <- c("spot", "gigantor", "fluffy")
upper_case_pets <- c()
for (pet in pets){
  pet_upper <- str_to_upper(pet)
  upper_case_pets <- c(upper_case_pets, pet_upper)
  print(upper_case_pets)
}
```


### Looping in data frames

* By default data frames loop over columns

```
pets <- data.frame(pet_name = c("spot", "gigantor", "fluffy"),
                   pet_type = c("fish", "hamster", "lizard"))
for (pet in pets){
  print("Start new loop")
  print(pet)
}
```

* Who has seen/used a different approach to looping than has been show?
* That's called looping over an `index` and while it's overly complicated for
  simple loops it's useful for more complicated things like looping over rows

```
pets <- data.frame(pet_name = c("spot", "gigantor", "fluffy"),
                   pet_type = c("fish", "hamster", "lizard"))
for (i in 1:nrow(pets)){
  print(paste(pets$pet_name[i], " is a ", pets$pet_type[i], sep =""))
}
```

* We can also use the index to store the output by pre-allocating memory
* This is a lot faster than adding rows because it doesn't copy the data frame
  every time through the loop

```
output <- data.frame(name = character(3), namelength = numeric(3),
                     stringsAsFactors = FALSE)
for (i in 1:nrow(pets)) {
  pet_upper <- str_to_upper(pets$pet_name[i])
  pet_length <- str_length(pets$pet_type[i])
  output[i,] <- c(pet_upper, pet_length)
}
```

> Assign [Exercise 4 - stringr]({{ site.baseurl }}/exercises/Loops-stringr-R).
> Assign [Exercise 5 - DNA or RNA]({{ site.baseurl }}/exercises/Making-choices-dna-or-rna-R).


### Alternatives to loops

#### Vectorization

* Operations that work on all of the elements in a vector
* Make functions that work with vectors so no need to loop over values

```
lengths <- c(2.26, 1.48, 3.84)
mass <- 0.73 * length ** 3.63
mass
```

* Works for most simple math

#### Looping over files

* To learn alternatives learn how to do the same thing with many files. First
  with loops and then with some alternatives in R
* E.g., we have a set of files with satellite collar location data

```
date,time,lat,long
2016-01-01,4:20,26.16,-35.28
```

* To get a list of all these files in our `data` directory use `list.files()`

```
download.file("http://www.datacarpentry.org/semester-biology/data/collar-data-2016-01.zip")
unzip("collar-data-2016-01.zip")
list.files()
collar_data_files <- list.files("collar-data-2016-01", 
                                pattern="collar-data-.*.txt",
                                full.names=TRUE)
```

* Using the `pattern` argument makes file structure clear and avoids errors
* `full.names = TRUE` retains directory information
* Now we can loop over the files to work with them

```
num_samps <- c()
for (data_file in collar_data_files){
  data <- read.csv(data_file)
  samples <- nrow(data)
  num_samps <- c(num_samps, samples) 
}
num_samps
```

```
get_num_samps <- function(data_file_name){
  data <- read.csv(data_file_name)
  samples <- nrow(data)
  return(samples)
}

num_samps <- c()
for (data_file in collar_data_files){
  num_samps <- c(num_samps, get_num_samps(data_file))
}
num_samps
```

#### apply/map

* Since: 1) create empty object, 2) loop, 3) add result to storage object; is so
  common, many languages have a shortcut for use in simple situations.
* In R the main version this is the `apply` family

```
num_samps = sapply(collar_data_files, get_num_samps)
```

* There are a variety
of [`apply()`](http://finzi.psych.upenn.edu/R/library/base/html/apply.html)
statements that handle different use cases
    * [`lapply()`](http://finzi.psych.upenn.edu/R/library/base/html/lapply.html): Operate across lists and vectors
    * [`sapply()`](http://finzi.psych.upenn.edu/R/library/base/html/lapply.html): Simplify output to vector
    * [`mapply()`](http://finzi.psych.upenn.edu/R/library/base/html/mapply.html): Pass multiple variables or function arguments
* Why use `apply()`:
    * Readability
        * Single line of code
        * Simple command structure
    * Speed?
        * Only
          ([sometimes](https://stackoverflow.com/questions/2275896/is-rs-apply-family-more-than-syntactic-sugar))
          and even then often not enough to matter.
        * [Avoid premature optimization](http://c2.com/cgi/wiki?PrematureOptimization).

* In a number of other languages this is called `map()`
* There is now a `map()` for R that works similarly in the `purrr` package

#### dplyr

* Use `rowwise()` to get `dplyr` to run the function on each row

```
num_samps <- data.frame(myfiles, stringsAsFactors=FALSE) %>%
  rowwise() %>%
  mutate(samples = get_num_samps(myfiles))
```

* This is an example of why to use `stringsAsFactors=FALSE`

```
num_samps <- data.frame(myfiles) %>%
  rowwise() %>%
  mutate(samples = get_num_samps(myfiles))
```

* Instead of passing the file names this passes the integer values for the
  levels

```
num_samps <- data.frame(myfiles) %>%
  rowwise() %>%
  mutate(samples = typeof(myfiles))
```
  
