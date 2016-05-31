---
layout: exercise
topic: For Loops
title: Exponential Growth 1
language: Python
---

The field of population biology is interested in how the number of
individuals (N) of a population (all members of a species living in some
region) changes through time. The most basic model in population biology
is exponential growth, which simply says that each individual reproduces
at a constant rate. Therefore the number of individuals at time t + 1 is
equal to the number of individuals at time t times the per individual
rate of reproduction (r). In other words N(t+1) = N(t) + r\*N(t).

One of your lab mates is conducting an experiment to determine if the
growth of insect populations follows exponential growth. They are really
good at cultivating insect populations, but they can barely turn their
computer on let alone program with it, so they have come to you for help
in generating the predicted population sizes for their experiments. The
first experiment will measure the population sizes of a species with a
reproductive rate of 0.152 at 10 weeks, 50 weeks and 100 weeks. The
experiment will start with an initial population size of 10 individuals.

Since you know there will be more experiments later, write a function,
`get_pop_size_at_t(init_pop_size, reprod_rate,
time_of_sample)`, that returns the population size of a species
undergoing exponential growth at the `time_of_sample` when the
population begins at `init_pop_size` individuals when t = 0. Use
this function to determine the expected population size at each of the
specified points in time and print the results to the screen.
