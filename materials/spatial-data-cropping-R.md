---
layout: page
element: notes
title: Cropping and Masking Spatial Data
language: R
--- 

* Spatial data is often larger than we need it to be
* E.g., Raster data is typically a large rectangular block of data
* And we are often only interested in the portion of that data that is located inside our study region
* To get the piece of spatial data that we want for our maps or analysis we can "crop" the data
* We'll look at this using the data from Harvard forest we've been working with so far
* Including the DTM file that covers the entire site

```r
library(stars)
library(sf)
library(ggplot2)

harv_boundary <- st_read("data/HARV/harv_boundary.shp")
harv_dtm <- read_stars("data/HARV/HARV_dtmFull.tif")
```

* If we plot this data we see that we have elevation data for a large square surrounding the site

```r
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

* We can see that the data has been cropped by looking at the extents

```r
harv_dtm
harv_dtm_cropped
```

* `harv_dtm_cropped` has smaller values for `from` and `to` in both the `x` and `y` dimensions
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
* The raster has been "cropped" to the limits of the vector object but rasters are always rectangular
* So these null values fill the space outside of the vector object but within it's x and y extent
* We can choose to not show these null values by setting their color to be transparent

```r
ggplot() +
  geom_stars(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, alpha = 0)
```

* Cropping removes the portion of the raster that is outside the x/y extent of the vector
* If we want to keep the full dimensions of the raster but convert all values outside the vector to NA we "mask" the data instead of cropping it
* Do this with an optional argument `crop = FALSE`

```r
harv_dtm_masked <- st_crop(harv_dtm, harv_boundary, crop = FALSE)
harv_dtm_masked
```

* We can see that it still has the same dimensions as the original raster, 150 x 150
* But if we plot it in the same way as the cropped data we will only see the values inside the vector

```r
ggplot() +
  geom_stars(data = harv_dtm_masked) +
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
  coord_sf(datum = st_crs(harv_dtm))
```

* We create a bounding box using the `st_bbox` function
* We describe the square based on the largest and smallest values of both x and y
* We provide this information in a named vector
* We create this using the `c` function, but giving names to each value using the name we want and the `=`
* The names for the bounding box are `xmin`, `xmax`, `ymin`, `ymax`
* And we also need to provide the CRS

```r
bbox <- st_bbox(c(xmin = 731000, ymin = 4713000, xmax = 732000, ymax = 4714000), crs = st_crs(harv_dtm))
```

* So let's crop a square in this region here

```r
harv_dtm_small <- st_crop(harv_dtm, bbox)
```

* We can also perform bounding box cropping on vector data
* Let's load and then crop our soils data

```r
harv_soils <- st_read("data/HARV/harv_soils.shp")
harv_soils_small <- st_crop(harv_soils, bbox)
```

* For `sf` vector data we can also skip the `st_bbox` function and just pass the named vector with xmin, xmax, ymin, and ymax directly
* Let's plot our cropped regions together

```r
ggplot() +
  geom_stars(data = harv_dtm_small) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_soils_small, alpha = 0)
```