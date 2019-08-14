---
layout: page
element: notes
title: Remote Sensing Image Analysis
language: R
---

> Adapted from:
>
> http://rspatial.org/rs/index.html

* Remote sensing data is one of the most commonly used types of image data
* Work with Landsat data
* Images from a series of satellites starting in 1972
* Look at some data from California in 2017

```
download.file('https://biogeo.ucdavis.edu/data/rspatial/rsdata.zip', 'rsdata.zip')
unzip('rsdata.zip')
```

## Multi-band/frame images

* Landsat data has multiple bands (like frames in EBImage)
* Regular images which have 3 bands - Red, green, blue
* These bands each have different intensities
    * Like grayscale intensivities but for that color
* When combined they can produce many different colors

* Load the red, green, and blue bands for landsat (bands 2-4)

```
library(raster)
blue <- raster('rs/LC08_044034_20170614_B2.tif')
green <- raster('rs/LC08_044034_20170614_B3.tif')
red <- raster('rs/LC08_044034_20170614_B4.tif')
blue
```

* Each image has information on dimensions and intensity values like other images
* Also contains additional metadata related to the spatial aspects of the data

```
plot(red, col = rgb(seq(0, 1, 0.01), 0, 0))
plot(red, col = grey(seq(0, 1, 0.01)))

landsatRGB <- stack(red, green, blue)
plotRGB(landsatRGB, scale = 0.718)
plotRGB(landsatRGB, scale = 0.718, stretch = "lin")
```