---
layout: exercise
topic: For Loops
title: While
language: Python
---

This is a follow up to the [Exponential Growth problem]({{ site.baseurl }}/exercises/For-loops-exponential-growth-1-Python).

In addition to wanting to be able to calculate the predicted abundance
at a given point in time for an exponentially growing species, your lab
mate is also interested in how long it will take for a species to double
in size as a function of it's growth rate. Write a function that takes
the growth rate and initial population size as inputs and returns the
number of time steps that it took for the population to double (it's OK
if the population has more than doubled, we just want the time step at
which it becomes greater than or equal to twice the starting value).
Print the results to the screen for species with growth rates of 0.0001,
0.005, and 0.21, all with initial population sizes of 1000 individuals.

*Optional*: If you're feeling clever, try thinking about whether or not
the time it takes for a population to double depends on the initial
population size. You can play around with this using your function.
Based on either your understanding of the math or the results from your
computational experiments. Modify your function to be simpler than the
one you initially wrote.
