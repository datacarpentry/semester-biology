---
layout: exercise
topic: Loops
title: Size Estimates By Name Loop
language: R
---

This is a followup to [Size Estimates by Name]({{ site.baseurl }}/exercises/Making-choices-size-estimates-by-name-R).

If `dinosaur_lengths.csv` is not already in your working directory download a copy of the [data on dinosaur lengths with species names]({{ site.baseurl }}/data/dinosaur_lengths.csv). Load it into R.

Write a function `mass_from_length()` that uses the equation `mass <- a * length^b` to estimate the size of a dinosaur from its length.
This function should take two arguments, `length` and `species`. For each of the following inputs for `species`,
so use the associated `a` and `b` values to estimate the
species mass using these equations:

* *Stegosauria*:  `mass = 10.95 * length ^ 2.64` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Theropoda*:  `mass = 0.73 * length ^ 3.63` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Sauropoda*:  `mass = 214.44 * length ^ 1.46` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* For any other value of `species`: `mass = 25.37 * length ^ 2.49`

1. Use this function and a for loop to calculate the estimated mass for each dinosaur, store the masses in a vector, and after all of the calculations are complete show the first few items in the vector using `head()`.
2. Add the results in the vector back to the original data frame. Show the first few rows of the data frame using `head()`.
3. Calculate the mean mass for each `species` using `dplyr`.
