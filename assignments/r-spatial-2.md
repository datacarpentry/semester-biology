---
layout: page
element: assignment
title: Spatial Data 2
language: R
exercises: ['Harvard Forest Soils Analysis', 'Cropping NEON Data']
points: [50, 50]
---

### Learning Objectives

> Following this assignment students should be able to:
>
> - Map polygon data based on properties
> - Aggregating raster data inside of polygons
> - Crop and mask spatial data
> - Save spatial data
> - Create vector data based on locations data in csv files

{% include reading.html %}

Place this code at the start of the assignment to load all the required packages.

```r
library(stars)
library(sf)
library(ggplot2)
library(dplyr)
```

{% include assignment.html %}
