---
layout: exercise
topic: Reproduction
title: Megafaunal Extinction
language: R
---

There were a relatively large number of extinctions of mammalian species roughly
10,000 years ago. To help understand why these extinctions happened scientists
are interested in understanding if there were differences in the size of the
species that went extinct and those that did not. You are going to reproduce the
three main figures from one of the major papers on this topic [Lyons et al.
2004](https://naturalhistory.si.edu/ETE/_LooyVersion/_img_ete/pubpdfs/LyonsEER.pdf).

You will do this using a 
[large dataset of mammalian body sizes](http://www.esapubs.org/archive/ecol/E084/094/#data)
that has data on the mass of recently extinct mammals as well as extant mammals
(i.e., those that are still alive today). Take a look at the
[metadata](http://www.esapubs.org/archive/ecol/E084/094/metadata.htm) to
understand the structure of the data.

1. Import the data into R. As with most real world data there are a number of
   issues with this dataset. Try to spot and clean them up during the import
   process, but understand that it is common to not discover some data issues
   until you start analyzing the data. Data cleaning is often an iterative
   process. Print out the structure of the resulting data frame.
2. Create a plot showing histograms of masses for extant mammals and those that
   went extinct during the pleistocene (`extant` and `extinct` in the `status`
   column). There should be one sub-plot for each continent and that sub-plot
   should show the histograms for both groups. Don't include islands (`Insular`
   and `Oceanic` in the `continent column) and only include continents with
   species that went extinct in the pleistocene. Scale the x-axis
   logarithmically and stack the sub-plots vertically like in the original paper
   (but don't worry about the order of the subplots being the same). Use good
   axis labels.
3. The 2nd figure in the original paper looks in more detail at two orders,
   *Xenarthra* and *Carnivora*, which showed extinctions in North and South
   America. Create a figure similar to the one in Part 2, but that shows 4
   sub-plots, one for each order on each of the two continents.
4. The 3rd figure in the original paper explores Australia as a case study.
   Australia is interesting because there is good data on both Pleistocene
   extinctions (`extinct` in the `status` column) and more modern extinctions
   occuring over the last 300 years (`historical` in the `status` column). Make
   a plot similar to the previous plots that compares these three different
   categories `extinct`, `extant`, and `historical`). Has the size pattern in
   exinctions changed for more modern extinctions?