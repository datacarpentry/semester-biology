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
* This allows us to combine it with other spatial data for analyses

* To do this we use the `st_read` function
* The first argument is still the name of the file we are going to read
* We also need to tell it which columns the spatial data is located in
* We do this using the `options` argument, which is a vector containing two strings
* `"X_POSSIBLE_NAMES=colnameforx"` and `"Y_POSSIBLE_NAMES=colnamefory"`
* Finally we need to indicate what the CRS is for the data using the `crs` argument
* If it's lat/long data this is `4326`
* If it's a UTM zone then enter the appropriate code for that zone

```r
library(sf)
location_data <- st_read("./pts.csv",
                         options=c("X_POSSIBLE_NAMES=long","Y_POSSIBLE_NAMES=lat"),
		                 crs = 4326)
```

* If we look at `location_data` we can see that it looks like all of our other vector data
* We can plot, reproject, and `extract` values from rasters using this data just like we can from shape files
* We can even save it as a shape file if we want, which we'll see how to do in the lesson on save spatial data
