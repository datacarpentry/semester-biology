---
layout: exercise
topic: NEON
title: Canopy Height from Space
language: R
---

The [National Ecological Observatory Network](http://www.neonscience.org) has invested in [high-resolution airborne imaging](http://www.neonscience.org/data-resources/get-data/airborne-data) of their field sites. 
Elevation models generated from [LiDAR](http://neondataskills.org/self-paced-tutorial/1_About-LiDAR-Data-Light-Detection-and-Ranging_Activity1/) can be used to map the topography and vegetation structure at the sites.

[Download]({{ site.baseurl }}/data/NEON-airborne.zip) the elevation models for the [Harvard Forest](http://harvardforest.fas.harvard.edu/) (`HARV`) and [San Joaquin Experimental Range](http://www.fs.fed.us/psw/ef/san_joaquin/) (`SJER`) 
and the plot locations for each of these sites. 
Often, plots within a site are used as representative samples of the larger site 
and act as reference areas to obtain more detailed information and ensure 
accuracy of satellite imagery (*i.e., ground truth*).

1. Map the digital terrain model for `SJER` using the `viridis` color ramp.
2. Create and map the canopy height model for `SJER` using `raster` math (`chm = dsm - dtm`) and the `viridis` color ramp.
3. Create a map that shows the `SJER` boundary and the plot locations colored by `plot_type`.
4. Transform the plot data to have the same CRS as the CHM and create a map that shows the canopy height model from (3) with the plot locations on top.
5. Extract the mean canopy heights at each plot location for `SJER` and display the values.
6. Add the canopy height values from (5) to the spatial data frame you created for the plots and display the full data frame.
7. Create a map that shows the `SJER` boundary and the plot locations colored by the canopy height values.
8. Create a map that shows the canopy height model raster, but in `cm` rather than `m` (i.e., multiply the canopy height model by 100).
9. Create a map that shows the canopy height model raster, the plot locations, and the `SJER` boundary, using transparency as needed to allow all three layers to be seen. Remember all three layers will need to have the same CRS.
10. (*optional*) Conduct an analysis of the relationship between elevation and canopy height at the SJER plots. Start by extracting the mean elevations (i.e., the values from the digital terrain model) at each plot location for `SJER` and adding them to the spatial plots data so that this data now includes both the elevations and the canopy heights. Then make a scatter plot showing the relationship between elevation and canopy height using this data. Color the points by `plot_type` and fit a linear model through all of the points together (not separately by `plot_type`). Finally, use `dplyr` to calculate the average canopy height and average elevation for the two different plot types. Give the axes good labels.