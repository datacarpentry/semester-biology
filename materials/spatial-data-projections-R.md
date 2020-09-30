---
layout: page
element: notes
title: Spatial Data Vector
language: R
--- 

> Remember to download and put into data subdirectory:
>
> * [LiDAR rasters and plot locations]({{ site.baseurl }}/data/NEON-airborne.zip)

> Load the following into browser window:

> * [Projections picture](https://media.opennews.org/cache/06/37/0637aa2541b31f526ad44f7cb2db7b6c.jpg)

> Set-up R Console:

```
library(ggplot2)
```

### Import and reproject shapefiles

```
library(rgdal)

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

> Do Task 3 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).
