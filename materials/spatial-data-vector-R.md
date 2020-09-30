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

> * [Vector Description]

> Set-up R Console:

```
library(raster)
library(ggplot2)
```

* `vector` data includes points, lines, and polygons
* `shapefiles` are one main format
    * set of multiple files
        * same name, different extensions
    * `readOGR("directory", "file_name_without_extensions")`
        * stores data in a single `data.frame`
        * access 'attributes' similar to GIS software using `$`
            * `file_name$site_id`

```
library(rgdal)

plots_harv <- readOGR("data/NEON-airborne/plot_locations", 
                      "HARV_plots")
```
