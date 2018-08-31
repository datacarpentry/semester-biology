---
layout: page
element: notes
title: Combining Data Manipulations in dplyr
topic: R
time: 30
---

* Combine a series of data manipulation actions
* Do each action in sequential order

#### Intermediate variables

* Determine the mean weight of DS in each year

```
surveys_DS <- filter(surveys, species_id == "DS")
surveys_DS_by_yr <- group_by(surveys_DS, year)
avg_weight_DS_by_yr <- summarize(surveys_DS_by_yr,
                                 avg_weight = mean(weight, na.rm=TRUE))
```

> Do [Portal Data Manipulation Exercise 1-2]({{ site.baseurl }}/exercises/Portal-data-manip-R)

#### Pipes

* Intermediate variables can get cumbersome if their are lots of steps.
* `%>%` ("pipe") takes the output of one command and passes it as input to the
  next command
* `x %>% f(y)` translates to `f(x, y)`
* `surveys %>% filter(species_id == "DS")`

```
avg_weight_DS_by_yr <- surveys %>%
  filter(species_id == "DS") %>%
  group_by(year) %>%
  summarize(avg_weight = mean(weight, na.rm=TRUE))
```

> Do [Fix the Code]({{ site.baseurl }}/exercises/Dplyr-fix-the-code-R).