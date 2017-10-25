---
layout: page
element: notes
title: Spatial Data Introduction
language: R
--- 

> Remember to download and put into data subdirectory:
>
> * [LiDAR rasters and plot locations]({{ site.baseurl }}/data/NEON-airborne.zip)
> * [Harvard Forest NDVI]({{ site.baseurl }}/data/HARV-NDVI.zip) 
> * [San Joaquin Experimental Range NDVI]({{ site.baseurl }}/data/SJER-NDVI.zip)

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
dsm_harv <- raster("data/NEON-airborne/HARV_dsmCrop.tif")
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
dtm_harv <- raster("data/NEON-airborne/HARV_dtmCrop.tif")
chm_harv <- dsm_harv - dtm_harv
```

> Do Tasks 1-2 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).


### Import and reproject shapefiles

* `vector` data can be added to `rasters` to provide reference information
    * `csv`
    * `shapefile`
        * set of multiple files
            * same name, different extensions
        * `readOGR("directory", "file_name_without_extensions")`
            * stores data in a single `data.frame`
            * access 'attributes' similar to GIS software using `$`
                * `file_name$site_id`

```
plots_harv <- readOGR("data/NEON-airborne/plot_locations", "HARV_plots")
plot(chm_harv)
plot(plots_harv, add = TRUE, pch = 4, cex = 1.5)
```

* Uh oh, nothing happened.

* Coordinate Reference System (*`crs` or `projection`*) is different from `raster`.

```
crs(chm_harv)
crs(plots_harv)
```

* Change projection: 
    * reproject `raster` with `projectRaster()`
    * reproject `vector` with `spTransform()`

```
plots_harv_utm <- spTransform(plots_harv, crs(chm_harv))
plot(plots_harv_utm, add = TRUE, pch = 4, cex = 1.5)
```

### Extract raster data

* Use `vector` to `extract()` values from `raster`
* These are canopy heights from `chm_harv` at the coordinates from 
  `plots_harv_utm`. 

```
plots_chm <- extract(chm_harv, plots_harv_utm)
```

* Order of values lines up with `plots_harv_utm$plot_id`.

```
plots_harv_utm$plot_id
plots_chm <- data.frame(plot_num = plots_harv_utm$plot_id, plot_value = plots_chm)
```

* To get an average of the values in a nearby region use `buffer`

```
plots_chm$plot_buffer_value <- extract(chm_harv, plots_harv_utm, buffer = 10, fun = mean)
```

> Do Tasks 3-4 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).


### Stacks of rasters

* Sets of rasters in the same location often analyzed together
* `Raster stack`
* Can be stored in one or multiple files
* To load all layers use `stack()` on a single multi-band file or multiple files
* We'll load a time-series of NDVI data from Harvard Forest into a raster stack
    * NDVI is a remotely sensed vegetation index that measures greenness
	* Provides information on plant phenology and productivity

```
ndvi_files = list.files("data/HARV_NDVI/",
                         full.names = TRUE,
                         pattern = "HARV_NDVI.*.tif")
ndvi_rasters <- stack(ndvi_files)
```

* Can visualize up to 16 layers using `plot()`

```
plot(ndvi_rasters)
plot(ndvi_rasters, c(1, 3, 5, 7, 9, 11))
```

* Calculate values across each raster using `cellStats()`

```
avg_ndvi <- cellStats(ndvi_rasters, mean)
```

* Store in data frame

```
avg_ndvi_df <- data.frame(samp_period = 1:length(avg_ndvi), ndvi = avg_ndvi)
```

* Get row names into column

```
library(dplyr)
avg_ndvi_df <- tibble::rownames_to_column(avg_ndvi_df, var = "name")
```

> Do [Phenology from Space]({{ site.baseurl }}/exercises/Neon-phenology-from-space-R).


### Making your own point data

* Make spatial data from `csv` file with latitudes and longitudes
* Do to combine with other spatial data
* Need to know the `proj4string` for standard latitude/longitude data
* `"+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0"`

```
points_csv <- read.csv("data/NEON-airborne/plot_locations/HARV_PlotLocations.csv")
points_crs <- crs("+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0")
points_spat <- SpatialPointsDataFrame(
	points_csv[c('long', 'lat')], 
	points_csv, 
	proj4string = points_crs)
```

```
str(points_spat)
plot(points_spat)
```

> Do [Species Occurrences Elevation Histogram]({{ site.baseurl }}/exercises/Spatial-data-elevation-histogram-R).


### Map of point data

* Can plot points on Google Map segment with `ggmap` package

```
library(ggmap)
```

* Uses only dataframes, not spatial data
* Generate map segment with csv coordinates

```
avg_long = mean(points_csv$long)
avg_lat = mean(points_csv$lat)
map = get_map(location = c(lon = avg_long, lat = avg_lat), zoom = 14)
```

* Plot original csv points

```
ggmap(map) +
    geom_point(data = points_csv, aes(x = long, y = lat))
```
