---
layout: page
element: notes
title: Spatial Data Introduction
language: R
--- 

> Remember to download and set-up directory:
>
> * [LiDAR rasters and plots]({{ site.baseurl }}/data/Neon-airborne.zip)
> * [`HARV_NDVI`]({{ site.baseurl }}/data/HARV_NDVI.zip) 
> * [`SJER_NDVI`]({{ site.baseurl }}/data/SJER_NDVI.zip)

> Set-up R Console:

```
library(raster)
library(rgdal)
```

### `raster` structure, import, and plotting

* Spatial data is often organized in a `raster`.
    * gridded format (*like coordinates*)
    * each pixel is a value
* Metadata is important to describe the context of spatial data.
    * `bands`
    * `projection`
    * `units`
    * `min`, `max`, `mean`

```
> GDALinfo("HARV_dsmCrop.tif")
rows        1367 
columns     1697 
bands       1 
lower left origin.x        731453 
lower left origin.y        4712471 
res.x       1 
res.y       1 
ysign       -1 
oblique.x   0 
oblique.y   0 
driver      GTiff 
projection  +proj=utm +zone=18 +datum=WGS84 +units=m +no_defs 
file        HARV_dsmCrop.tif 
apparent band summary:
   GDType hasNoDataValue NoDataValue blockSize1 blockSize2
1 Float64           TRUE       -9999          1       1697
apparent band statistics:
    Bmin   Bmax    Bmean      Bsd
1 305.07 416.07 359.8531 17.83169
Metadata:
AREA_OR_POINT=Area 
```

* `raster()` import

```
> dsm_harv <- raster("HARV_dsmCrop.tif")
> dsm_harv
class       : RasterLayer 
dimensions  : 1367, 1697, 2319799  (nrow, ncol, ncell)
resolution  : 1, 1  (x, y)
extent      : 731453, 733150, 4712471, 4713838  (xmin, xmax, ymin, ymax)
coord. ref. : +proj=utm +zone=18 +datum=WGS84 +units=m +no_defs +ellps=WGS84 +towgs84=0,0,0 
data source : /Users/Zack/Desktop/DataRA/misc-datacarp/Neon-phenology-from-space/NEON-airborne/HARV_dsmCrop.tif 
names       : HARV_dsmCrop 
values      : 305.07, 416.07  (min, max)
```

* `plot(raster)`
    * package modifies R basic `graphics`

```
plot(dsm_harv, main="HARV", xlab="Easting", ylab="Northing")
```

### `raster` math

```
dtm_harv <- raster("HARV_dtmCrop.tif")
chm_harv <- dsm_harv - dtm_harv
```

> Do [Exercise 1 - Phenology from Space]({{ site.baseurl }}/exercises/Neon-phenology-from-space-R), Tasks 1-2.

### Import and reproject shapefiles

* `vector` data can be added to `rasters` to provide reference information
    * `csv`
    * `shapefile`
        * set of multiple files
            * same name, different extensions
        * `readOGR("directory/", "file_name_without_extentsions")`
            * stores data in a single `data.frame`
            * access 'attributes' similar to GIS software using `$`
                * `file_name$site_id`

```
plots_harv <- readOGR("plot_locations/", "HARV_plots")
plot(plots_harv, add=TRUE, pch=1, cex=2, lwd=2)
```

* Uh oh, nothing happened.

```
> plots_harv
class       : SpatialPointsDataFrame 
features    : 5 
extent      : -72.17808, -72.1662, 42.53402, 42.54048  (xmin, xmax, ymin, ymax)
coord. ref. : +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0 
variables   : 2
names       : id, plot_id 
min values  :  1,       1 
max values  :  5,       5 
```

* Coordinate Reference System (*`crs` or 'projection'*) is different from `raster`.
    * reproject `raster` with `projectraster()`
    * reproject `vector` with `spTransform()`

```
plots_harv_utm <- spTransform(plots_harv, crs(chm_harv))
plot(plots_harv_utm, add=TRUE, pch=1, cex=2, lwd=2)
```

* Use `vector` to `extract()` values from `raster`

```
> extract(chm_harv, plots_harv_utm)
[1] 18.00000 15.94000 18.70999 19.45999 22.72000
```

* These are canopy heights from `chm_harv` at the coordinates from 
  `plots_harv_utm`. 
    * Order of values lines up with `plots_harv_utm$site_id`.

### `raster` in time series

* Values over time can be stored in
    * a single file with multiple bands (*or layers*,`stack`)
        * similar to `RGB` raster with multiple color bands
    * multiple coordinated files
* The assignment uses multiple coordinated files of NDVI
    * NDVI is a data product (*vegetation index*) stored in a `raster`
    * Works just like the files with 'raw' data

> Assign remainder of [Exercise 1 - Phenology from Space]({{ site.baseurl }}/exercises/Neon-phenology-from-space-R).
