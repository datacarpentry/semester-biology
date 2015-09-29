---
layout: exercise
title: Scientific 0
subtitle: Shrub Volume Pt 3
language: R
---

This is a follow-up to [Data Frames]({{ site.baseurl }}/exercises/Data-frames-R)

Dr. Granger is interested in studying the factors controlling the size and
carbon storage of shrubs. This research is part of a larger area of research
trying to understand carbon storage by plants. She has conducted a small
preliminary experiment looking at the effect of three different treatments on
shrub volume at four different locations. She has placed a data file on the web 
for you to [download]({{ site.baseurl }}/data/shrub_volume_experiment.csv).

You want to get familiar with the data so…

1. Import the shrub dimensions data using `read.csv()`. 
2. Check the column names in the data using the function `names()`
3. Print out the first few rows of the data using the function `head()`.
4. Select the data from the length column and print it out.

   Use `dplyr` to complete the remaining tasks.
5. Select the data from the site and experiment columns and print it out.
6. Filter the height data for all of the plants with heights greater than 5 and
   print out the result.
 
   This code calculates the average height of a plant at each site:

   ```
   by_site <- group_by(shrub_dims, site)
   avg_height <- summarize(by_site, avg_height = mean(height))
   ```
7. Modify the code to calculate and print the average height of a plant in each 
experiment.
8. Determine the maximum height of a plant in each site and print it out.
9. Create a new data frame called `shrub_data_w_vols` that includes all of the
   original data and a new column containing the volumes.
