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

1. Generate a [Canopy Height Model](http://neondataskills.org/R/Raster-Calculations-In-R/) for each site (`HARV` and `SJER`) using simple `raster` math, where `chm = dsm - dtm`.

2. `plot()` the `chm` and `hist()` of canopy heights for each site on a single 
panel. *The `raster` package modifies `plot()` from the basic R `graphics` 
package, so use `par(mfrow=c(2,2), mar=c(5, 4, 2, 2))` prior to plotting to get 
the four figures on the same panel and to set margins to make labels visible.*

3. Add the `plot_locations` to the site images. *Use the `add=TRUE` argument in another `plot()` immediately proceeding plotting the site image to add the plot points.*

   *Don't see the `plot_locations` on the map??? Compare the `crs(chm)` to 
   `crs(plot_locations)`. [HINT:](http://neondataskills.org/R/vector-data-reproject-crs-R/) They should be the same.* 

4. Extract the maximum canopy heights for each plot at both sites within 10
   meters of the center of the plot.
