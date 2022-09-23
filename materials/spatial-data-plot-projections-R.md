---
layout: page
element: notes
title: Changing the Plot Projection in ggplot
language: R
--- 

* We've talked about how different spatial data have different projections which have different units
* But you may have noticed that something a little funny happens with these units when we plot data using ggplot
* Let's start where we did at the beginning of the last lesson
* Having already loaded the packages we need and imported the Harvard Forest soils data and digital terrain model

```r
library(sf)
library(stars)
library(ggplot2)

harv_soils <- st_read("data/HARV/harv_soils.shp")
harv_dtm <- read_stars("data/HARV/HARV_dtmFull.tif")
```

* Let's look at the coordinate reference systems for these two data sets

```r
st_crs(harv_soils)
st_crs(harv_dtm)
```

* So both data sets in are UTM Zone 18 North

* If we plot the raster data on it's own it is in UTM units

```r
ggplot() +
  geom_stars(data = harv_dtm)
```

* It has the large numbers we've seen before on the axes
* Now let's add the soils data

```r
ggplot() +
  geom_stars(data = harv_dtm) +
  geom_sf(data = harv_soils, alpha = 0)
```

* Now all of a sudden we have latitudes and longitudes instead of our UTM coordinates
* This happens because by default `geom_sf` changes the units to latitude and longitude values
* To change the units to another projection, like the projection of the data, we use `coord_sf`
* Which takes a CRS and shows the axes in those units
* So if we want this graph in the units of the projection of our data we can look up the CRS and use that

```r
ggplot() +
  geom_stars(data = harv_dtm) +
  geom_sf(data = harv_soils, alpha = 0) +
  coord_sf(datum = st_crs(harv_dtm))
```

* We could also use the numeric code for the CRS instead if we want to