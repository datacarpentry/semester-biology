---
layout: exercise
topic: NEON
title: Canopy Height from Space
language: R
---

The [National Ecological Observatory Network](http://www.neonscience.org) has invested in [high-resolution airborne imaging](http://www.neonscience.org/data-resources/get-data/airborne-data) of their field sites. 
Elevation models generated from [LiDAR](http://neondataskills.org/self-paced-tutorial/1_About-LiDAR-Data-Light-Detection-and-Ranging_Activity1/) can be used to map the topography and vegetation structure at the sites.
This data gets really powerful when you can compare ecological processes across 
sites. 
[Download]({{ site.baseurl }}/data/NEON-airborne.zip) the elevation models for the [Harvard Forest](http://harvardforest.fas.harvard.edu/) (`HARV`) and [San Joaquin Experimental Range](http://www.fs.fed.us/psw/ef/san_joaquin/) (`SJER`) 
and the plot locations for each of these sites. 
Often, plots within a site are used as representative samples of the larger site 
and act as reference areas to obtain more detailed information and ensure 
accuracy of satellite imagery (*i.e., ground truth*).

1. Map the digital surface model for `SJER`.
2. Create and map the [Canopy Height Model](https://datacarpentry.org/r-raster-vector-geospatial/04-raster-calculations-in-r/index.html) using `raster` math (`chm = dsm - dtm`) for `SJER` site.
3. Creat a map that combines the Canopy Height Model from 3 with the corresponding plot locations from the `plot_locations` folder.
4. Extract the canopy heights at each plot location for `SJER` and display the values.
5. Extract the maximum canopy heights (using `fun = max`) in a buffer of 10 for each point at the `HARV` site and `SJER` plots. Create a single dataframe with two columns, one holding the maximum height values for each site at each `plot_id`.
