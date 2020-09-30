---
layout: page
element: notes
title: Spatial Data Create Vector Data
language: R
--- 

### Making your own vector data

* Make spatial data from from non-spatial data with latitudes and longitudes
* Do to combine with other spatial data
* Need to know the `proj4string` for standard latitude/longitude data
* `"+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0"`

```
points_crs <- crs("+proj=longlat +datum=WGS84 +ellps=WGS84 +towgs84=0,0,0")
do_data_spat <- SpatialPointsDataFrame(
	do_data[c('Dipodomys_ordii.longitude', 'Dipodomys_ordii.latitude')], 
	do_data, 
	proj4string = points_crs)
str(do_data_spat)
```

* `do_data` was a regular data frame, so do the same thing with your down data
  after loading it using `read.csv`
* Now you can do things like reproject and `extract` values from rasters 

> Do [Species Occurrences Elevation Histogram]({{ site.baseurl }}/exercises/Spatial-data-elevation-histogram-R)