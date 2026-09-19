---
layout: page
element: assignment
title: Data Visualization
language: R
exercises:
  [
    "Acacia and Ants",
    "Acacia and Ants Color and Facets",
    "Mass vs Metabolism",
    "Acacia and Ants Data Manipulation",
    "Acacia and Ants Histograms",
    "Acacia and Ants Stacked Plots",
    "Acacia and Ants Layers",
    "Lifespan vs Gestation Time",
    "Check That Your Code Runs",
    "Graphing Data From Multiple Tables",
  ]
points: [10, 10, 10, 10, 10, 10, 15, 15, 10, "Challenge - optional"]
---

### Learning Objectives

> Following this assignment students should be able to:
>
> - understand the basic plot function of `ggplot2`
> - import 'messy' data with missing values and extra lines
> - execute and visualize a regression analysis

{% include reading.html %}

Place this code at the start of the assignment to load all the required packages.

```r
library(dplyr)
library(ggplot2)
library(readr)
```

{% include assignment.html %}
