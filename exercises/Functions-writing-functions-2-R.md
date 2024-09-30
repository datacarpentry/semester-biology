---
layout: exercise
topic: Functions
title: Writing Functions 2
language: R
---

1\. Copy the following function (which converts weights in pounds to weights in grams and rounds them) into your assignment. Replace the `________` with the variable names for the input and output. Replace `__` with a number so that by default the function will round the output to one decimal place.

```r
convert_pounds_to_grams <- function(________, numdigits = __) {
  grams <- 453.6 * pounds
  rounded <- round(grams, digits = numdigits)
  return(________)
}
```

Use the function to calculate how many grams there are in 4.3 pounds using the default for the number of decimal places.

2\. Write a function called `get_height_from_weight` that takes three arguments, `weight`, `a`, and `b`, and returns an estimate of `height` using `height = a * weight ^ b` (a prediction from a power model). Give it default arguments of `a` = 12 and `b` = 0.38. There should be no default value for `weight`. Use the default argument values (by passing only the value of `weight` to the function) to calculate `height` when `weight` = 42.

3\. Call the function from (2) setting `weight` to 42, `a` to 6, and `b` to 0.5.

4\. The function in (2) assumes that the weight is provided in grams. Use the functions from (1) and (2) in combination to estimate the height for an animal that weighs 2 pounds using the default value for `a`, but changing the value for `b` to 0.32.