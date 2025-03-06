---
layout: page
element: notes
title: Publication quality figures
language: R
---

> * Have students install `ggplot2`, `readr`, `patchwork`
> * Download the data file from <https://datacarpentry.org/semester-biology/data/TREE_SURVEYS.txt>
> * `download.file("https://datacarpentry.org/semester-biology/data/TREE_SURVEYS.txt", "TREE_SURVEYS.txt")`
> * Open https://ggplot2.tidyverse.org/reference/ggtheme.html in browser

### File formats

* Raster vs vector (just like in spatial data)
* Raster
  * Right choice for photos (or rasters)
  * Made of pixels, so gets grainy
  * JPEG, GIF, PNG, TIFF
  * PNG is a good compromise format

```r
library(ggplot2)
library(readr)

trees <- read_tsv("TREE_SURVEYS.txt")

ggplot(trees, aes(x = HEIGHT, y = CIRC)) +
  geom_point()

ggsave("acacia_size_scaling.png")
```

* Show pixelation zoom

* Vector
  * Right choice for plots, line drawings
  * Describes the objects that make up the image, including their shapes, colors, and positions
  * Provides infinite scaling
    * EPS (printers), AI, PDF, SVG (web)

* Save in different file formats using different extensions

```r
ggsave("acacia_size_scaling.eps")
ggsave("acacia_size_scaling.svg")
```

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

* When submitting to a journal first think about how large the image will be
* Then set the dpi to at least the journal's minimum resolution

### Color palettes

* Choose colors that work well for everyone
  * People with different kinds of color vision
  * People who printed your paper out without a color printer
* Need to be correctly interpreted
* Viridis is a new(ish) color scale that is designed to provide a good set of default
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

### Themes

* Can customize every aspect of plots in `ggplot`
* Themes are an easy way to change the overall look of figures
* These can be used to make coordinated changes to groups of options

```r
ggplot(trees, aes(x = HEIGHT, y = CIRC, color = SPECIES)) +
  geom_point() +
  scale_color_viridis_d() +
  theme_classic()
```

* Show theme examples at https://ggplot2.tidyverse.org/reference/ggtheme.html

* Themes have a small number of options for jointly controlling the size of things in the plot

```r
ggplot(trees, aes(x = HEIGHT, y = CIRC, color = SPECIES)) +
  geom_point() +
  scale_color_viridis_d() +
  theme_classic(base_size = 16)
```

* If you want to make additional changes use `theme()`

```r
ggplot(trees, aes(x = HEIGHT, y = CIRC, color = SPECIES)) +
  geom_point() +
  scale_color_viridis_c() +
  theme_classic(base_size = 16) +
  theme(legend.position = "top")
```

* Show large number of autocomplete options for `theme()`

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

```r
height_dist + species_scaling +
  plot_layout(ncol = 1)
```

* The relative sizes of subplots

```r
height_dist + species_scaling +
  plot_layout(ncol = 1, heights = c(1, 3))
```

* And labeling

```r
height_dist + species_scaling +
  plot_layout(ncol = 1, heights = c(1, 3)) +
  plot_annotation(tag_levels = "A")
```

* Combined this can result in fairly complex figures for publication with a
  small amount of code

```r
height_dist <- height_dist +
  theme_void() +
  theme(legend.position='none')

height_dist + species_scaling +
  plot_layout(ncol = 1, heights = c(1, 5))
```

### Reusing custom plots

* Once you've created a plot you might want to reuse the same basic plotting code
* The most common way folks do this is to copy and paste the code and change the pieces they want to change
* A better way is using functions
* Let's start with just the first piece of our graph

```r
make_plot <- function(data, xcolumn, ycolumn, colorcolumn) {
  species_scaling <- ggplot(data, aes(x = xcolumn, y = ycolumn, color = colorcolumn)) +
    geom_point() +
    scale_color_viridis_d()
}

plot_circ <- make_plot(trees, HEIGHT, CIRC, SPECIES)
plot_circ
```

* This doesn't work, but why?
* There is an extra step we need to take when working with tidyverse functions that work with "data variables", i.e., names of columns that are not in quotes
* These functions use tidy evaluation, a special type of non-standard evaluation
* This basically means they do fancy things under the surface to make them easier to work with
* But it means they don't work if we just pass things to functions in the most natural way
* To fix this we have to tell our code which inputs/arguments are this special type of data variable
* We do this by "embracing" them in double braces

```r
make_plot <- function(data, xcolumn, ycolumn, colorcolumn) {
  {% raw %}scaling <- ggplot(data, aes(x = {{ xcolumn }}, y = {{ ycolumn }}, color = {{ colorcolumn }})) +{% endraw %}
    geom_point() +
    scale_color_viridis_d()
}

plot_circ <- make_plot(trees, HEIGHT, CIRC, SPECIES)
plot_circ
```

* Now let's add the rest of our plot

```r
make_plot <- function(data, xcolumn, ycolumn, colorcolumn) {
{% raw %}scaling <- ggplot(data, aes(x = {{ xcolumn }}, y = {{ ycolumn }}, color = {{ colorcolumn }})) +{% endraw %}
  geom_point() +
  scale_color_viridis_d()

{% raw %}distribution <- ggplot(data, aes(x = {{ xcolumn }}, fill = {{ colorcolumn }})) +{% endraw %}
    geom_histogram() +
    scale_fill_viridis_d() +
    theme_void() +
    theme(legend.position='none')

  distribution + scaling + plot_layout(ncol = 1, heights = c(1, 5))
}

plot_circ <- make_plot(trees, HEIGHT, CIRC, SPECIES)
plot_circ
```

* Having done this we can now plot whatever we want

```r
plot_axis1 <- make_plot(trees, HEIGHT, AXIS_1, SPECIES)
plot_axis1
```

```r
plot_axis1_year <- make_plot(trees, HEIGHT, AXIS_1, as.factor(YEAR))
plot_axis1_year
```

```r
plot_axis1_axis2_year <- make_plot(trees, AXIS_1, AXIS_2, as.factor(YEAR))
plot_axis1_axis2_year
```
