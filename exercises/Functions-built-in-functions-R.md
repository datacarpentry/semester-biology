---
layout: exercise
topic: Functions
title: Built-in Functions
language: R
---

Use the built-in functions `abs()`, `round()`, `sqrt()`. A built-in function is
one that you don't need to install and load a package to use. Use another
function, `help()`, to learn how to use any of the functions that you don't know
how to use appropriately. `help()` takes one parameter, the name of the function
you want information about. E.g.,`help(round)`.

1. The absolute value of -15.5.
2. 4.483847 rounded to one decimal place. The function `round()` takes two
   arguments, the number to be rounded and the number of decimal places.
3. 3.8 rounded to the nearest integer. You don't have to specify the number of
   decimal places in this case if you don't want to, because `round()` will
   default to using 0 if the second argument is not provided. Look at
   `help(round)` or `?round` to see how this is indicated.
4. Assign the value of the square root of 2.6 to a variable. Then round the
   variable you've created to 2 decimal places and assign it to another
   variable. Print out the rounded value.
5. Do the same thing as in problem 4, but instead of creating the intermediate
   variable, perform both the square root and the round on a single line by
   putting the `sqrt()` call inside the `round()` call.
