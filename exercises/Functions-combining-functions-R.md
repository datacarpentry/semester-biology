---
layout: exercise
topic: Functions
title: Combining Functions
language: R
---

This is a follow up to [Use and Modify]({{ site.baseurl }}/exercises/Functions-use-and-modify-R).

Measuring things using the metric system is the standard approach for scientists, but when communicating your results more broadly it may be
useful to use different units (at least in some countries).
Write a function called `convert_kg_to_pounds` that converts kilograms into pounds (`kg = 2.205 * pounds`).
Use that function along with your `get_mass_from_length()` function from [Use and Modify]({{ site.baseurl }}/exercises/Functions-use-and-modify-R) to estimate the weight, in pounds, of a 12 m long Stegosaurus with `a = 10.95` and `b = 2.64` (The estimated `a` and `b` values for *Stegosauria* from [Seebacher 2001](http://www.jstor.org/stable/4524171)).
