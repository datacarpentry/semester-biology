---
layout: exercise
topic: Making Choices
title: Size Estimates by Name
language: R
---

You're going to write a function to estimate a dinosaur's mass based on its length.
The general form of the equation for doing this is:

> mass <- a * length ^ b

The parameters `a` and `b` vary by the group of dinosaurs, so you
decide to create a function that lets you specify which dinosaur group you need
to estimate the size of by name and then have the function automatically choose
the right parameters.

Create a new function `get_mass_from_length_by_name()` that takes two arguments,
the `length` and the name of the dinosaur group. Inside this function use
`if`/`else if`/`else` statements to check to see if the name is one of the
following values and if so use the associated equation to estimate the
species mass:

* *Stegosauria*:  `mass = 10.95 * length ^ 2.64` ([Seebacher 2001](http://www.jstor.org/stable/4524171))
* *Theropoda*:  `mass = 0.73 * length ^ 3.63` ([Seebacher 2001](http://www.jstor.org/stable/4524171))
* *Sauropoda*:  `mass = 214.44 * length ^ 1.46` ([Seebacher 2001](http://www.jstor.org/stable/4524171))

If the name is not any of these values the function should return `NA`.

Run the function for:
1. A *Stegosauria* that is 10 meters long.
2. A *Theropoda* that is 8 meters long.
3. A *Sauropoda* that is 12 meters long.
4. A *Ankylosauria* that is 13 meters long.

*Challenge (**optional**)*: If the name is not one of values that have `a` and `b` values print warning that it doesn't know how to convert that group that includes that groups name in a message like "No known estimation for Ankylosauria".
You can use the function `warning("your warning text")` to print a warning and
the function `paste()` to combine text with a value from a variable `paste("My name is", name)`.
Doing this successfully will modify your answer to (4), which is fine.

*Challenge (**optional**)*: Change your function so that it uses two different
equations for *Stegosauria*. When *Stegosauria* is greater than 8
meters long use the equation above. When it is less than 8 meters long use
`mass = 8.5 * length ^ 2.8``.
Run the function for a *Stegosauria* that is 6 meters long.
