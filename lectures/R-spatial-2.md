---
layout: page
element: lecture
title: Spatial Data 2
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

* [Mapping polygon data based on properties]({{ site.baseurl }}/materials/spatial-data-polygon-properties-R)
* [Aggregating raster data inside polygons]({{ site.baseurl }}/materials/spatial-data-polygon-aggregation-R)
* [Why is ggplot plotting my UTM data as latitudes and longitudes and how do I make it stop]({{ site.baseurl }}/materials/spatial-data-plot-projections-R)
* [Creating vector data from csv]({{ site.baseurl }}/materials/spatial-data-create-vector-data-R)
* [Cropping and Masking Spatial Data]({{ site.baseurl }}/materials/spatial-data-cropping-R)
* [Saving Spatial Data From R]({{ site.baseurl }}/materials/spatial-data-saving-R)
* [Making nicer maps]({{ site.baseurl }}/materials/spatial-nicer-maps-R)
