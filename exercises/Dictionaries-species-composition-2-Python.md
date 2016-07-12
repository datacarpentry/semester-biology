---
layout: exercise
topic: Dictionaries
title: Species Composition 2
language: Python
---

Some measures of similarity, like the Jaccard index in
[Species Composition 1]({{ site.baseurl }}/exercises/Sets-species-composition-1-Python), are based only on the presence/absence of
species. Another major class of similarity measures also includes information on
their relative abundance in the community. One of these measures is the
[Euclidean distance](http://en.wikipedia.org/wiki/Euclidean_distance) (actually
the Euclidean distance measures difference not similarity so the similarity
measure is 1 - Euclidean distance), which is calculated as the `sqrt(sum((N1_i -
N2_i)^2))`, where `N1_i` is the relative abundance of species `i` at site 1 and
`N2_i` is the relative abundance of species `i` at site 2 (including
zeros). Relative abundance is the number of individuals of a species divided by
the total abundance of all species at the site.

#### Data

Use the data from McGlinn et al. 2010. We need some information on the
relative prevalence of the different species at the different sites so
this time download the [Cover
table](http://www.esapubs.org/archive/ecol/E091/124/TGPP_cover.csv). Use
the `cover` column as the measure of N (we often work with cover instead of
number of individuals in plant communities). For this analysis we decide
that instead of keeping the years in the analysis separate we want to
combine the data from all of the years to get a longer time-scale
picture.

#### Using dictionaries

Write a function that calculates the Euclidean distance for two sites
when passed two dictionaries as arguments. Each dictionary should hold
the information on the species identity of all species occurring at a
site and the associated total cover of that species.

Write a series of commands that takes the imported data and creates one
dictionary for each site that includes the species names and associated
abundances for each site, where the abundance is the sum of all of the
values in the cover column, for each species at the site. Then pass all
possible pairs of dictionaries to your function for calculating the
Euclidean distance between each pair of sites. Save the results to a `csv`
file where the first column is the plot id for one of the two plots, the
second column is the plot id for the other of the two plots, and the
third column is the 1 minus the Euclidean Distance (our abundance based
measure of similarity.
