---
layout: page
element: assignment
title: Spatial Data 2
language: R
exercises: ['Harvard Forest Soils Analysis', 'Cropping NEON Data', 'Check That Your Code Runs']
points: [45, 45, 10]
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
library(dplyr)
library(ggplot2)
library(sf)
library(terra)
library(tidyterra)
```

{% include assignment.html %}
