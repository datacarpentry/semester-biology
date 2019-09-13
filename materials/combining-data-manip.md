---
layout: page
element: notes
title: Combining Data Manipulations in dplyr
language: R
time: 30
---

* Combine a series of data manipulation actions
* Do each action in sequential order

#### Intermediate variables

* Run a command
* Store the output in a variable
* Use that variable later in the code
* Repeat

* Determine the mean weight of DS in each year

```
ds_data <- filter(surveys, species_id == "DS")
ds_data_by_year <- group_by(ds_data, year)
ds_weight_by_year <- summarize(ds_data_by_year,
                               avg_weight = mean(weight, na.rm = TRUE))
```

> Do [Portal Data Manipulation Exercise 1-2]({{ site.baseurl }}/exercises/Portal-data-manip-R)

#### Pipes

* Intermediate variables can get cumbersome if their are lots of steps.
* `%>%` ("pipe") takes the output of one command and passes it as input to the
  next command
* Want to take the mean of a vector
* Normally we would run the `mean` function with the vector as the input:

```
x = c(1, 2, 3)
mean(x)
```

* Instead we could pipe the vector into the function

```
x %>% mean()
```

* So `x` becomes the first argument in `mean`
* If we want to add other arguments they get added to the function call

```
x = c(1, 2, 3, NA)
mean(x, na.rm = TRUE)
x %>% mean(na.rm = TRUE)
```

* *Questions?*

```
surveys %>%
  filter(species_id == "DS", !is.na(weight))
```

```
ds_weight_by_year <- surveys %>%
  filter(species_id == "DS") %>%
  group_by(year) %>%
  summarize(avg_weight = mean(weight, na.rm = TRUE))
```

* Shortcut: Ctrl-shift-m

> Do [Portal Data Manipulation Pipes 1]({{ site.baseurl }}/exercises/Portal-data-manip-pipes-R).