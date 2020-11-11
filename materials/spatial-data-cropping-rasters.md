---
layout: page
element: notes
title: Cropping/Masking Spatial Data
language: R
--- 

* Spatial data is often larger than we need it to be
* E.g., Raster data is typically a large rectangular block of data
* And we are often only interested in the portion of that data that is located inside our study region
* To get the piece of spatial data that we want for our maps or analysis we can "crop" the data
* We'll look at this using the data from Harvard forest we've been working with so far

```r
library(stars)
library(sf)
library(ggplot2)

harv_dtm <- read_stars("data/HARV/HARV_dtmCrop.tif")
harv_boundary <- st_read("data/HARV/harv_boundary.shp")
harv_soils <- st_read("data/HARV/harv_soils.shp")

ggplot() +
  geom_stars(data = harv_dtm) +
  scale_fill_viridis_c() +
  geom_sf(data = harv_boundary, alpha = 0)
```

### Cropping a raster using to a vector polygon

* There are two general approaches to cropping data
* The first is to crop a raster to only keep the portion that falls inside some vector data
* For example, we often only want the portion of a raster dataset that falls inside the boundar of our study site
* We can do this using the `st_crop` function
* The first argument is the raster we want to crop
* The second argument is the vector data we want to crop it to
* Let's crop our raster to only include points inside the site boundary

```r
harv_dtm_cropped <- st_crop(harv_dtm, harv_boundary)
```

* Let's plot the cropped raster to see what it looks like 

```r
ggplot() +
  geom_stars(data = harv_dtm_cropped) +
  scale_fill_viridis_c() +
  geom_sf(data = harv_boundary, alpha = 0)
```

* We now see colored values only for the part of the part of the raster inside the boundary
* But we still see gray boxes outside of it
* These boxes indicate that the values have been replaced with null values
* Since it's the full extent of the original raster this is technically "masking" instead of "cropping"
* We can not show these null values by setting their color to be transparent

```r
ggplot() +
  geom_stars(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, alpha = 0)
```

## Cropping to a bounding box

* The other common approach to cropping is to crop spatial objects to only include those within a bounding box
* E.g., we might only want to explore a specific area within Harvard Forest
* We still use `st_crop` to do this but we pass it a square region instead of a polygon
* To do this we need to know the values for the region we want to crop
* To figure out these values let's modify our plot to plot in the CRS of our data

```r
ggplot() +
  geom_stars(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, alpha = 0) +
  coord_sf(datum = st_crs(dtm_harv))
```

* We create a bounding box using the `st_bbox` function
* We describe the square based on the largest and smallest values of both x and y
* We provide this information in a named vector
* We create this using the `c` function, but giving names to each value using the name we want and the `=`
* The names for the bounding box are `xmin`, `xmax`, `ymin`, `ymax`
* And we also need to provide the CRS

```r
bbox <- st_bbox(c(xmin = 731000, ymin = 4713000, xmax = 732000, ymax = 4714000), crs = st_crs(dtm_harv))
```

* So let's crop a square in this region here

```r
harv_dtm_small <- st_crop(harv_dtm, bbox)
```

* We can also perform bounding box cropping on vector data
* Let's also crop our soils data

```r
harv_soils_small <- st_crop(harv_soils, bbox)
```

* For `sf` vector data we can also skip teh `st_bbox` function and just pass the named vector with xmin, xmax, ymin, and ymax directly

* Let's plot our cropped regions together

```r
ggplot() +
  geom_stars(data = harv_dtm_small) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_soils_small, alpha = 0)
```