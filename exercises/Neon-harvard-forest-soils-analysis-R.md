---
layout: exercise
topic: NEON
title: Harvard Forest Soils Analysis
language: R
---

The [National Ecological Observatory Network](http://www.neonscience.org) has invested in [high-resolution airborne imaging](https://www.neonscience.org/data-collection/airborne-remote-sensing) of their field sites. 
Elevation models generated from [LiDAR](https://www.neonscience.org/resources/learning-hub/tutorials/lidar-basics) can be used to map the topography and vegetation structure at the sites.

Check to see if there is a `data` directory in your workspace with `harv` subdirectory in it.
If not, [Download the data]({{ site.baseurl }}/data/neon-geospatial-data.zip) and extract it into your working directory.
The `harv` directory contains spatial data for Harvard Forest including raster data for a digital terrain model (`harv_dtmfull.tif`) and a digital surface model (`harv_dsmfull.tif`), and polygon data for the site boundary (`harv_boundary.shp`) and the soil types (`harv_soils.shp`).

1. Make a map of the `harv_soils` data with the polygons colored based on `DRAINAGE_C` column. Use the viridis color ramp.
2. Make a map of the `harv_soils` data with one facet (i.e., subplot) for each category in the `DRAINAGE_C` column.
3. Using the `harv_dtmfull.tif` and `harv_dsmfull.tif` rasters create a canopy height model (DSM - DTM) and extract the maximum canopy height (i.e., the CHM value) within each soils polygon. To get the maximum canopy height instead of the mean value use the `max` function instead of `mean`. Display a vector of the resulting canopy height.
4. Add the vector of canopy heights from (3) to the original `sf` object and display the resulting data frame.
5. Make a map of the soil polygons colored based on their maximum canopy height. Use the viridis color ramp.
6. Make a map that is the same as (5), but preserves the UTM coordinates on the axes.
