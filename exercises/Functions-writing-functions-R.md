---
layout: exercise
topic: Functions
title: Writing Functions
language: R
---

1\. Copy the following function (which converts weights in pounds to weights in grams) into your assignment and replace the `________` with the variable names for the input and output.

```r
convert_pounds_to_grams <- function(________) {
    grams = 453.6 * pounds
    return(________)
}
```

Use the function to calculate how many grams there are in 3.75 pounds.

2\. Copy the following function (which converts temperatures in Fahrenheit to temperatures in Celsius) into your assignment and replace the `________` with the needed commands and variable names so that the function returns the calculated value for Celsius.

```r
convert_fahrenheit_to_celsius <- ________(________) {
    celsius = (fahrenheit - 32) * 5 / 9
    ________(________)
}
```

Use the function to calculate the temperature in Celsius if the temperature in Fahrenheit is 80°F.

3\. Write a function named `double` that takes a number as input and outputs that number multiplied by 2. Run it with an input of 512.

4\. Write a function named `prediction` that takes three arguments, `x`, `a`, and `b`, and returns `y` using `y = a + b * x` (like a prediction from a simple linear model). Run it with `x` = 12, `a` = 6, and `b` = 0.8.
