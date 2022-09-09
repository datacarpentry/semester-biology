---
layout: page
element: notes
title: Combining Data Manipulations in dplyr
language: R
time: 30
---

### Introduction

* Combine a series of data manipulation actions
* Do each action in sequential order

### Intermediate variables

* Run a command
* Store the output in a variable
* Use that variable later in the code
* Repeat

* Obtain the data for only DS, sorted by year, with only the year and and weight columns

```
ds_data <- filter(surveys, species_id == "DS", !is.na(weight))
ds_data_by_year <- arrange(ds_data, year)
ds_weight_by_year <- select(ds_data_by_year, year, weight)
```

> Do [Portal Data Manipulation Exercise 1-2]({{ site.baseurl }}/exercises/Portal-data-manip-R)

### Pipes

* Intermediate variables can get cumbersome if their are lots of steps.
* `|>` ("pipe") takes the output of one command and passes it as input to the
  next command
* Want to take the mean of a vector
* Normally we would run the `mean` function with the vector as the input:

```
x = c(1, 2, 3)
mean(x)
```

* Instead we could pipe the vector into the function

```
x |> mean()
```

* So `x` becomes the first argument in `mean`
* If we want to add other arguments they get added to the function call

```
x = c(1, 2, 3, NA)
mean(x, na.rm = TRUE)
x |> mean(na.rm = TRUE)
```

* *Questions?*

```
surveys |>
  filter(species_id == "DS", !is.na(weight))
```

```
ds_weight_by_year <- surveys |>
  filter(species_id == "DS", !is.na(weight)) |>
  arrange(year) |>
  select(year, weight)
```

> Do [Portal Data Manipulation Pipes 1]({{ site.baseurl }}/exercises/Portal-data-manip-pipes-R).

### The magrittr pipe

* You will also see another type of pipe character `%>%`
* This is the original pipe in R and you had to load the magrittr package to use it (this gets loaded automatically by dplyr)
* Either pipe is fine for this class
    * `|>` will work everywhere as long as you have a new enough version of R
    * magrittr has some fancier functionality that may be useful in some cases

### Keyboard Shortcut

* Shortcut: Ctrl-Shift-m
* You can change this to give the base R pipe
    * Tools -> Global Options -> Code -> Use native pipe operator

### What if I want to pipe to an argument other than the first argument

```
surveys |>
  filter(species_id == "DS", !is.na(weight)) |>
  arrange(year) |>
  select(year, weight) |>
  lm(weight ~ year, data = _)
```