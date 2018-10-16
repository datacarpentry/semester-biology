---
layout: exercise
topic: Reproduction
title: Dinosaur Size Distribution
language: R
---

This is exercise builds on [Size Estimates by Name]({{ site.baseurl }}/exercises/Making-choices-size-estimates-by-name-R).

You want reproduce the analysis determining the distribution of body masses was
for dinosaurs originally performed by [Gorman & Hone
2012](https://doi.org/10.1371/journal.pone.0051925). Gorman & Hone (2012) use
femur length (FL; the length of the upper leg bone) to estimate mass based on a
general power law equation `Mass = a * FL ^ b` and the parameters vary by group:

* *Ornithischia*:  `a` = `0.002` and `b` = `3.0587`
* *Sauropodomorpha*:  `a` = `0.509` and `b` = `2.3459`
* *Theropoda*:  `a` = `0.0007` and `b` = `3.1854`

Download [the data]({{ site.baseurl }}/data/dinosaur_femur_lengths.csv),
estimate the mass of each species, and then make a histogram of these masses with
a logarithmically scaled size axis to reproduce their Figure 2a.

This should be done in a maximally automated way. The equations listed above
should only need be entered once and the code should automatically use the right
set of parameters based on the `Clade` data to estimate the mass of each species.