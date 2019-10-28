---
layout: exercise
topic: Functions
title: Use and Modify
language: R
---

The length of an organism is typically strongly correlated with its body
mass. This is useful because it allows us to estimate the mass of an organism
even if we only know its length. This relationship generally takes the form:

Mass = a * Length<sup>b</sup>

Where the parameters `a` and `b` vary among groups. This allometric approach is
regularly used to estimate the mass of dinosaurs since we cannot weigh something
that is only preserved as bones.

The following function estimates the mass of an organism in kg based on its
length in meters for a particular set of parameter values, those for *Theropoda*
(where `a` has been estimated as `0.73` and `b` has been estimated as `3.63`;
[Seebacher 2001](http://www.jstor.org/stable/4524171)).

```
get_mass_from_length_theropoda <- function(length){
  mass <- 0.73 * length ^ 3.63
  return(mass)
}
```

1. Add a comment to this function so that you know what it does.
2. Use this function to print out the mass of a Spinosaurus that is 16 m long
   based on its reassembled skeleton.
3. Create a new version of this function called `get_mass_from_length()` that
   estimates the mass of an organism in kg based on its length in meters by
   taking `length`, `a`, and `b` as parameters. This lets us pass the function
   all 3 values that it needs to estimate a mass as parameters, which makes it
   much easier to reuse for all of the non-theropod species. Use this new
   function to estimate the mass of a Sauropoda (`a = 214.44`, `b = 1.46`) that
   is 26 m long.
