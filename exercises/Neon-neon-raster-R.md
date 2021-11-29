---
layout: exercise
topic: NEON
title: NEON Raster
language: R
---

Jane just got a job working to develop data products for [NEON](http://www.neonscience.org/). 
She's got to familiarize herself with working with LiDAR data and seeks out the 
great 'Work with Data' [tutorial for raster data](https://www.neonscience.org/resources/learning-hub/workshops/work-lidar-derived-rasters-r). 
Help Jane take the next step and develop a few additional products from the 
[LiDAR Dataset](https://figshare.com/articles/dataset/Week_4_Earth_Analytics_teaching_data_subset_-_lidar_and_insitu_for_California/4620268)

1. Modify the code provided in the tutorial to add the average and minimum
values from the Canopy Height Model to the plot centroids data with the maximum 
values.

2. Add the average, minimum and stem count (`n()`) to the `insitu_maxStemHeight` 
summary (*You might consider renaming it to something more appropriate*). *Do 
you notice more or less deviation from the LiDAR and field sampling data 
for the average and minimum canopy height values? What do you think is going on?*

3. Modify your `insitu...` data to include the difference in average canopy 
height values. Determine values of a linear model and *r*<sup>2</sup> for the  
difference in average canopy height values (`y`) and stem count (`x`). Does a 
polynomial (`poly(x, 2)`) fit better? Plot the data with the best geometric line 
determined by your models and include the *r*<sup>2</sup> value as the title.
