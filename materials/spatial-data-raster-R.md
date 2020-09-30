---
layout: page
element: notes
title: Spatial Data Raster
language: R
--- 

> Remember to download and put into data subdirectory:
>
> * [LiDAR rasters and plot locations]({{ site.baseurl }}/data/NEON-airborne.zip)

> Load the following into browser window:

> * [Raster description](https://datacarpentry.org/organization-geospatial/01-intro-raster-data/)
> * [Canopy Height Model picture](https://datacarpentry.org/r-raster-vector-geospatial/images/dc-spatial-raster/lidarTree-height.png)

> Set-up R Console:

```
library(ggplot2)
```

### Introduction to raster data

* There are two common types of spatial data, raster and vector
* Raster data stores data that is continous across space
* Like climate variables, satellite imagery, and elevation
* It is stored in a gridded format

![Aerial photo of a green landscape.
A section of the landscape is expanded to show that it is composed of green pixels.
This is expanded to show that underlying the green pixels is a matrix of numerical values.
The matrix is then shown as green pixels again to represent plotting the raster.]({{ site.baseurl }}/materials/raster_concept.png)

* In the grid each pixel contains a value
* So it is basically a matrix of numbers of one value at each position in the matrix
* So for elevation we would have a matrix of heights above sea level

### Importing and exploring

* We import raster data using the `raster()` function
* We'll start by importing some elevation data collected from an airplane using an instrument called LIDAR
* One of the values that LIDAR can generate is a Digital Terrain Model or DTM, which is the elevation of the ground

![Drawing of trees on undulating terrain.
A brown line along the top of the terrain indicates the Digital Terrain Model]({{ site.baseurl }}/materials/digital-terrain-model.png)

```r
dtm_harv <- raster("data/NEON-airborne/HARV_dsmCrop.tif")
```

* Looking at this object provides information on the data it contains

```r
dtm_harv
```

* This is "metadata" or "data about "data"
* It is is important because it provides the context of spatial data this raster matrix so that R knows how to work with it
    * `bands`
    * `projection`
    * `units`
    * `min`, `max`, `mean`


### Plotting spatial data with ggplot

* Spatial data can be plotted using either base R or `ggplot`
* We'll use `ggplot` since that's the data visualization tool we're using for this course
* Useful for making nice maps combined with other figures

Making spatial plots with ggplot requires three steps (write on board):

1. Do Spatial Work (just importing so far)
2. Convert to Data Frame (this is what ggplot works with)
3. Make Plots

* For Step 2 we convert using the `as.data.frame` function
* This function is overloaded by `raster` to convert spatial data into spatial data frames
* We tell R we want to keep the spatial coordinates with the optional argument `xy = TRUE`

```
dtm_harm_df = as.data.frame(dsm_harv, xy = TRUE)
```

* *View dtm_harm_df*
* Once we've converted the raster object to a data frame we can plot it using `geom_raster`
* For the aesthetic we use `x = x` and `y = y` for the coordinates and `fill = HARV_dtmCrop` to indicate the column with the elevation values to color by
* We use `fill` instead of `color` because we are changing the fill color of each cell, like with bar plots or histograms

```
ggplot() +
  geom_raster(data = dtm_harm_df, 
              aes(x = x, y = y, fill = HARV_dtmCrop))
```

* Because this is a data frame we can also treat raster values like they are part of
  a normal table

```
ggplot() +
  geom_histogram(data = dtm_harm_df, 
                 aes(x = HARV_dsmCrop))
```

> Do Task 1 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).
