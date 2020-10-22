---
layout: exercise
topic: Functions
title: Combining Functions
language: R
---

This is a follow up to [Default Argument]({{ site.baseurl }}/exercises/Functions-default-arguments-R).

Measuring things using the metric system is the standard approach for scientists, but when communicating your results more broadly it may be
useful to use different units (at least in some countries).
Write a function called `convert_kg_to_pounds` that converts kilograms into pounds (`pounds = 2.205 * kg`).
Use that function and your `get_mass_from_length()` function from [Default Arguments]({{ site.baseurl }}/exercises/Functions-default-arguments-R) to estimate the weight, in pounds, of a 12 m long Stegosaurus with `a = 10.95` and `b = 2.64` (The estimated `a` and `b` values for *Stegosauria* from [Seebacher 2001](http://www.jstor.org/stable/4524171)).
