---
layout: exercise
topic: Scientific
title: Tree Biomass Challenge
language: R
---

Understanding the total amount of biomass (the total mass of all individuals) in 
forests is important for understanding the global carbon budget and how the 
earth will respond to increases in carbon dioxide emissions. Measuring the mass 
of entire trees is difficult, and it's pretty much impossible to weigh an entire 
forest *even if we were willing to clear cut a forest for science*, but 
fortunately we can estimate the mass of a tree based on its diameter.

There are lots of equations for estimating the mass of a tree from its diameter, 
but one good option is the equation M = 0.124 * D<sup>2.53</sup>, where M is measured in 
kg of dry (above-ground) biomass and D is in cm d.b.h. (Brown 1997). We're going 
to estimate the total tree biomass for trees in a 96 hectare area of the Western 
Ghats in India.

1.  Write a function that takes a vector of tree diameters as an argument and   
    returns a vector  of tree masses.
2.  [The raw data](http://esapubs.org/archive/ecol/E091/216/Macroplot_data_Rev.txt)
    is available on [Ecological Archives](http://esapubs.org/Archive/), but
    unfortunately due to poor database structure using all of the trees would be
    a hassle. You could try to solve this problem yourself, but it turns out
    that someone else has already solved it for you. Install the
    [EcoData Retriever](http://ecodataretriever.org/) and use it to download and
    cleanup this data automatically (using the command line interface the
    command would be `retriever install csv Ramesh2010` and the data will be
    stored in `Ramesh2010_macroplots.csv`) and import it into R.
3.  If you look at the file or [the
    metadata](http://esapubs.org/archive/ecol/E091/216/metadata.htm)
    carefully you'll notice that the data is actually in girth (i.e.,
    circumference, which is equal to pi * diameter) rather than
    diameter. Write a function to take an vector of circumferences as an
    argument and returns an vector of diameters.
4.  Use the two functions you've written to estimate the total biomass
    (i.e., the sum of the masses) of trees in this dataset and print the
    result to the screen.
