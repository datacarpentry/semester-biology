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
> plots_harv <- st_read("data/HARV/harv_plots.shp")
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

* To get the raster values associated with vector data we use the `aggregate` function
* `aggregate` takes three main arguments
* The raster object that we want to extract information from
* The vector object indicating where we want the to get the information from the raster
* The function for combining multiple pixels

* To extract the average elevation of each of our plots

```r
plot_elevations = aggregate(dtm_harv, plots_harv_utm, mean, as_points = FALSE)
```

* The last argument has to do with how R treats the raster data
* It prevents it from approximating that data as points (which can be faster, but doesn't work when extracting values at point locations)

* If we look at `elevs_points` we can see that it has a list of elevations, one for each point
* These values can be accessed directly using the `$`

```r
plot_elevations$HARV_dtmCrop.tif
```

* The name of the vector comes from the raster file name
* These extracted values are in the same order as the features in the vector object
* So we can add them to our existing spatial data frame
* We can do this using the `dplyr` `mutate` function that we've used before

```r
mutate(plots_harv_utm, elevations = plot_elevations$HARV_dtmCrop.tif)
```

* Or by assigning it to a new column in our existing data frame

```r
plots_harv_utm$elevations <- plot_elevations$HARV_dtmCrop.tif
```

### Extract raster data within polygons

* When extracting data at points there is only one pixel per point and so we get back a single elevation
* We often want to extract data from rasters inside of a polygon or along a line
* In that case ther are multiple values for the raster
* This is where the third argument in `aggregate` becomes important
* It provides the function for turning all of those pixels into a single value
* Look at this by extracting elevations in different soil regions within Harvard Forest
* Load the soil maps using `st_read` and convert them to the same projection as the raster

```r
soils_harv <- st_read("data/HARV/harv_soils.shp")
soils_harv_utm <- st_transform(soils_harv, st_crs(dtm_harv))
```

* We can look at what this data looks like

```r
ggplot() +
  geom_sf(soils_harv_utm)
```

* We can see that it is a bunch of 
* Often want values surrounding a point, not just the single pixel that the
  point lands in
* Do this using `buffer` to get the values for all pixels within some buffer
  distance from the point

```
extract(chm_harv, plots_harv_utm, buffer = 10)
```

* This returns one value for each pixel within the buffer region
* Also what output is like for line and polygon data
* One value for each cell intersected by a line or each cell inside a polygon

* Could keep all of this data, or calculate a value from it
* Often want an average

```
extract(chm_harv, plots_harv_utm, buffer = 10, fun = mean)
```

> Do Tasks 4-5 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).