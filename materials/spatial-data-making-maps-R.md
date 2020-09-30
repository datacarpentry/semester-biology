---
layout: page
element: notes
title: Spatial Data Making Maps
language: R
--- 

### Map of point data

* Maps are available in the `maps` package
* Maps are typically vector data
  
```
library(maps)
us_map = map_data("usa")
```

* *Open `map`*
* Polygons, but already stored as data frames (already done as.data.frame)
* Coordinates + Group + Order
* Group identifies unique polygons
* Order identifies how the points in each polygon are connected
* *Draw a polygon illustrating points, edges, & order*

```r
ggplot() +
  geom_polygon(data = us_map, 
               aes(x = long, y = lat, group = group), 
               fill = "grey")
```

* `coord_quickmap` gives us a reasonable projection

```r
ggplot() +
  geom_polygon(data = us_map, 
               aes(x = long, y = lat, group = group), 
               fill = "grey") +
  coord_quickmap()
```

* Add other data on top
* Data on species occurances using the `spocc` package
* Gets data from multiple sources include GBIF

```
library(spocc)

do_gbif = occ(query = "Dipodomys ordii", 
              from = "gbif", 
              limit = 1000, 
              has_coords = TRUE)
do_data = data.frame(dipo_df$gbif$data)
```

```r
ggplot() +
  geom_polygon(data = us_map, 
               aes(x = long, y = lat, group = group), 
               fill = "grey") +
  geom_point(data = do_data, 
             aes(x = Dipodomys_ordii.longitude,
                 y = Dipodomys_ordii.latitude)) +
  coord_quickmap()
```

> Do [Species Occurrences Map]({{ site.baseurl }}/exercises/Spatial-data-map-R).
