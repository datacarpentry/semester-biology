---
layout: exercise
topic: Sets
title: Species Composition 1
language: Python
---

In ecology we are often interested in how similar two locations are with
respect to their species composition. In other words, we often want to
know how similar the species lists are at the two sites. Do the two
sites have all the same species, completely different sets of species,
something in the middle? Patterns related to the similarity of species
composition can provide information on the operation of important
ecological processes, like competition and dispersal, and can also allow
us to estimate the total number of species occuring in a large area
based on a small number of samples.

There are a number of different ways of calculating the similarity of
species composition among sites, but one of the classic and still most
popular approaches is the [Jaccard
index](http://en.wikipedia.org/wiki/Jaccard_index). The Jaccard index is
calculated simply as the number of species that are shared by the two
sites divided by the total number of species that occur at both sites
combined. To be precise, `J = C / (S(A) + S(B) - C)`, where `J` is the
Jaccard index, `C` is the number of species shared by the two sites, and
`S(A)` and `S(B)` are the number of species at Site A and Site B
respectively. Another way of saying this (and one that is quite useful
for this assignment) is that the Jaccard index is equal to the size of
the intersection of the two species lists divided by the size of the
union of the two species lists.

Determine the Jaccard similarity for all pairs of sites in a tallgrass
prairie from Oklahoma published by [McGlinn et al.
2010](http://www.esapubs.org/archive/ecol/E091/124/default.htm). The
data you will need is in the [species presence
table](http://www.esapubs.org/archive/ecol/E091/124/TGPP_pres.csv).This
dataset includes information on the scales at which species were present
and their location within each plot (the Corner and Scale columns), but
for the purposes of this analysis we are only interested in whether or
not the species occurs within the plot.

Use sets as described below to answer this question. Calculate the
similarities within each year. Save the results to a `csv` file where the
first column is the year, the second column is the plot id for one of
the two plots, the third column is the plot id for the other of the two
plots, and the fourth column is the Jaccard similarity.

#### Using sets

There is only one requirement for how you go about answering this
problem and that is that you use sets to do so. Specifically your
solution must include a function that calculates the Jaccard similiarity
between a pair of sites when passed two sets as arguments. Each set is a
species list for one site. This is one of the easiest to implement, most
readable, and most computationally efficient ways to solve this problem.

#### Problem decomposition

When tackling a broad problem like this it is always important to
think about how you are going to [decompose the
problem]({{ site.baseurl }}/material/problem-decomposition) into manageable pieces. Take a few
minutes to think about how you would approach this problem before
following the steps outlined below. Sketch them out in a text file, or
by writing out just the final commands you will use (i.e., none of the
details, just the major function names and calls to the functions) in
your program, or on a piece of paper (for those of you who are old
school like me).
