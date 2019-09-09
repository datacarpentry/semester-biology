---
layout: exercise
topic: Graphing
title: Sexual Dimorphism Data Manipulation
language: R
---

This is a follow up to [Sexual Dimorophism Exploration]({{ site.baseurl }}/exercises/Graphing-sexual-dimorphism-exploration-R).

Having done some basic visualization of the
[Lislevand et al. 2007](https://doi.org/10.1890/06-2054)
[dataset of bird size measures](http://www.esapubs.org/archive/ecol/E088/096/avian_ssd_jan07.txt)
you realize that you'll need to do some data manipulation to really get at the
questions you want to answer.

1. In [Sexual Dimorophism Exploration]({{ site.baseurl }}/exercises/Graphing-sexual-dimorphism-exploration-R)
   you created a plot of the histograms of female and male masses by family. This
   resulted in a lot of plots, but many of them had low sample sizes.

   Use `dplyr` to filter out null values for mass, group the data by family,
   and then filter the grouped data to return data only for families with more
   than 25 species. Add a comment to the top of the block of code describing
   what it does.
    
   Now, remake your original graph using only the data on families with greater
   than 25 species.

2. Sexual size dimorphism doesn't seem to show up clearly when visually
   comparing the distributions of male and female masses across species. Maybe
   the differences among species are too large relative to the differences 
   between sexes to see what is happening; so, you decide to calculate the
   difference between male and female masses for each species and look at the
   distribution of those values for all species in the data.
   
   In the original data frame, use `mutate()` to create a new column which is the 
   relative size difference between female and male masses 

   `(F_mass - M_mass) / F_mass`

   and then make a single histogram that shows all of the species-level
   differences. Using `geom_vline` add a vertical line at 0 difference for
   reference.

3. Combine the two other tasks to produce histograms of the relative size
   difference for each family, only including families with more than 25
   species.

4. Save the figure from task 3 as a jpg file with the name
   `sexual_dimorphism_histogram.jpg`. 
