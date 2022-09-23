---
layout: exercise
topic: NEON
title: Cropping NEON Data
language: R
---

The [National Ecological Observatory Network](http://www.neonscience.org) has invested in [high-resolution airborne imaging](https://www.neonscience.org/data-collection/airborne-remote-sensing) of their field sites. 
Elevation models generated from [LiDAR](https://www.neonscience.org/resources/learning-hub/tutorials/lidar-basics) can be used to map the topography and vegetation structure at the sites.

Check to see if there is a `data` directory in your workspace with an `SJER` subdirectory in it.
If not, [Download the data]({{ site.baseurl }}/data/neon-geospatial-data.zip) and extract it into your working directory.
The `SJER` directory contains csv data on plot locations (`sjer_plots.csv`), raster data for a digital terrain model (`SJER_dtmFull.tif`) and a digital surface model (`SJER_dsmFull.tif`), and vector data on the site boundary (`sjer_boundary.shp`) for the [San Joaquin Experimental Range](http://www.fs.fed.us/psw/ef/san_joaquin/). 

1. Load the csv plots data (`sjer_plots.csv`) as an `sf` object and display that object (don't load the shape files, use the csv file). The data is in latitudes and longitudes, so the CRS code is 4326.
2. Reproject the plots data to the UTM coordinates of the DTM data (`SJER_dtmFull.tif`) and display the resulting object.
3. Crop the DTM data to the site boundary (`sjer_boundary.shp`). To do this, first reproject the site boundary to have the same CRS as the DTM. Make a map showing the site boundary and the cropped DTM data without null values. Use the viridis color ramp.
4. Use a bounding box to crop both the DTM data and the plots data. The bounding box should have `xmin = 256500`, `xmax = 257500`, `ymin = 4110000`, and `ymax = 4111000`. Make a map showing the cropped DTM (with no null values and the viridis color ramp) and the cropped points. Display the plot in the UTM coordinates.
5. Save the map from (4) as an image named `sjer_cropped_figure.png`.
6. Write the cropped DTM from (4) to a geotiff file. Name it `sjer_dtm_cropped.tif`. Write the cropped plots data from (4) to a shape file. Name it `sjer_plots_cropped.shp`.
