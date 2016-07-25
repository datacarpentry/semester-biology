---
layout: exercise
topic: Tidyr
title: Tree Biomass
language: R
---

Estimating the total amount of biomass (*the total mass of all individuals*) 
in forests is important for understanding the global carbon budget and how the 
earth will respond to increases in carbon dioxide emissions. Measuring the mass 
of whole trees is a major effort and requires destructive harvest of the tree. 
Fortunately, we can estimate the mass of a tree based on its diameter.

There are lots of equations for estimating the mass of a tree from its diameter, 
but one good option is the equation: 
    
Mass = 0.124 * Diameter<sup>2.53</sup>

where `Mass` is measured in kg of dry above-ground biomass and `Diameter` is in cm [DBH](https://en.wikipedia.org/wiki/Diameter_at_breast_height) ([Brown 1997](http://www.fao.org/docrep/W4095E/W4095E00.htm)). 

We're going to estimate the total tree biomass for trees in a 96 hectare area of 
the Western Ghats in India. [The raw data](http://esapubs.org/archive/ecol/E091/216/Macroplot_data_Rev.txt) is available on [Ecological Archives](http://esapubs.org/Archive/). Unfortunately, the data is stored in a poor database 
structure and using all of the tree stems would be difficult without first 
tidying up the data. You can have a look at [the metadata](http://esapubs.org/archive/ecol/E091/216/metadata.htm) to get familiar with the data structure.

1. Use `tidyr` to `gather()` the raw data into rows for each measured stem. 
2. Write a function that takes a vector of tree diameters as an argument and   
returns a vector of tree masses.
3. Stems are measured in girth (*or circumference*) rather than diameter. Write a function that takes a vector of circumferences as an argument and returns a vector of diameters (*circumference = pi \* diameter*).
4. Use the two functions you've written to estimate the total biomass (*i.e., 
the sum of the masses*) of trees in this dataset and print the result to the
screen.
5. `separate()` the `SpCode` into `GenusCode` and `SpEpCode` and estimate the 
total biomass per genus in a table. *Technically the four letter code doesn't 
uniquely identify all of the genera in the dataset, but we'll assume it does for 
the purpose of this exercise.* 
