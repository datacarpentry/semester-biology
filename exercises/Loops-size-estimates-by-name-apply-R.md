---
layout: exercise
topic: Loops
title: Size Estimates By Name Apply
language: R
---

If the [data on dinosaur lengths with species names]({{ site.baseurl }}/data/dinosaur_lengths.csv) is not in your working directory then download it. Import it using `read_csv()`.

You're going to write a function to estimate a dinosaur's mass based on its length and name of its taxonomic group.
The general form of the equation for doing this is:

> mass <- a * length ^ b

The parameters `a` and `b` vary by the group of dinosaurs, so you
decide to create a function that lets you specify which dinosaur group you need
to estimate the size of by name and then have the function automatically choose
the right parameters.

Create a function `get_mass_from_length_by_name()` that takes two arguments,
the `length` and the name of the dinosaur group. Inside this function use
`if`/`else if`/`else` statements to check to see if the name is one of the
following values and if so use the associated `a` and `b` values to estimate the
species mass using these equations:

* *Stegosauria*:  `mass = 10.95 * length ^ 2.64` ([Seebacher 2001](http://www.jstor.org/stable/4524171))
* *Theropoda*:  `mass = 0.73 * length ^ 3.63` ([Seebacher 2001](http://www.jstor.org/stable/4524171))
* *Sauropoda*:  `mass = 214.44 * length ^ 1.46` ([Seebacher 2001](http://www.jstor.org/stable/4524171))

If the name is not any of these values the function should return `NA`.

1. Use this function and `mapply()` to calculate the estimated mass for each dinosaur. You'll need to pass the data to `mapply()` as single vectors or columns, not the whole data frame.

2. Using `dplyr`, add a new `masses` column to the data frame (using `rowwise()`, `mutate()` and your function) and print the result to the console.

3. Using `ggplot`, make a histogram of dinosaur masses with one subplot for each species (using `facet_wrap()`).
