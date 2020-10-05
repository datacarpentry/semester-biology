---
layout: page
element: notes
title: Spatial Data Raster Math
language: R
--- 

> Show > * [Canopy Height Model picture](https://datacarpentry.org/r-raster-vector-geospatial/images/dc-spatial-raster/lidarTree-height.png)

* We've been working with the DTM data, which is the Digital Terrain Model, or the elevation of the ground
* LIDAR also collects data on the highest point in each location 
* This is used to create a Digital Surface Model or DSM - the elevation of top physical point

![Panel 1: Drawing of trees on undulating terrain. A green line along the top of the trees indicates the Digital Surface Model.
Panel 2: Drawing of trees on undulating terrain. A brown line along the top of the terrain indicates the Digital Terrain Model.
Panel 3: Drawing of trees on a flat terrain. A green line along the top of the trees indicates the Canopy Height Model.
Panel 4: Equation: DSM (Digital Surface Model) - DTM (Digital Terrain Model) = CHM (Canopy Height Model).
]({{ site.baseurl }}/materials/lidarTree-height.png)

* In forested areas we can combine these to create a Canopy Height Model (CHM)
* Do this by subtracting the DTM from the DSM

```r
library(stars)

dtm_harv <- read_stars("data/HARV/HARV_dtmCrop.tif")
dsm_harv <- read_stars("data/HARV/HARV_dsmCrop.tif")
chm_harv <- dsm_harv - dtm_harv
```

* Math happens on a cell by cell (elementwise) basis
* Can then graph this new raster

```
ggplot() +
  geom_stars(data = chm_harv)
```

* This lets us see where there are the tallest trees on the landscape and where there are none

> Do Task 2 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).