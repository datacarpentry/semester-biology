---
layout: page
element: notes
title: Changing the Plot Projection in ggplot
language: R
---

## Plotting with expected units

* We've talked about how different spatial data have different projections which have different units
* But you may have noticed that something a little funny happens with these units when we plot data using ggplot
* Let's start where we did at the beginning of the last lesson
* Having already loaded the packages we need and imported the Harvard Forest soils data and digital terrain model

```r
library(ggplot2)
library(sf)
library(terra)
library(tidyterra)

harv_soils <- read_sf("data/harv/harv_soils.shp")
harv_dtm <- rast("data/harv/harv_dtmfull.tif")
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
  geom_spatraster(data = harv_dtm)
```

* It has the large numbers we've seen before on the axes
* Now let's add the soils data

```r
ggplot() +
  geom_spatraster(data = harv_dtm) +
  geom_sf(data = harv_soils, alpha = 0)
```

* Now all of a sudden we have latitudes and longitudes instead of our UTM coordinates
* This happens because by default `geom_sf` changes the units to latitude and longitude values
* To change the units to another projection, like the projection of the data, we use `coord_sf`
* Which takes a CRS and shows the axes in those units
* So if we want this graph in the units of the projection of our data we can look up the CRS and use that

```r
ggplot() +
  geom_spatraster(data = harv_dtm) +
  geom_sf(data = harv_soils, alpha = 0) +
  coord_sf(datum = st_crs(harv_dtm))
```

* We could also use the numeric code for the CRS instead if we want to

## Rotating axis labels

* Our x-axis labels are overlapping, which makes the map difficult to read
* Can fix this by rotating the axis labels
* Do this using the `theme()` function, which lets us control many details of how our plots display
* We want to set an element of the x-axis text so we set `axis.text.x`
* We can set the element we want using the `element_text()` function
* And then the name of the element and it's value
* In this case the element is `angle` and we'll set it to 45 degrees

```r
ggplot() +
  geom_spatraster(data = harv_dtm) +
  geom_sf(data = harv_soils, alpha = 0) +
  coord_sf(datum = st_crs(harv_dtm)) +
  theme(axis.text.x = element_text(angle = 45))
```

* This is better, but now our label is starting to overlap our plot
* We can adjust the position using two functions that control the "justificiation"
* `vjust` to control vertical and `hjust` to control horizontal
* Possible values are 0 (left justified), 1 (right justified), and 0.5 (center justified)

```r
ggplot() +
  geom_spatraster(data = harv_dtm) +
  geom_sf(data = harv_soils, alpha = 0) +
  coord_sf(datum = st_crs(harv_dtm)) +
  theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1))
```

* Setting both to 1, for right justified, will align the right edge with the tick

* If to rotate vertically we can use 90 for the angle

```r
ggplot() +
  geom_spatraster(data = harv_dtm) +
  geom_sf(data = harv_soils, alpha = 0) +
  coord_sf(datum = st_crs(harv_dtm)) +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))
```

> Do Task 6 of [Harvard Forest Soils Analysis]({{ site.baseurl }}/exercises/Neon-harvard-forest-soils-analysis-R).
