---
layout: page
element: notes
title: Publication quality figures
language: R
---
 
> Have students install `devtools` and `patchwork` (using `devtools`)

### File formats

* Raster vs vector (just like in spatial data)
* Raster
  * Right choice for photos (or rasters)
  * Made of pixels, so gets grainy
  * JPEG, GIF, PNG, TIFF
  * PNG is a good compromise format
* Vector
  * Right choice for plots, line drawings
  * Provides infinite scaling
    * EPS, AI, PDF, SVG

* Save in different file formats using different extensions

```r
library(ggplot2)
library(raster)

dtm_harv <- raster("data/neon-airborne/harv_dtmcrop.tif")
dtm_harv_cropped <- crop(dtm_harv, extent(dtm_harv, 731500, 732000, 4713200, 4713500))
dtm_harv_df = as.data.frame(dtm_harv_cropped, xy = TRUE)

ggplot(dtm_harv_df, aes(x = HARV_dtmCrop)) +
  geom_histogram()

ggsave("elev_hist.png")
ggsave("elev_hist.svg")
ggsave("elev_hist.pdf")
```

* Show differences in zoom
* Some journals will require you to submit vector plots in a raster format
* You now know enough to cry a little inside when they do

### Resolution,  DPI, and Image Dimensions

* Images have dimensions, their height and width

```r
ggsave("elev_hist.png", height = 7, width = 10)
```

* Resolution determines how many pixes occur per unit area within those dimensions
* DPI -> Dots per inch
* Journals typically request at least 300 DPI

```r
ggsave("elev_hist.png", dpi = 300)
ggsave("elev_hist.png", dpi = 30)
```

### Color palettes

* When choosing colors to use in images we need to think about more than what
  looks good to you
* How will your plots look to other people
  * People with different kinds of color blindness
  * People who printed your paper out without a color printer
* Need to be correctly interpreted
* Viridis is a new color scale that is designed to provide a good set of default
  colors for addressing all of these concerns

```r
ggplot() +
  geom_raster(data = dtm_harv_df, mapping = aes(x = x, y = y, fill = HARV_dtmCrop)) +
  scale_fill_viridis_c()
```

```r
ggplot() +
  geom_raster(data = dtm_harv_df, mapping = aes(x = x, y = y, fill = HARV_dtmCrop)) +
  scale_fill_viridis_c(options = "magma")
```

### Saving and exporting multiple plots


### Themes

* These can be used to make coordinated changes to groups of options

```
p1 + theme_classic()
```

### Combining multiple plots

* Bivariate plot + histogram example

```
```

* Map + picture + plot example

```
elevation_map = ggplot() +
  geom_raster(data = dsm_harv_df, 
              aes(x = x, y = y, fill = HARV_dsmCrop))
elevation_histogram = ggplot() +
  geom_histogram(data = dsm_harv_df, 
                 aes(x = HARV_dsmCrop))
```

* Mention `cowplot`