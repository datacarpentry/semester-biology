---
layout: page
element: notes
title: Nicer Maps
language: R
---

- We can cleanup our maps using theming
- And add additional information using the `ggspatial` package
- Set the extents for our map
- Limit it to the extents of our DTM

```r
extents <- ext(harv_boundary)
ggplot() +
  geom_spatraster(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, fill = "transparent") +
  coord_sf(xlim = c(extents$xmin, extents$xmax), ylim = c(extents$ymin, extents$ymax))
```

- Now get rid of the grey background using `theme_bw()`

```r
extents <- ext(harv_boundary)
ggplot() +
  geom_spatraster(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, fill = "transparent") +
  coord_sf(xlim = c(extents$xmin, extents$xmax), ylim = c(extents$ymin, extents$ymax)) +
  theme_bw()
```

- Make our boundary clearer with `linewidth` and `color`

```r
extents <- ext(harv_boundary)
ggplot() +
  geom_spatraster(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, fill = "transparent", linewidth = 1, color = "black") +
  coord_sf(xlim = c(extents$xmin, extents$xmax), ylim = c(extents$ymin, extents$ymax)) +
  theme_bw()
```

- Rotate our x-axis labels

```r
extents <- ext(harv_boundary)
ggplot() +
  geom_spatraster(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, fill = "transparent", linewidth = 1, color = "black") +
  coord_sf(xlim = c(extents$xmin, extents$xmax), ylim = c(extents$ymin, extents$ymax)) +
  theme_bw() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))
```

- Now use `ggspatial` to add north arrow

```r
install.packages("ggspatial")
```

```r
extents <- ext(harv_boundary)
ggplot() +
  geom_spatraster(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, fill = "transparent", linewidth = 1, color = "black") +
  coord_sf(xlim = c(extents$xmin, extents$xmax), ylim = c(extents$ymin, extents$ymax)) +
  annotation_north_arrow(location = "tl") +
  theme_bw() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))
```

- And a scale bar

```r
extents <- ext(harv_boundary)
ggplot() +
  geom_spatraster(data = harv_dtm_cropped) +
  scale_fill_viridis_c(na.value = "transparent") +
  geom_sf(data = harv_boundary, fill = "transparent", linewidth = 1, color = "black") +
  coord_sf(xlim = c(extents$xmin, extents$xmax), ylim = c(extents$ymin, extents$ymax)) +
  annotation_north_arrow(location = "tl") +
  annotation_scale(location = "br", width_hint = 0.5) +
  theme_bw() +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))
```
