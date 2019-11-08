---
layout: page
element: notes
title: For Loops in R
language: R
---

### Basic `for` loop

* Fundamental structure for repetition in programming
* Do same action to each item in a list of things

```r
for (item in list_of_items) {
  do_something(item)
}
```

* Need `print()` to display values inside a loop or function.

```r
volumes = c(1.6, 3, 8)
for (volume in volumes){
  print(2.65 * volume^0.9)
}
```

* This does the same exact thing as

```r
volume <- volumes[1]
print(2.65 * volume ^ 0.9)
volume <- volumes[2]
print(2.65 * volume ^ 0.9)
volume <- volumes[3]
print(2.65 * volume ^ 0.9)
```

* Can have many rows in a loop body

```r
for (volume in volumes){
   mass <- 2.65 * volume ^ 0.9
   mass_lb <- mass * 2.2
   print(mass_lb)
}
```

> Do Tasks 1 & 2 in [Basic For Loops]({{ site.baseurl }}/exercises/Loops-basic-for-loops-R/).

### Looping with an index & storing results

* Loops over integers and uses these integers to access the vector the associated positions

```r
for (i in 1:length(volumes)){
   mass <- 2.65 * volumes[i] ^ 0.9
   print(mass)
}
```

* Use this "index" to get the values at that position
* Can use the "index" for multiple vectors

* Looping with an index allows us to store results calculated in the loop
* First create an empty vector the length of the results
* `mode` is the type of data we are going to store
* `length` is the length of the vector

```r
masses <- vector(mode = "numeric", length = length(volumes))
masses
```

* Then add each result in the right position
* For each trip through the loop put the output into the empty vector at the ith position

```r
for (i in 1:length(volumes)){
   mass <- 2.65 * volumes[i] ^ 0.9
   masses[i] <- mass
}
masses
```

* Walk through iteration in debugger

> Do Tasks 3-4 in [Basic For Loops]({{ site.baseurl }}/exercises/Loops-basic-for-loops-R/).

* Looping with an index also allows us to access values from multiple vectors


```r
b0 <- c(2.65, 1.28, 3.29)
b1 <- c(0.9, 1.1, 1.2)
masses <- vector(mode="numeric", length=length(volumes))
for (i in seq_along(volumes)){
   mass <- b0[i] * volumes[i] ^ b1[i]
   masses[i] <- mass
}
```

### Looping over files

* Repeat same actions on many similar files
* Get names of satellite collar location files

```r
download.file("http://www.datacarpentry.org/semester-biology/data/locations-2016-01.zip", 
              "locations.zip")
unzip("locations.zip")
data_files = list.files(pattern = "locations-.*.txt", 
                        full.names = TRUE)
```

* Calculate the number of observations in each file

```r
results <- vector(mode = "integer", length = length(data_files))
for (i in 1:length(data_files){
  data <- read.csv(data_files[i])
  count <- nrow(data)
  results[i] <- count
}
```

* Store output in a data frame instead of a vector
* Associate the file name with the count

```r
results <- data.frame(file_name = charcter(length(data_files))
                      count = integer(length(data_files)),
                      stringsAsFactors = FALSE)
for (i in 1:length(data_files){
  data <- read.csv(data_files[i])
  count <- nrow(data)
  results$file_name[i] <- data_files[i]
  results$count[i] <- count
}
results
```

> Do [Multiple-file Analysis]({{ site.baseurl }}/exercises/Loops-multi-file-analysis-R/).
> **Exercise uses different collar data**

* With `apply`

```r
get_counts <- function(data_file_name){
  file <- read.csv(data_file_name)
  count <- nrow(file)
  return(count)
}

results <- unlist(lapply(collar_data_files, get_counts))
```

* How to choose when there are many ways to do the same thing?
  * Speed
    * Matters in few cases
    * Hard to identify bottlenecks
  * Readability
    * Easy to understand
  * Personal preference
* There is no “right” way to do anything

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