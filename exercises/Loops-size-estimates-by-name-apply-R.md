---
layout: exercise
topic: Loops
title: Size Estimates By Name Apply
language: R
---

This is a followup to [Size Estimates by Name]({{ site.baseurl }}/exercises/Functions-size-estimtates-by-name-R).

Download and import [data on dinosaur lengths with species names]({{ site.baseurl }}/data/dinosaur_lengths.csv).

Write a function `get_mass_from_length_by_name()` that uses the equation `mass <- a * length^b` to estimate the size of a dinosaur from its length. This function should take two arguments, the `length` and the name of the dinosaur group. Inside this function use `if`/`else if`/`else` statements to check to see if the name is one of the following values and if so set `a` and `b` to the appropriate values.

* *Stegosauria*:  `a` = `10.95` and `b` = `2.64` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Theropoda*:  `a` = `0.73` and `b` = `3.63` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Sauropoda*:  `a` = `214.44` and `b` = `1.46` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).

If the name is not any of these values set `a` and `b` to `NA`. 

1. Use this function and `mapply` to calculate the estimated mass for each dinosaur. You'll need to pass the data to `mapply` as single vectors or columns, not the whole data frame.

2. Using `dplyr` add a new `masses` column to the data frame (using `rowwise`, `mutate` and your function).

3. Make a histogram of of dinosaur masses with one subplot for each species (using `facet_wrap`).
