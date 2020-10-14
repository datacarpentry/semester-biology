---
layout: page
element: notes
title: Spatial Data Create Vector Data
language: R
--- 

### Making your own vector data

* Some data that is spatial doesn't come prepackaged as a spatial object
* One common instance of this is spatial location data collected using a GPS
* The `sf` package let's us load data with spatial coordinates, like latitude and longitude, as spatial data

```r
library(sf)
```

* This allows us to combine it with other spatial data for analyses

* For example, what if our plot data for Harvard Forest as originally provided as a table with latitude and longitude columns instead of a shape file?
* We have a version of the plots data that is stored like this in `harv_plots.csv`

* To read in data like this as a spatial object we use the `st_read` function
* The first argument is still the name of the file we are going to read

```r
harv_plots <- st_read("data/HARV/harv_plots.csv")
```

* But now we also need to tell it which columns the spatial data is located in
* We do this using the `options` argument, which is a vector containing two strings
* `"X_POSSIBLE_NAMES=colnameforx"` and `"Y_POSSIBLE_NAMES=colnamefory"`
* In our case those column names are `longitude` and `latitude`

```r
harv_plots <- st_read("data/HARV/harv_plots.csv",
                      options = c("X_POSSIBLE_NAMES=longitude", "Y_POSSIBLE_NAMES=latitude"))
```

* Finally we need to indicate what the CRS is for the data using the `crs` argument
* If it's lat/long data this is `4326`

```r
harv_plots <- st_read("data/HARV/harv_plots.csv",
                      options = c("X_POSSIBLE_NAMES=longitude", "Y_POSSIBLE_NAMES=latitude"),
                      crs = 4326)
```

* If the data is stored in UTM coordinates then enter the appropriate code for that zone

* If we look at `harv_plots` we can see that it looks like all of our other vector data
* We can plot, reproject, and `extract` values from rasters using this data just like we can from shape files
* We can even save it as a shape file if we want, which we'll see how to do in the lesson on save spatial data
