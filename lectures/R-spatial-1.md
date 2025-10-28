---
layout: page
element: lecture
title: Spatial Data 1
language: R
---

## Setup

```r
install.packages(c("dplyr", "ggplot2", "sf", "terra", "tidyterra"))
download.file("www.datacarpentry.org/semester-biology/data/neon-geospatial-data.zip", "neon-geospatial-data.zip", mode = "wb")
unzip("neon-geospatial-data.zip")
file.rename("neon-geospatial-data/", "data/")
```

## Lectures

* [Spatial Data Raster]({{ site.baseurl }}/materials/spatial-data-raster-R)
* [Spatial Data Raster Math]({{ site.baseurl }}/materials/spatial-data-raster-math-R)
* [Spatial Data Vector]({{ site.baseurl }}/materials/spatial-data-vector-R)
* [Spatial Data Projections]({{ site.baseurl }}/materials/spatial-data-projections-R)
* [Spatial Data Extracting Raster Values]({{ site.baseurl }}/materials/spatial-data-extracting-raster-values-R)
