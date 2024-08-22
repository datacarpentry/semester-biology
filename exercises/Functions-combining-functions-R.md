---
layout: exercise
topic: Functions
title: Combining Functions
language: R
---

This is a follow up to [Default Argument]({{ site.baseurl }}/exercises/Functions-default-arguments-R).

Measuring things using the metric system is the standard approach for scientists, but when communicating your results more broadly it may be
useful to use different units (at least in some countries).
Write two functions:

- One called `convert_kg_to_pounds` that converts kilograms into pounds (`pounds = 2.205 * kg`)
- One called `get_mass_from_length()` function called `get_mass_from_length()` that takes `length`, `a` and `b` as arguments, has the following default arguments `a = 39.9` and `b = 2.6`, uses the following code to estimate the mass `mass <- a * length ^ b`, and returns it (This is the function from [Default Argument]({{ site.baseurl }}/exercises/Functions-default-arguments-R), so feel free to copy over your answer to that exercise).


Use these two functions (each function should be called separately) to estimate the weight, in pounds, of a 12 m long Stegosaurus with `a = 10.95` and `b = 2.64` (The estimated `a` and `b` values for *Stegosauria* from [Seebacher 2001](http://www.jstor.org/stable/4524171)).
