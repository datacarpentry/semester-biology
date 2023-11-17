---
layout: page
element: notes
title: Spatial Data Extracting Raster Values
language: R
--- 

> Setup:
> 
> ```r
> library(ggplot2)
> library(sf)
> library(stars)
> dtm_harv <- read_stars("data/HARV/HARV_dtmCrop.tif")
> plots_harv <- read_sf("data/HARV/harv_plots.shp")
> ```

### Extract raster data at points

* One of the common tasks we want to perform in geospatial analysis is extracting data from rasters for use in our analyses
* We might want information on elevation or precipitation from a raster
* Or we might want information on soils from a set of polygons

* We'll start with the code we used last time to load in our digitial terrain model and plot locations
* The raster and the vector data need to have the same CRS so let's go ahead and transform our point locations to the UTM Zone for the raster data
* Remember that we do this using `st_transform` which takes the object to be transformed and the CRS we want to transform it to
* To get that CRS we'll use `st_crs` to ge the CRS for the raster data

```r
plots_harv_utm <- st_transform(plots_harv, st_crs(dtm_harv))
```

* To get the raster values associated with vector data we use the `st_extract` function
* `st_extract` takes two main arguments
* The raster object that we want to extract information from
* The vector object indicating where we want the to get the information from the raster
* To extract the average elevation of each of our plots

```r
plot_elevations = st_extract(dtm_harv, plots_harv_utm)
```

* If we look at `plot_elevations` we can see that it is a simple features collection with an elevation for each point
* We can access the values directly using the `$`

```r
plot_elevations$harv_dtmcrop.tif
```

* The name of the vector comes from the raster file name
* These extracted values are in the same order as the features in the vector object
* So we can add them to our existing spatial data frame using standard approaches

```r
library(dplyr)
plot_harv_elevations <- mutate(plots_harv_utm, elevations = plot_elevations$harv_dtmcrop.tif)
```

* We can add these data to the information in our original `plots_harv_utm` object using a spatial join, which will combine things from the same locations
* Works like `inner_join()`

```r
plot_harv_elevations <- st_join(plots_harv_utm, plot_elevations)
```

> Do Tasks 4-5 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).

### Extract raster data at points with buffers

* So far we've extracted raster data at points
* So we just get the value in the single pixel that the point falls inside
* We often want data in larger areas around points
* We can do this by buffering those points
* Let's get the average canopy height within 25 m of the center of each plot
* First, we buffer the plots
* The second argument is the distance from the point to include in the buffer
* The radius of the circle

```r
plots_harv_buffered <- st_buffer(plots_harv_utm, dist = 25)
plots_harv_buffered
```

* This changes the geometry to polygon
* The units for `dist` are in the units of the vector object
* UTM is in units of meters so here we're saying within 25 m

```r
st_crs(plots_harv_utm)$units
```

* Plot our buffered objects

```r
ggplot() +
  geom_stars(data = dtm_harv) +
  geom_sf(data = plots_harv_buffered, fill = "transparent", color = "white")
```

* Now we can run `st_extract()` on that buffered data

```r
plot_elevations_buffered <- st_extract(dtm_harv, plots_harv_buffered)
plot_elevations_buffered
```

* This initially creates a stars object, but we can convert it back to a simple features object

```r
plot_elevations_buffered <- st_as_sf(plot_elevations_buffered)
plot_elevations_buffered
```