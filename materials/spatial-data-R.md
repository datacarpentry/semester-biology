---
layout: page
element: notes
title: Spatial Data Introduction
language: R
--- 

> Remember to download and set-up directory:
>
> * [LiDAR rasters and plots]({{ site.baseurl }}/data/NEON-airborne.zip)
> * [`HARV_NDVI`]({{ site.baseurl }}/data/HARV-NDVI.zip) 
> * [`SJER_NDVI`]({{ site.baseurl }}/data/SJER-NDVI.zip)

> Load the following into browser window:

> * Projections figure from http://neondataskills.org/R/Introduction-to-Raster-Data-In-R/
> * Canopy Height Model figure from http://neondataskills.org/R/Raster-Calculations-In-R/

> Set-up R Console:

```
library(raster)
library(rgdal)
```

### `raster` structure, import, and plotting

* Spatial data is often organized in a `raster`.
    * gridded format (*like coordinates*)
    * each pixel is a value
	* most remote sensing and environmental data

* `raster()` import

```
dsm_harv <- raster("HARV_dsmCrop.tif")
dsm_harv
```

* Metadata is important to describe the context of spatial data.
    * `bands`
    * `projection`
    * `units`
    * `min`, `max`, `mean`

* `dsm_harv` is a `RasterLayerObject` and we can get individual pieces of it's
   metadata using appropriate functions

```
nbands(dsm_harv)
crs(dsm_harv)
```

* Plotting
    * package modifies R basic `graphics`

```
plot(dsm_harv)
```

* Looking at raster values

```
hist(dsm_harv)
```

### `raster` math

* The DSM data is a Digital Surface Model: elevation of top physical point
* DTM is Digital Terrain Model: elevation of the ground
* We can create a Canopy Height Model (CHM) by taking the difference between them

```
dtm_harv <- raster("HARV_dtmCrop.tif")
chm_harv <- dsm_harv - dtm_harv
```

> Do Tasks 1-2 from [Exercise 1 - Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).


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
plots_harv
```

* Coordinate Reference System (*`crs` or 'projection'*) is different from `raster`.
    * reproject `raster` with `projectraster()`
    * reproject `vector` with `spTransform()`

```
plots_harv_utm <- spTransform(plots_harv, crs(chm_harv))
plot(plots_harv_utm, add=TRUE, pch=1, cex=2, lwd=2)
```

### Extract raster data

* Use `vector` to `extract()` values from `raster`

```
extract(chm_harv, plots_harv_utm)
```

* These are canopy heights from `chm_harv` at the coordinates from 
  `plots_harv_utm`. 
    * Order of values lines up with `plots_harv_utm$site_id`.

* To get an average of the values in a nearby region use `buffer`


```
extract(chm_harv, plots_harv_utm, buffer = 10, fun = mean)
```

> Assign remainder of [Exercise 1 - Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).


### Making your own point data

* Make spatial data from `csv` file with latitudes and longitudes
* Need to know the `proj4string` for standard latitude/longitude data
* `"+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0"`

```
plot_latlong_data <- read.csv("data/NEON-airborne/plot_locations/HARV_PlotLocations.csv")
plot_latlong_data
crs_longlat <- crs("+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0")
plot_latlong_data_spat <- SpatialPointsDataFrame(plot_latlong_data[c('long', 'lat')],
                                                    plot_latlong_data,
                                                    proj4string = crs_longlat)
str(plot_latlong_data_spat)
plot(plot_latlong_data_spatial)
```


### `raster` in time series

* Values over time can be stored in
    * a single file with multiple bands (*or layers*,`stack`)
        * similar to `RGB` raster with multiple color bands
    * multiple coordinated files
* The assignment uses multiple coordinated files of NDVI
    * NDVI is a data product (*vegetation index*) stored in a `raster`
    * Works just like the files with 'raw' data

> [Exercise 2 - Phenology from Space]({{ site.baseurl }}/exercises/Neon-phenology-from-space-R).
