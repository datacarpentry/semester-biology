---
layout: page
element: notes
title: For Loops in R
language: R
---

### Basic `for` loop

* Loops are the fundamental structure for repetition in programming
* `for` loops perform the same action for each item in a list of things

```r
for (item in list_of_items) {
  do_something(item)
}
```

* To see an example of this let's calculate masses from volumes using a loop
* Need `print()` to display values inside a loop or function

```r
volumes = c(1.6, 3, 8)
for (volume in volumes){
  print(2.65 * volume^0.9)
}
```

* Code takes the first value from `volumes` and assigns it to `volume` and does the calculation and prints it
* Then it takes the second value from `volumes` and assigns it to `volume` and does the calculation and prints it
* And so on
* So, this loop does the same exact thing as

```r
volume <- volumes[1]
print(2.65 * volume ^ 0.9)
volume <- volumes[2]
print(2.65 * volume ^ 0.9)
volume <- volumes[3]
print(2.65 * volume ^ 0.9)
```

* Like with functions and conditionals loops can have many rows of code
* Everything between the curly brackets is executed each time through the loop
* Let's expand our look so that it first estimates the mass, then converts it from kilograms to pounds, and then prints out the value

```r
for (volume in volumes){
   mass <- 2.65 * volume ^ 0.9
   mass_lb <- mass * 2.2
   print(mass_lb)
}
```

> Do Tasks 1 & 2 in [Basic For Loops]({{ site.baseurl }}/exercises/Loops-basic-for-loops-R/).

### Looping with an index & storing results

* In the last video we saw that in R loops iterate over a series of values in a vector or other list like object
* When we use that value directly this is called looping by value
* But there is another way to loop, which is called looping by index
* Looping by index loops over a list of integer index values, typically starting at 1
* These integers are then used to access values in one or more vectors at the position inicated by the index
* If we modified our previous loop to use an index it would look like this
* We often use `i` to stand for "index" as the variable we update with each step through the loop
* We then create a vector of position values starting at 1 (for the first value) and ending with the length of the object we are looping over
* Then inside the loop instead of doing the calculation on the index (which is just a number between 1 and 3 in our case)
* We use square brackets and the index to get the appropriate value out of our vector

```r
volumes = c(1.6, 3, 8)
for (i in 1:length(volumes)){
   mass <- 2.65 * volumes[i] ^ 0.9
   print(mass)
}
```

* This gives us the same result, but it's more complicated to understand
* So why would we loop by index?
* The advantage to looping by index is that it lets us do more complicated things
* One of the most common things we use this for are storing the results we calculated in the loop
* To do this we start by creating an empty object the same length as the results will be
* To store results in a vector we use the function `vector` to create an empty vector of the right length
* `mode` is the type of data we are going to store
* `length` is the length of the vector

```r
masses <- vector(mode = "numeric", length = length(volumes))
masses
```

* Then add each result in the right position in this vector
* For each trip through the loop put the output into the empty vector at the `i`th position

```r
for (i in 1:length(volumes)){
   mass <- 2.65 * volumes[i] ^ 0.9
   masses[i] <- mass
}
masses
```

* Walk through iteration in debugger

> Do Tasks 3-4 in [Basic For Loops]({{ site.baseurl }}/exercises/Loops-basic-for-loops-R/).


### Looping over multiple values

* Looping with an index also allows us to access values from multiple vectors


```r
b0 <- c(2.65, 1.28, 3.29)
b1 <- c(0.9, 1.1, 1.2)
volumes = c(1.6, 3, 8)
masses <- vector(mode="numeric", length=length(volumes))
for (i in seq_along(volumes)){
   mass <- b0[i] * volumes[i] ^ b1[i]
   masses[i] <- mass
}
```

> Do Task 5 in [Basic For Loops]({{ site.baseurl }}/exercises/Loops-basic-for-loops-R/).

### Looping with functions

* It is common to combine loops with with functions by calling one or more functions as a step in our loop
* For example, let's take the non-vectorized version of our `est_mass` function that returns an estimated mass if the `volume > 5` and `NA` if it's not.

```r
est_mass <- function(volume){
  if (volume > 5) {
    mass <- 2.65 * volume ^ 0.9
  } else {
    mass <- NA
  }
  return(mass)
}

volumes = c(1.6, 3, 8)
```

* We can't pass the vector to the function and get back a vector of results because of the `if` statements
* So let's loop over the values
* First we'll create an empty vector to store the results
* And them loop by index, callling the function for each value of `volumes`

```r
masses <- vector(mode="numeric", length=length(volumes))
for (i in length(volumes)){
   mass <- est_mass(volumes[i])
   masses[i] <- mass
}
```

* This is the for loop equivalent of an `sapply` statement we used in a previous lesson

```r
masses_apply <- sapply(volumes, est_mass)
```

* How to choose when there are many ways to do the same thing?
  * Speed
    * Matters in few cases
    * Hard to identify bottlenecks
  * Readability
    * Easy to understand
  * Personal preference
* There is single best choice

