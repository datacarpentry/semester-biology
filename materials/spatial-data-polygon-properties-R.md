---
layout: page
element: notes
title: Mapping polygon data based on properties
language: R
--- 

* A common type of vector data is data with multiple polygons that each have associated properties
* For Harvard Forest we have a map of soil types at the site
* Let's load it and map it using the `sf` package

```r
library(sf)

harv_soils <- st_read("data/HARV/harv_soils.shp")

ggplot() +
  geom_sf(data = harv_soils)
```

* We can see that we get a map with multiple polygons
* If we look at the `harv_soils` object we'll see that it's a simple feature object with the geometry being `POLYGON`

```r
harv_soils
```

* Each feature is a single polygon with 5 associated fields: soil type, notes, two different soil type descriptions, and how well drained the soil is
* We can include this information on our maps in the same ways we include it in other `ggplot` maps and graphs
* Let's start by coloring each polygon by it's soil type
* We do this by setting the `mapping` to have `fill = TYPE_`

```r
ggplot() +
  geom_sf(data = harv_soils, mapping = aes(fill = TYPE_))
```

* We can switch the color scheme to viridis like we did for raster data, but using the `_d` for discrete

```r
ggplot() +
  geom_sf(data = harv_soils, mapping = aes(fill = TYPE_)) +
  scale_fill_viridis_d()
```

* We can also plot different soil types on different subplots to help us focus on where individual soil types occur
* We do this using `facet_wrap` just like we did for plotting tabular data

```r
ggplot() +
  geom_sf(data = harv_soils) +
  facet_wrap(~TYPE_)
```