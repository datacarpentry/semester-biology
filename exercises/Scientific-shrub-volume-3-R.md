---
layout: exercise
topic: Scientific
title: Shrub Volume 3
language: R
---

This is a follow-up to [Shrub Volume 2]({{ site.baseurl }}/exercises/Data-frames-shrub-volume-2-R).

Dr. Granger is interested in studying the factors controlling the size and
carbon storage of shrubs. This research is part of a larger area of research
trying to understand carbon storage by plants. She has conducted a small
preliminary experiment looking at the effect of three different treatments on
shrub volume at four different locations. She has placed two data files on the 
web for you to download:

* [shrub dimensions data]({{ site.baseurl }}/data/shrub_volume_experiment.csv)
* [experiments data]({{ site.baseurl }}/data/shrub_volume_experiments_table.csv)

Download these into your `data` folder and get familiar with the data by 
importing the shrub dimensions data using `read.csv()` and then:

1. Check the column names in the data using the function `names()`.
2. Use `str()` to show the structure of the data frame and its individual 
   columns.
3. Print out the first few rows of the data using the function `head()`.

   Use `dplyr` to complete the remaining tasks.
4. Select the data from the length column and print it out.
5. Select the data from the site and experiment columns and print it out.
6. Filter the data for all of the plants with heights greater than 5 and
   print out the result.
7. This code calculates the average height of a plant at each site:

   ```
   by_site <- group_by(shrub_dims, site)
   avg_height <- summarize(by_site, avg_height = mean(height))
   ```

   Modify the code to calculate and print the average height of a plant in each
   experiment.
8. Use `max()` to determine the maximum height of a plant at each site.
9. Create a new data frame called `shrub_data_w_vols` that includes all of the
   original data and a new column containing the volumes, and display it.
10. Import the experiments data and then use `inner_join` to combine it with the
    shrub dimensions data to automatically add a `manipulation` column to the
    shrub data.