> Do [Size Estimates By Name Loop]({{ site.baseurl }}/exercises/Loops-size-estimates-by-name-loop-R/).

### Looping over files

* Repeat same actions on many similar files
* Let's download some simulated satellite collar data

```r
download.file("http://www.datacarpentry.org/semester-biology/data/locations.zip",
              "locations.zip")
unzip("locations.zip")
```

* Now we need to get the names of each of the files we want to loop over
* We do this using `list.files()`
* If we run it without arguments it will give us the names of all files in the directory

```r
list.files()
```

* But we just want the data files so we'll add the optional `pattern` argument to only get the files that start with `"locations-"`
* The `*` is a wild card, so this means "starts with locations- and includes anything afterwards"


```r
data_files = list.files(pattern = "locations-*", 
                        full.names = TRUE)
```

* Once we have this list we can loop over it count the number of observations in each file
* First create an empty vector to store those counts

```r
results <- vector(mode = "integer", length = length(data_files))
```

* Then write our loop

```r
for (i in 1:length(data_files){
  data <- read.csv(data_files[i])
  count <- nrow(data)
  results[i] <- count
}
```

> Do Task 1 of [Multiple-file Analysis]({{ site.baseurl }}/exercises/Loops-multi-file-analysis-R/).
> **Exercise uses different collar data**

### Storing loop results in a data frame

* We often want to calculate multiple pieces of information in a loop making it useful to store results in things other than vectors
* We can store them in a data frame instead by creating an empty data frame and storing the results in the `i`th row of the appropriate column
* Associate the file name with the count
* Start by creating an empty data frame
* Use the `data.frame` function
* Provide one argument for each column
* "Column Name" = "an empty vector of the correct type"

```r
results <- data.frame(file_name = vector(mode = "character", length = length(data_files)))
                      count = vector(mode = "integer", length = length(data_files)))
```

* Now let's modify our loop from last time
* Instead of storing `count` in `results[i]` we need to first specify the `count` column using the `$`: `results$count[i]`
* We also want to store the filename, which is `data_files[i]`

```r
for (i in 1:length(data_files){
  data <- read.csv(data_files[i])
  count <- nrow(data)
  results$file_name[i] <- data_files[i]
  results$count[i] <- count
}
```

* We could also rewrite this a little to make it easier to understand by getting the file name at the begging

```r
for (i in 1:length(data_files){
  filename <- data_files[i]
  data <- read.csv(filename)
  count <- nrow(data)
  results$file_name[i] <- filename
  results$count[i] <- count
}
```

> Do Task 2 [Multiple-file Analysis]({{ site.baseurl }}/exercises/Loops-multi-file-analysis-R/).
> **Exercise uses different collar data**

### Subsetting Data (optional)

* Loops can subset in ways that are difficult with things like `group_by`
* Look at some data on trees from the National Ecological Observatory Network

```r
library(ggplot2)
library(dplyr)

neon_trees <- read.csv('data/HARV_034subplt.csv')
ggplot(neon_trees, aes(x = easting, y = northing)) +
  geom_point()
```

* Look at a north-south gradient in number of trees
* Need to know number of trees in each band of y values
* Start by defining the size of the window we want to use
  * Use the grid lines which are 2.5 m

```r
window_size <- 2.5
```

* Then figure out the edges for each window

```r
south_edges <- seq(4713095, 4713117.5, by = window_size)
north_edges <- south_edges + window_size
```

* But we don't want to go all the way to the far edge

```r
south_edges <- seq(4713095, 4713117.5 - window_size, by = window_size)
north_edges <- south_edges + window_size
```

* Set up an empty data frame to store the output

```r
counts <- vector(mode = "numeric", length = length(left_edges))
```

* Look over the left edges and subset the data occuring within each window

```r
for (i in 1:length(south_edges)) {
  data_in_window <- filter(neon_trees, northing >= south_edges[i], northing < north_edges[i])
  counts[i] <- nrow(data_in_window)
}
counts
```

### Nested Loops (optional)

* Sometimes need to loop over multiple things in a coordinate fashion
* Pass a window over some spatial data
* Look at full spatial pattern not just east-west gradient

* Basic nested loops work by putting one loop inside another one

```r
for (i in 1:10) {
  for (j in 1:5) {
    print(paste("i = " , i, "; j = ", j))
  }
}
```

* Loop over x and y coordinates to create boxes
* Need top and bottom edges

```r
east_edges <- seq(731752.5, 731772.5 - window_size, by = window_size)
west_edges <- east_edges + window_size

```

* Redefine out storage

```r
output <- matrix(nrow = length(south_edges), ncol = length(east_edges))
```

```r
for (i in 1:length(south_edges)) {
  for (j in 1:length(east_edges)) {
    data_in_window <- filter(neon_trees,
                            northing >= south_edges[i], northing < north_edges[i],
                            easting >= left_edges[j], easting < right_edges[j],)
    output[i, j] <- nrow(data_in_window)
  }
}
output
```

### Sequence along (optional)

* `seq_along()` generates a vector of numbers from 1 to `length(volumes)`