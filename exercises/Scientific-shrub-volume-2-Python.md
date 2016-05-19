---
layout: exercise
topic: Scientific
title: Shrub Volume 2
language: Python
---

*This problem is related to [Shrub Volume]({{ site.baseurl }}/exercises/Combining-basics-shrub-volume-Python),
but using the Pandas library.*

Dr. Granger is interested in studying the factors controlling the size and
carbon storage of shrubs. This research is part of a larger area of research
trying to understand carbon storage by plants. She has conducted a small
preliminary experiment looking at the effect of three different treatments on
shrub volume at four different locations. She wants to conduct a preliminary
analysis of these data to include in a grant proposal and she would like you to
conduct the analysis for her (she might be a world renowned expert in carbon
storage in plants, but she sure doesn't know much about computers). She has
placed a data file on the web for you to
[download]({{ site.baseurl }}/data/shrub_volume_experiment.csv).

1. Import the data using Pandas and print out the first few rows of the data
   using the `.head()` method.
2. Select the data from the length column and print it out.
3. Select the data from the site and experiment columns and print it out.
4. Multiple the length, width, and height columns together to get a volume
   column and print it out.
5. Calculate the shrub carbon for all of the shrubs using the equation
       `1.8 + 2 * log(volume)` where `volume` is the volume of the shrub. 
   You'll need to use the `numpy` version of the `log()` function. 
6. Select the height data for all of the plants with heights greater than 5 and
   print out the result.
7. The following code calculates the average height of a plant at each site:

   ```
   data_means = data.groupby('site').mean()
   data_means['height']
   ```
   Modify the code to calculate the average height of a plant in each experiment type.
8. Calculate the maximum height of a plant in each site and print it out.
