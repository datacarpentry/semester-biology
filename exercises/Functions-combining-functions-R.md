---
layout: exercise
topic: Functions
title: Combining Functions
language: R
---

Write two functions:

- One called `get_mass_from_length()` that takes `length` (in m), `a` and `b` as arguments, has the following default arguments `a = 39.9` and `b = 2.6`, uses the following code to estimate the mass (in kg) `mass <- a * length ^ b`, and returns it. (This function is the answer to the [Default Arguments]({{ site.baseurl }}/exercises/Functions-default-arguments-R) exercise, so feel free to copy over your answer if you've done that exercise).
- One called `convert_kg_to_pounds` that converts kilograms into pounds (`pounds = 2.205 * kg`)

1. Use these two functions (each function should be called separately) to estimate the weight, in pounds, of a 12 m long Stegosaurus with `a = 10.95` and `b = 2.64` (The estimated `a` and `b` values for *Stegosauria* from [Seebacher 2001](http://www.jstor.org/stable/4524171)).

2. Use these two functions (each function should be called separately) to estimate the weight, in pounds, of a 4 m long dinosaur using the default parameters.