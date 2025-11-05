---
layout: page
element: notes
title: Saving Spatial Data From R
language: R
---

* Once we've created new spatial objects in R we often want to save them so they can be used later or shared with others
* Let's start where we left off when cropping data

```r
library(sf)
library(terra)

harv_boundary <- read_sf("data/harv/harv_boundary.shp")
harv_dtm <- rast("data/harv/harv_dtmfull.tif")

bbox <- st_bbox(c(xmin = 731000, ymin = 4713000, xmax = 732000, ymax = 4714000), crs = st_crs(dtm_harv))
harv_dtm_small <- crop(harv_dtm, bbox)
harv_soils_small <- crop(harv_soils, bbox)
```

### Writing raster data

* To save data we use `write` functions
* So to save the DTM that was cropped to Harvard Forest boundary we use `writeRaster`
* The first argument is the object we want to write and the second is the file name
* The format of the raster will be determined by the file extension
* To save as geotiff we use `.tif`

```r
writeRaster(harv_dtm_small, "harv_dtm_small.tif")
```

* We can see that this worked by reading it back in

```r
rast("harv_dtm_small.tif")
```

* We can see this is the cropped data because it's dimensions are < 150 x 150

### Writing sf vector data

* To save data `sf` vector data we use `write_sf`
* Again the arguments are the object to be written and the name of the file to write to
* With the extension indicating the file type

```r
write_sf(harv_soils_small, "harv_soils_small.shp")
```

* If we look in the `Files` tab we can see this created a full set of the files that make up a single shape file

### Saving maps

- We can save ggplot maps in the same way we save other ggplots

```r
ggsave("harv_map.png")
```

> Do Tasks 5-6 of [Cropping NEON Data]({{ site.baseurl }}/exercises/Neon-cropping-neon-data-R).
