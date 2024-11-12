---
layout: page
element: notes
title: Aggregating raster data inside polygons
language: R
--- 

* In a previous lesson we learned how to extract the raster values at points in the landscape
* We can also extract the values inside of polygons
* We'll start by loading the `sf` and `stars` packages and the Harvard Forest soils the elevation data
* But this time we'll load a DTM file that covers the entire site

```r
library(sf)
library(stars)
library(ggplot2)
library(dplyr)

harv_dtm <- read_stars("data/harv/harv_dtmfull.tif")
harv_soils <- read_sf("data/harv/harv_soils.shp")

ggplot() +
  geom_stars(data = harv_dtm) +
  geom_sf(data = harv_soils, fill = "transparent", color = "white")
```

* If we want to understand whether the polygon fields are related to the raster we need to extract data about the raster within each polygon
* We do this using the `aggregate` function just like for points
* The arguments are: the raster, the vector we want to aggregate the values to, and the function we want to use to combine the different pixels
* Let's calculate the average elevation in each soil polygon

```r
elevs_by_soil <- aggregate(harv_dtm, harv_soils, mean)
```

* You can think of this as similar to `group_by` and `summarize` in `dplyr`, but spatial
* The function groups the digital terrain model into groups of pixels that fall inside each soil polygon
* It then calculates the mean value inside each polygon
* These values are stored in

```r
elevs_by_soil$harv_dtmfull.tif
```

* You can add them to our simple features object using your favorite approach
* I'll use `mutate` from `dplyr`

```r
harv_soils_elevs <- mutate(harv_soils, elevation = elevs_by_soil$harv_dtmfull.tif)
```

* Or we can use `st_join`
* To do this we have to first convert `elevs_by_soil` into an `sf` object

```r
elevs_by_soil <- st_as_sf(elevs_by_soil)
```

* And then join

```r
harv_soils_elevs <- st_join(harv_soils, elevs_by_soil, join = st_equals)
```

* The `join = st_equals` indicates that we only want to match polygons that are the same
* `st_join` defaults to using `st_intersects`, which means that any polygons that touch each other will be match

* Once we done this then we can make maps using this information
* So let's plot the our soils map but colored by average elevation within the region

```r
ggplot() +
  geom_sf(data = harv_soils_elevs, mapping = aes(fill = elevation)) +
  scale_fill_viridis_c()
```

> Do Tasks 3-5 of [Harvard Forest Soils Analysis]({{ site.baseurl }}/exercises/Neon-harvard-forest-soils-analysis-R).
