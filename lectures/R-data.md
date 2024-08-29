---
layout: page
element: lecture
title: Data in Tables
language: R
---

### Setup

```r
install.packages(c('dplyr', 'readr', 'tidyr'))
download.file("https://ndownloader.figshare.com/files/2292172",
              "surveys.csv")
download.file("https://ndownloader.figshare.com/files/3299474",
              "plots.csv")
download.file("https://ndownloader.figshare.com/files/3299483",
              "species.csv")
download.file("https://www.datacarpentry.org/semester-biology/data/shrub-volume-data.csv",
              "shrub-volume-data.csv")
```

### Lecture Notes

* [Working with Tabular Data (in dplyr)]({{ site.baseurl }}/materials/dplyr)
* [Basic Code Execution Order]({{ site.baseurl }}/materials/code-execution-R)
* [Combining Data Manipulations]({{ site.baseurl }}/materials/combining-data-manip)
