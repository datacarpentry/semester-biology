---
layout: page
element: notes
title: Image Processing and Analysis
language: R
---

> Adapted from:
> https://www.bioconductor.org/packages/release/bioc/vignettes/EBImage/inst/doc/EBImage-introduction.html

> On Ubuntu install requires
> `sudo apt install r-cran-fftwtools`
> from marutter's ppa

```
install.packages("BiocManager")
BiocManager::install("EBImage")
```

```
library(EBImage)
```

## Reading

* Let's look at some microscope images of cells

```
nuclei_file <- system.file("images", "nuclei.tif", package="EBImage")
nuclei_img <- readImage(nuclei_file)
nuclei_img
```

* Image object includes information on
* Color mode - Gray scale
* Dimensions - 510 x 510 pixels
* Frame is like a layer in spatial data
    * Can be frames in a movie, different images, or different color bands
    * If this was a single color image would have
        * `frames.total = 3` for red, green, blue
        *  `frames.render = 1` for a single combined image
* Images are encoded as numbers for each pixel
* For grayscale: range from 0 (black) to 1 (white)
* Data is stored in a 3D matrix
    * x
    * y
    * frame

## Display

* Can show image using `plot` or `display`
* `plot` makes a simple graph of the first frame

```
plot(nuclei_img)
```

* `display` allows interactive viewing

```
display(nuclei_img)
```

## Cropping

* Because an image is just a matrix of numbers
* Cropping is like subsetting a matrix

```
nuclei_img_cropped <- nuclei_img[200:300, 350:450, 1]
display(nuclei_img_cropped)
```

* Just work with one image for simplicity
* Get all rows and columns for a single frame

```
nuclei_img = nuclei_img[,,1]
nuclei_img
```

## Thresholding

* Distinguish between background and objects
* We can see which areas are nuclei and which aren't
* But the computer just sees continuous numbers
* Even in areas that appear clearly black the numbers aren't zero

```
nuclei_img[220:225, 220:225]
```

* Thresholding makes pixels binary
    * True or False
    * Part of a nuclei or not

* Can do this manually

```
nuclei_thresh <- nuclei_img > 0.5
display(nuclei_thresh)
```

* But determining the right threshold can be tricky
* Our first try left some nuclei out
* Try a lower threshold

```
nuclei_thresh <- nuclei_img > 0.1
display(nuclei_thresh)
```

* Leaves too many pixels in

* Automatically select threshold with Otsu's method
    * Clusters pixels by intensity to get a better result

```
threshold <- otsu(nuclei_img)
nuclei_thresh <- nuclei_img > threshold
display(nuclei_thresh)
```

* Adaptive thresholding- vary threshold by location in image

## Image segmentation

* Split the image up into unique objects
* One simple way is to group all contiguous threshold pixels into an object

```
nuclei_segmented <- bwlabel(nuclei_thresh)
```

* Labels each distinct nuclei with a different number (class)

```
nuclei_segmented
nuclei_segmented@.Data[1:15, 1:15]
```

* Can them display them with different colors
  
```
display(colorLabels(nuclei_segmented))
```

## Counting objects

* With this segmentation we can then count the number of nuclei
* One unique number for each nuclei so the biggest number is the number of nuclei

```
max(nuclei_segmented)
```

* 98 nuclei in this image


## Measuring

* Measure the location and features of the objects
* `computeFeatures` 
* Information on shape and size

```
computeFeatures.shape(nuclei_segmented)
```

* Information on location

```
computeFeatures(nuclei_segmented, nuclei_img)
```

* Measures are in pixels
* Include an object of known size to convert to meaningful units

## Conclusions

* Threshold -> Segment
* Lets us count and measure objects in an image