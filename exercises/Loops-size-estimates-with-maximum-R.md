---
layout: exercise
topic: Loops
title: Size Estimates With Maximum
language: R
---

This is a followup to Part 1 [Size Estimates Vectorized]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R).

Create a new version of your `mass_from_length_theropoda()` function from Part 1 of [Size Estimates Vectorized]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R) called `mass_from_length_max()`. This function should only calculate a mass if the value of `length` passed to the function is less than 20. If `length` is greater than 20 return `NA` instead. Use `sapply()` and this new function to estimate the mass for the `theropoda_lengths` data from [Size Estimates Vectorized]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R).
