---
layout: exercise
topic: Statistics
title: Mammal Body Size 4
language: Python
---

This is a follow up to [Mammal Body Size 1]({{ site.baseurl }}/exercises/Scientific-mammal-body-size-1-Python) and [Mammal Body Size 3]({{ site.baseurl }}/exercises/Graphing-mammal-body-size-3-Python).

We have previously compared the average masses of extant and extinct species on
different continents to try to understand whether size has an influence on
extinction in mammals. We've done this by looking at the means and by comparing
the histograms for extinct and extant species, but we haven't done any
statistics yet to actually test if the average sizes are different.

Perform either a two-sample t-test to compare the average sizes
of the extinct and extant species in each continent.

Save the results as a `csv` file named `size_comparison_results.csv`, where the
first column is the name of the continent, the second column is the average mass
for the extant species, the third column is the average mass for the extinct
species, and the fourth column is the p-value for whether or not they are
different.
