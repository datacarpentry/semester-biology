---
layout: exercise
topic: Tidyr
title: Tree Biomass
language: R
---

Estimating the total amount of biomass (*the total mass of all individuals*) 
in forests is important for understanding the global carbon budget and how the 
earth will respond to increases in carbon dioxide emissions. We can estimate
the mass of a tree based on its diameter.

There are lots of equations for estimating the mass of a tree from its diameter, 
but one good option is the equation: 
    
Mass = 0.124 * Diameter<sup>2.53</sup>

where `Mass` is measured in kg of dry above-ground biomass and
`Diameter` is in cm
[DBH](https://en.wikipedia.org/wiki/Diameter_at_breast_height)
([Brown 1997](http://www.fao.org/docrep/W4095E/W4095E00.htm)).

We're going to estimate the total tree biomass for trees in a 96
hectare area of the Western Ghats in India.
The data needs to be tidied before all of the tree stems can be used for analysis.
f
If the [`Macroplot_data_Rev.txt`](http://datacarpentry.org/semester-biology/data/Macroplot_data_Rev.txt) is not already in your working directory download a copy.

1. Use `pivot_longer()` to create a longer data frame with one row for each measured stem. Use dplyr's `filter` function to remove all of the girths that are zero. Store this longer data frame in a variable and also display it.
2. Write a function that takes a vector of tree diameters as an argument and   
   returns a vector of tree masses using the equation above. Test it using `mass_from_diameter(22)`.
3. Stems are measured in girth (*i.e., circumference*) rather than diameter.
   Write a function that takes a vector of circumferences as an argument
   and returns a vector of diameters (`diameter = circumference / pi`). Test it using `diameter_from_circumference(26)`.
4. Use the two functions you've written to and dplyr to add a `mass` column to your longer data frame. Store this data in a variable and display it.
5. Estimate the total biomass by summing the mass of all of the stems in dataset.
6. `separate()` the `SpCode` column into `GenusCode` and `SpEpCode` columns and then use `group_by` and `summarize` to the total biomass for each unique `GenusCode`.
7. Use ggplot to make a histogram of the `diameter` values. Make the x label `"Diameter [cm]` and the y label `"Number of Stems"`