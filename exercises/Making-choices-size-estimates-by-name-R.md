---
layout: exercise
topic: Making Choices
title: Size Estimates by Name
language: R
---

This is a follow up to [Use and Modify]({{ site.baseurl }}/exercises/Functions-use-and-modify-R).

To make it even easier to work with your dinosaur size estimation functions you
decide to create a function that lets you specify which dinosaur group you need
to estimate the size of by name and then have the function automatically choose
the right parameters.

Create a new function `get_mass_from_length_by_name()` that takes two arguments,
the `length` and the name of the dinosaur group. Inside this function use
`if`/`else if`/`else` statements to check to see if the name is one of the
following values and if so set `a` and `b` to the appropriate values.

* *Stegosauria*:  `a` = `10.95` and `b` = `2.64` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Theropoda*:  `a` = `0.73` and `b` = `3.63` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Sauropoda*:  `a` = `214.44` and `b` = `1.46` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).

Once the function has assigned `a` and `b` have it run `get_mass_from_length()`
with the appropriate values and return the estimated mass.

Run the function for:

1. A *Stegosauria* that is 10 meters long.
2. A *Theropoda* that is 8 meters long.
3. A *Sauropoda* that is 12 meters long.

*Challenge (optional)*: If the name doesn't match any of these values have the
function return `NA` and print out a message that it doesn't know how to convert
that group.