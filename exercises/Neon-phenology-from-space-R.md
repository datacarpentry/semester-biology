---
layout: exercise
topic: NEON
title: Phenology from Space
language: R
---

The [National Ecological Observatory Network](http://www.neoninc.org) has invested in [high-resolution airborne imaging](http://www.neonscience.org/data-resources/get-data/airborne-data) of their field sites. 
Elevation models generated from [LiDAR](http://neondataskills.org/self-paced-tutorial/1_About-LiDAR-Data-Light-Detection-and-Ranging_Activity1/) can be used to map the topography and vegetation at the sites. 
These high-resolution images can then be integrated with satellite imagery that is gathered more frequently. 

This data gets really powerful when you can compare ecological processes across sites. One common ecological process that can be observed from space is vegetation structure and phenology, or seasonal patterns, of plants.

[Download the data]({{ site.baseurl }}/data/Neon-phenology-from-space.zip).

1. Generate a 'Canopy Height Model' for each site (`HARV` and `SJER`).

### Lesson Plan
- Generate `canopy_height` model for two sites with varying vegetation structure
    - `canopy_height = surface_elevation - terrain_elevation` 
    - Similar task to http://neondataskills.org/R/Raster-Calculations-In-R/
- Identify plots at each site
    - Use `points` or `polygons` from vector
    - Similar task to  http://neondataskills.org/R/crop-extract-raster-data-R/
- Visualize seasonal changes (*phenology*) in vegetation structure
    - Use multiple rasters (*time series*) for each site
    - `NDVI` or comparable metric for vegetation structure
    - May require reprojection to line up `NDVI` with `canopy_height` 
- Compare vegetation structure (`canopy_height`) for site to seasonal phenology (`NDVI`)
    - forested plot has a gradual seasonal shift in phenology
    - grassland plot has pulsed or less 'green' shift in phenology 
 