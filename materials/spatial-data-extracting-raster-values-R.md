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
> dtm_harv <- read_stars("data/harv/harv_dtmcrop.tif")
> plots_harv <- read_sf("data/harv/harv_plots.shp")
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

* If we look at `plot_elevations` we can see that it is a data frame with an elevation for each point

* We can add these data to the information in our original `plots_harv_utm` object using a spatial join, which will combine things from the same locations

```r
st_join(plots_harv_utm, plot_elevations)
```

* Or we can access the values can be accessed directly using the `$`

```r
plot_elevations$harv_dtmcrop.tif
```

* The name of the vector comes from the raster file name
* These extracted values are in the same order as the features in the vector object
* So we can add them to our existing spatial data frame
* We can do this using the `dplyr` `mutate` function that we've used before

```r
mutate(plots_harv_utm, elevations = plot_elevations$harv_dtmcrop.tif)
```

* Or by assigning it to a new column in our existing data frame

```r
plots_harv_utm$elevations <- plot_elevations$harv_dtmcrop.tif
```

> Do Tasks 4-5 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).