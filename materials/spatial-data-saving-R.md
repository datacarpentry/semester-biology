---
layout: page
element: notes
title: Saving Spatial Data From R
language: R
--- 

* Once we've new spatial objects in R we often want to save them so they can be used later or shared with others
* Let's start where we left off when cropping data

```r
library(stars)
library(sf)
library(ggplot2)

harv_boundary <- st_read("data/HARV/harv_boundary.shp")
harv_dtm <- read_stars("data/HARV/HARV_dtmFull.tif")

harv_dtm_cropped <- st_crop(harv_dtm, harv_boundary)

bbox <- st_bbox(c(xmin = 731000, ymin = 4713000, xmax = 732000, ymax = 4714000), crs = st_crs(dtm_harv))
harv_dtm_small <- st_crop(harv_dtm, bbox)
harv_soils_small <- st_crop(harv_soils, bbox)
```

### Writing stars raster data

* To save data we use the `write` versions of the `read` functions
* So to save the DTM that was cropped to Harvard Forest boundary we use `write_stars`
* The first argument is the object we want to write and the second is the file name
* The format of the raster will be determined by the file extension
* To save as geotiff, which we've been working with, we'll use `.tif

```r
write_stars(harv_dtm_cropped, "harv_dtm_cropped.tif")
```

* We can see that this worked by reading it back in

```r
read_stars("harv_dtm_cropped.tif")
```

* We can see this is the cropped data because it's dimensions are < 150 x 150

### Writing sf vector data

* To save data `sf` vector data we use `st_write`
* Again the arguments are the object to be written and the name of the file to write to
* With the extension indicating the file type

```r
st_write(harv_soils_small, "harv_soils_small.shp")
```

* If we look in the `Files` tab we can see this created a full set of the files that make up a single shape file
 