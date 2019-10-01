---
layout: page
element: notes
title: Publication quality figures
language: R
---
 
> * Have students install `devtools` and `patchwork` (using `devtools`)
> * Open https://ggplot2.tidyverse.org/reference/ggtheme.html in browser

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
library(readr)

trees <- read_tsv("https://ndownloader.figshare.com/files/5629536")

ggplot(trees, aes(x = HEIGHT, y = CIRC)) +
  geom_point()

ggsave("acacia_size_scaling.png")
ggsave("acacia_size_scaling.svg")
ggsave("acacia_size_scaling.pdf")
```

* Show differences in zoom
* Some journals will require you to submit vector plots in a raster format
* You now know enough to cry a little inside when they do

### Resolution,  DPI, and Image Dimensions

* Images have dimensions of height and width

```r
ggsave("acacia_size_scaling.png", height = 7, width = 10)
```

* Resolution determines how many pixels occur per unit area within those dimensions
* DPI -> Dots per inch
* Journals typically request at least 300 DPI

```r
ggsave("acacia_size_scaling.png", dpi = 300)
ggsave("acacia_size_scaling.png", dpi = 30)
```

### Color palettes

* Choose colors that work well for everyone
  * People with different kinds of color blindness
  * People who printed your paper out without a color printer
* Need to be correctly interpreted
* Viridis is a new color scale that is designed to provide a good set of default
  colors for addressing all of these concerns

```r
ggplot(trees, aes(x = HEIGHT, y = CIRC, color = SPECIES)) +
  geom_point() +
  scale_color_viridis_d()
```

```r
ggplot(trees, aes(x = HEIGHT, y = CIRC, color = SPECIES)) +
  geom_point() +
  scale_color_viridis_d(option = "magma")
```

```r
ggplot(trees, aes(x = HEIGHT, y = CIRC, color = HEIGHT)) +
  geom_point() +
  scale_color_viridis_c(option = "magma")
```

### Themes

* Can customize every aspect of plots in `ggplot`
* Themes are an easy way to change the overall look of figures 
* These can be used to make coordinated changes to groups of options

```r
ggplot(trees, aes(x = HEIGHT, y = CIRC, color = SPECIES)) +
  geom_point() +
  scale_color_viridis_c() +
  theme_classic()
```

* Show theme examples at https://ggplot2.tidyverse.org/reference/ggtheme.html

### Saving and exporting multiple plots

* To save plots to work with later assign them to a variable

```r
species_scaling <- ggplot(trees, aes(x = HEIGHT, y = CIRC, color = SPECIES)) +
  geom_point() +
  scale_color_viridis_d()

species_scaling
ggsave("species_scaling.jpg", species_scaling)
```

### Combining multiple plots

* Often want to combine multiple distinct plots into a single figure
* Two popular packages for this, `patchwork` and `cowplot`

* `patchwork` is not on CRAN so install using `devtools`
* `devtools` lets us install packages from a variety of sources, including
  GitHub, one of the major hubs of software development

```r
install.packages('devtools')
library(devtools)
install_github('thomasp85/patchwork')
```

* `patchwork` works by "adding" plots to one another

```r
library(patchwork)

height_dist <- ggplot(trees, aes(x = HEIGHT, fill = SPECIES)) +
  geom_histogram() +
  scale_fill_viridis_d()

species_scaling + height_dist
```

* Can control the positioning of subplots

```r
species_scaling + height_dist +
  plot_layout(ncol = 1)
```

* The relative sizes of subplots

```r
species_scaling + height_dist +
  plot_layout(ncol = 1, heights = c(3, 1))
```

* And labeling

```r
species_scaling + height_dist +
  plot_layout(ncol = 1, heights = c(3, 1)) +
  plot_annotation(tag_levels = "A")
```

* Combined this can result in fairly complex figures for publication with a
  small amount of code

```r
height_dist <- height_dist +
  theme_void() +
  theme(legend.position='none')

height_dist + species_scaling + plot_layout(ncol = 1, heights = c(1, 5))
```