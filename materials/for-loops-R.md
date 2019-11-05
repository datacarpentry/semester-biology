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
download.file("http://www.datacarpentry.org/semester-biology/data/collar-data-2016-01.zip", 
              "collar_data.zip")
unzip("collar_data.zip")
data_files = list.files(pattern = "collar-data-.*.txt", 
                        full.names = TRUE)
```

* Look at one of the files
* Write a function to handle a single file
* Use a loop to run the function for each file

* Calculate the number of observations in each file

```r
results <- vector(length = length(data_files))
for (i in 1:length(data_files){
  data <- read.csv(data_files[i])
  count <- nrow(data)
  results[i] <- count
}
```

* Store output in a data frame instead of a vector
* Associate the file name with the count

```r
results <- data.frame(file_name = numeric(length(cdata_files))
                      count = integer(length(data_files)))
for (i in 1:length(data_files){
  data <- read.csv(data_files[i])
  count <- nrow(data)
  results$file_name[i] <- data_files[i]
  results$count[i] <- count
}
```

> Do [Multiple-file Analysis]({{ site.baseurl }}/exercises/Loops-multi-file-analysis-R/).

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

* 

```r
window_size = 1
for (x in 1:max(x)) {
  data_in_window = filter(data, xs >= x, xs < x + 2)
}
```

### Nested Loops (optional)

* Sometimes need to loop over multiple things in a coordinate fashion
* Pass a window over some spatial data
* Calculate a value in each window

```r
window_size = 1
for (x in 1:max(x)) {
  for (y in 1:max(y)) {
    data_in_window = filter(data, xs >= x, xs < x + 2, ys >= y, ys < y + 2)
  }
}
```

### Sequence along

* `seq_along()` generates a vector of numbers from 1 to `length(volumes)`