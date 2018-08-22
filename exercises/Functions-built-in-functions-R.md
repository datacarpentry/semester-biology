---
layout: exercise
topic: Functions
title: Built-in Functions
language: R
---

A built-in function is one that you don't need to install and load a package to
use. To learn how to use a function you can use the `help()` function or the
`Help` tab in RStudio. `help()` takes one parameter, the name of the function
that you want information about (*e.g.,* `help(abs)`) or type the name into the
search box on the `Help` tab.  Familiarize yourself with the built-in functions
`abs()`, `round()`, `sqrt()`, `tolower()`, and `toupper()`.  Use these built-in
functions to print the following items:

1. The absolute value of -15.5.
2. 4.483847 rounded to one decimal place. *The function `round()` takes two
   arguments, the number to be rounded and the number of decimal places.*
3. 3.8 rounded to the nearest integer. *You don't have to specify the number of
   decimal places in this case if you don't want to, because `round()` will
   default to using `0` if the second argument is not provided. Look at
   `help(round)` or `?round` to see how this is indicated.*
4. `"species"` in all capital letters.
5. `"SPECIES"` in all lower case letters.
6. Assign the value of the square root of 2.6 to a variable. Then round the
   variable you've created to 2 decimal places and assign it to another
   variable. Print out the rounded value.

*Challenge*: Do the same thing as task 6 (*immediately above*), but instead of
creating the intermediate variable, perform both the square root and the round
on a single line by putting the `sqrt()` call inside the `round()` call.
