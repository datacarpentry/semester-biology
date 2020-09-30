---
layout: page
element: notes
title: Spatial Data Extracting Raster Values
language: R
--- 

### Extract raster data

* Use `vector` to `extract()` values from `raster`
* These are canopy heights from `chm_harv` at the coordinates from 
  `plots_harv_utm`. 

```
plots_chm <- extract(chm_harv, plots_harv_utm)
```

* Order of values lines up with `plots_harv_utm$plot_id`.

```
plots_harv_utm$plot_id
plots_chm <- data.frame(plot_num = plots_harv_utm$plot_id, plot_value = plots_chm)
```

* Often want values surrounding a point, not just the single pixel that the
  point lands in
* Do this using `buffer` to get the values for all pixels within some buffer
  distance from the point

```
extract(chm_harv, plots_harv_utm, buffer = 10)
```

* This returns one value for each pixel within the buffer region
* Also what output is like for line and polygon data
* One value for each cell intersected by a line or each cell inside a polygon

* Could keep all of this data, or calculate a value from it
* Often want an average

```
extract(chm_harv, plots_harv_utm, buffer = 10, fun = mean)
```

> Do Tasks 4-5 of [Canopy Height from Space]({{ site.baseurl }}/exercises/Neon-canopy-height-from-space-R).