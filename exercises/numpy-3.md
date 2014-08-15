---
layout: page
title: Numpy 3
---

Understanding the total amount of biomass (the total mass of all
individuals) in forests is important for understanding the global carbon
budget and how the earth will respond to increases in carbon dioxide
emissions. Measuring the mass of entire trees is difficult, and it's
pretty much impossible to weigh an entire forest (even if we were
willing to clear cut a forest for science), but fortunately we can
estimate the mass of a tree based on its diameter.

There are lots of equations for estimating the mass of a tree from its
diameter, but one good option is the equation M = 0.124D^2.53^, where M
is measured in kg of dry (above-ground) biomass and D is in cm d.b.h.
(Brown 1997). We're going to estimate the total tree biomass for trees
in a 96 hectare area of the Western Ghats in India.

1.  Write a function that takes an array of tree diameters as an
    argument and returns an array of tree masses.
2.  Download [the raw
    data](http://esapubs.org/archive/ecol/E091/216/Macroplot_data_Rev.txt)
    and import it into Python.
3.  If you look at the file or [the
    metadata](http://esapubs.org/archive/ecol/E091/216/metadata.htm)
    carefully you'll notice that the data is actually in girth (i.e.,
    circumference, which is equal to pi \* diameter) rather than
    diameter. Write a function to takes an array of circumferences as an
    argument and returns an array of diameters. You can get the value of
    pi from the math module.
4.  Due to poor database structure using all of the trees will be a
    hassle. Since the vast majority of the trees are in the first
    TreeGirth column you can just use that data for the estimates. If
    you're feeling bold you can optionally choose to do the work of
    using all of the trees from all of the TreeGirth columns.
5.  Use the two functions you've written to estimate the total biomass
    (i.e., the sum of the masses) of trees in this dataset and print the
    result to the screen.
