---
layout: exercise
topic: Statistics
title: Shrub Volume 3
language: Python
---

This is a follow up to [Shrub Volume 2]({{ site.baseurl }}/exercises/Scientific-shrub-volume-2-Python).

Dr. Granger is interested in studying the factors controlling the size and
carbon storage of shrubs. This research is part of a larger area of research
trying to understand carbon storage by plants. She has conducted a small
preliminary experiment looking at the effect of three different treatments on
shrub volume at four different locations. She wants to conduct a preliminary
analysis of these data to include in a grant proposal and she would like you to
conduct the analysis for her (she might be a world renowned expert in carbon
storage in plants, but she sure doesn't know much about computers). She has
placed a data file on the web for you to
[download]({{ site.baseurl }}/data/shrub_volume_experiment.csv). She wants you to run an ANOVA to
determine if the different experimental treatments lead to differences in shrub
carbon.

1. Import the data using Pandas and print out the first few rows of the data
   using the `.head()` method.
2. Write a function to calculate the shrub carbon using a column of lengths, a
   column of widths and a column of heights, using the equation                             
     `1.8 + 2 * log(volume)` where `volume` is the volume of the shrub. You'll 
   need to use the `numpy` version of the `log()` function. Call the function to  
   get a column of shrub carbons and then print out that column.
3. Use this function to get a column of carbons for all of the shrubs in the
   table and append that column to your existing dataframe using a command like
   `data['carbon'] = get_shrub_carbons(lengths, widths, heights)`. Print out the
   entire dataframe.
4. Do an ANOVA to determine if the experiment has an influence on the shrub
   carbon and print out the results in a standard ANOVA table using
   `anova_lm()`. You can import `anova_lm()` using `from statsmodels.stats.anova
   import anova_lm`.
