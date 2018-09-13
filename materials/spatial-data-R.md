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

> * [Projections picture](https://media.opennews.org/cache/06/37/0637aa2541b31f526ad44f7cb2db7b6c.jpg)
> * [Canopy Height Model picture](https://datacarpentry.org/r-raster-vector-geospatial/images/dc-spatial-raster/lidarTree-height.png)

> Set-up R Console:

```
library(raster)
library(rgdal)
library(ggplot2)
```

### `raster` structure, import, and plotting

* Spatial data is often organized in a `raster`.
    * gridded format (*like coordinates*)
    * each pixel is a value
	* most remote sensing and environmental data
* `raster()` import

* DSM is Digital Surface Model: elevation of top physical point
* See diagram
* Later use with Digital Terrain Model (elevation of ground) to create Canopy Height Model

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
    * Change to dataframe for `ggplot`
    * `coord_quickmap()` sets projection

```
dsm_harv_df = as.data.frame(dsm_harv, xy = TRUE)
head(dsm_harv_df)

ggplot() +
  geom_raster(data = dsm_harv_df, 
              aes(x = x, y = y, fill = HARV_dsmCrop)) +
  coord_quickmap()

```

* Looking at raster values

```
ggplot() +
  geom_histogram(data = dsm_harv_df, 
                 aes(x = HARV_dsmCrop))

```

### `raster` math

* Create Canopy Height Model

```
dtm_harv <- raster("data/NEON-airborne/HARV_dtmCrop.tif")
chm_harv <- dsm_harv - dtm_harv
```

> Do Tasks 1-2 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).


### Import and reproject shapefiles

* `vector` data
    * `csv`
    * `shapefile`
        * set of multiple files
            * same name, different extensions
        * `readOGR("directory", "file_name_without_extensions")`
            * stores data in a single `data.frame`
            * access 'attributes' similar to GIS software using `$`
                * `file_name$site_id`

```
plots_harv <- readOGR("data/NEON-airborne/plot_locations", 
                      "HARV_plots")
```

* Plot `vector` on top of `raster`

```
chm_harv_df = as.data.frame(chm_harv, xy = TRUE)
plots_harv_df = as.data.frame(plots_harv)
```

```
ggplot() +
  geom_raster(data = chm_harv_df, 
              aes(x = x, y = y, fill = layer)) +
  geom_point(data = plots_harv_df, 
             aes(x = coords.x1, y = coords.x2), color = "yellow")
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
plots_harv_utm_df = as.data.frame(plots_harv_utm)
```

```
ggplot() +
  geom_raster(data = chm_harv_df, 
              aes(x = x, y = y, fill = layer)) +
  geom_point(data = plots_harv_utm_df, 
             aes(x = coords.x1, y = coords.x2), color = "yellow")
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

* Plot one layer

```
ndvi_rasters_df = as.data.frame(ndvi_rasters, xy = TRUE)
ggplot() +
  geom_raster(data = ndvi_rasters_df, 
              aes(x = x, y = y, alpha = HARV_NDVI_2015353)) +
  coord_quickmap()
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
str(points_spat)
```

```
points_spat_df = as.data.frame(points_spat)
ggplot() +
  geom_point(data = points_spat_df, 
             aes(x = long, y = lat))
```

> Do [Species Occurrences Elevation Histogram]({{ site.baseurl }}/exercises/Spatial-data-elevation-histogram-R).


### Map of point data

* `ggplot` generates maps using `maps` package

```
map = map_data("state", region = "massachusetts")
ggplot() +
  geom_polygon(data = map, 
               aes(x = long, y = lat, group = group), 
               fill = "grey")
```

* Add spatial data on top

```
ggplot() +
  geom_polygon(data = map, 
               aes(x = long, y = lat, group = group), 
               fill = "grey") +
  geom_point(data = points_spat_df, 
             aes(x = long, y = lat))
```
