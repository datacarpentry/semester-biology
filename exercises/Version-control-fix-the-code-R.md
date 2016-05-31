---
layout: exercise
topic: Version Control
title: Fix the Code
language: R
---

Growth of biological populations are often modeled using logistic
growth, which posits that some limit will eventually stop a population
from increasing in size. The simplest form of this type of growth is
logistic growth and takes the following form:

`N_tplus1 <- N_t + r * N_t * ((K - N_t) / K)`

where `N_t` is the abundance at time `t`, `N_tplus1` is the
abundance at time `t+1`, `r` is the maximum per capita reproductive
rate, and `K` is the carrying capacity. The `(K - N_t) / K` term
captures the impact of the members of a species on each other - the more
individuals of the species there are, the lower each individuals net
reproductive rate.

Working late into the evening your professor has thrown together a small
example program that determines the equilibrium population sizes from
logistic growth and the time it takes to reach those equilibria. The
file is in your repository and is named `logistic_growth.R`.
Unfortunately, he's gotten sloppy because of the late hour and he's made
a few mistakes. Fix the errors on lines 3 and 13, save the file, and
then `commit` it back to your repository with an appropriate commit
message.
