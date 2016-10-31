---
layout: exercise
topic: NEON
title: Phenology from Space
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

These high-resolution images can then be integrated with satellite imagery that 
is gathered more frequently. We will use data collected from [MODIS](http://modis.gsfc.nasa.gov/), 
which orbits the globe every 16 days. 
One common ecological process that can be observed from space is [phenology](https://en.wikipedia.org/wiki/Phenology) (*or seasonal patterns*) of plants.
Multi-band satellite imagery can be processed to provide a vegetation index of greenness called [NDVI](https://en.wikipedia.org/wiki/Normalized_Difference_Vegetation_Index). 
NDVI values range from `-1.0` to `1.0`, where negative values indicate clouds, 
snow, and water; bare soil returns values from `0.1` to `0.2`; and green vegetation returns values greater than `0.3`.
Download [`HARV_NDVI`]({{ site.baseurl }}/data/HARV-NDVI.zip) and [`SJER_NDVI`]({{ site.baseurl }}/data/SJER-NDVI.zip) and place them in a folder with the NEON airborne data. The `zip` contain folders with a year's worth of NDVI sampling 
from MODIS. The files are in order (*and named*) by date and can be organized 
implicitly by sampling period for analysis. 

1. Generate a [Canopy Height Model](http://neondataskills.org/R/Raster-Calculations-In-R/) for each site (`HARV` and `SJER`) using simple `raster` math, where `chm = dsm - dtm`.

2. `plot()` the `chm` and `hist()` of tree heights for each site on a single 
panel. *The `raster` package modifies `plot()` from the basic R `graphics` 
package, so use `par(mfrow=c(2,2), mar=c(5, 4, 2, 2))` prior to plotting to get 
the four figures on the same panel and to set margins to make labels visible.*

3. Add the `plot_locations` to the site images. *Use the `add=TRUE` argument in another `plot()` immediately proceeding plotting the site image to add the plot points.*

   *Don't see the `plot_locations` on the map??? Compare the `chm@crs` to 
   `plot_locations@proj4string`. [HINT:](http://neondataskills.org/R/vector-data-reproject-crs-R/) They should be the same.* 

4. Evaluate and visualize the `mean(NDVI)` [among plots](http://neondataskills.org/R/crop-extract-raster-data-R/) at each site for each 
of the MODIS sampling periods. *Prepare your analysis results in a `data.frame` that is suitable to `ggplot2` so that it is easy to plot the sites in different colors.*

   *Optional: Extract `sampling_day` from the NDVI `file_name` and include that 
   with your `data.frame` for graphing.*

5. Describe the differences in vegetation structure (`chm`) and seasonal phenology (`NDVI`) that you have observed from this analysis.
 
