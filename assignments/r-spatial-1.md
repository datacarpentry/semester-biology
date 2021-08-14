---
layout: page
element: assignment
title: Spatial Data 1
language: R
exercises: ['Canopy Height from Space']
points: [100]
---

### Learning Objectives

> Following this assignment students should be able to:
>
> - import, view properties, and plot a `raster` 
> - perform simple `raster` math
> - import, view properties, and plot vector data
> - extract points from a `raster` using a shapefile

{% include reading.html %}

Place this code at the start of the assignment to load all the required packages.

```r
library(stars)
library(sf)
library(ggplot2)
library(dplyr)
```

{% include assignment.html %}
