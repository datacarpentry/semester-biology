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

```r
library(ggplot2)
```

### Introduction to Vector Data

* `vector` data includes points, lines, and polygons
* `shapefiles` are one main format
* set of multiple files with the same name, but different extensions

* Work with vector data using the `sf` package
* We can read this data into R using `st_read`
* Let's load in some data on some field plots at that Harvard Forest NEON site we've been working with

```r
library(sf)
plots_harv <- st_read("plot_locations/HARV_plots.shp")
```

* When read read the data in we see information about it including
* The data has 5 features
* Each feature is one object, either a point, a line, or a polygon
* The geometry type is "POINT", which means that the features are points
* The data has 2 fields
* Each field is a piece of information that is associated with each feature
* And there is information on the minimum and maximum spatial values in the dataset
* If we view this object we'll see that it is a data frame with one row per vector object
* There are three columns
* The first two are the fields: id and plot_id, which in this case are both numerical plot IDs
* The last field is where the spatial information is stored and which is called `geometry`
* Since this is point data each object is stored as a pair of x and y coordinates
* This makes it a special kind of data frame that can be used by spatial tools

* We can plot this data using a special geom, `geom_sf`

```r
ggplot() +
  geom_sf(data = plots_harv)
```

* We can also color vector data based on the values in the fields (or columns)
* For example, our plots have two different types, "Tower" and "Distributed"
* These are stored in the `plot_type` field
* To color the points based on `plot_type` we add a mapping

```r
ggplot() +
  geom_sf(data = plots_harv, mapping = aes(color = plot_type))
```

* Just like in scatter plots this mapping tells ggplot to "color the points based on `plot_type"


### Combining multiple spatial layers

* We have the start This shows us the position of the plots, but it's hard to learn much from this without some context
* So let's load another vector object that shows the boundary of the research site

```r
boundary_harv <- st_read("plot_locations/HARV_boundary.shp")
```

* We can plot them together by adding two `geom_sf` layers in `ggplot`

```r
ggplot() +
  geom_sf(data = boundary_harv) +
  geom_sf(data = plots_harv)
```

* The order of layers is important because they will plot on top of one another
* So if we'd plotted the plots first...


```r
ggplot() +
  geom_sf(data = plots_harv) +
  geom_sf(data = boundary_harv)
```

* We wouldn't have been able to see them.
* If we need to see through layers we can do this by setting the transparency using `alpha`


```r
ggplot() +
  geom_sf(data = plots_harv) +
  geom_sf(data = boundary_harv, alpha = 0.5)
```
