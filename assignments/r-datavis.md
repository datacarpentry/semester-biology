---
layout: page
element: assignment
title: Data Visualization
language: R
exercises:
  [
    "Acacia and Ants",
    "Mass vs Metabolism",
    "Acacia and Ants Data Manipulation",
    "Lifespan vs Gestation Time",
    "Acacia and Ants Histograms",
    "Acacia and Ants Layers",
    "Check That Your Code Runs",
    "Graphing Data From Multiple Tables",
  ]
points: [10, 10, 10, 20, 20, 20, 10, "Challenge - optional"]
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
