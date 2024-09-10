---
layout: page
element: lecture
title: Grouping & Joining Data
language: R
---

### Setup

```r
install.packages('dplyr')
download.file("https://ndownloader.figshare.com/files/2292172",
              "surveys.csv")
download.file("https://ndownloader.figshare.com/files/3299474",
              "plots.csv")
download.file("https://ndownloader.figshare.com/files/3299483",
              "species.csv")
download.file("https://www.datacarpentry.org/semester-biology/data/shrub-volume-data.csv",
              "shrub-volume-data.csv")
download.file("https://datacarpentry.org/semester-biology/data/mbaiki_measures.csv",
              "mbaiki_measures.csv")
download.file("https://datacarpentry.org/semester-biology/data/mbaiki_trees.csv",
              "mbaiki_trees.csv")
download.file("https://datacarpentry.org/semester-biology/data/mbaiki_species.csv",
              "mbaiki_species.csv")
```

### Lecture Notes

* [dplyr Aggregation]({{ site.baseurl }}/materials/dplyr-aggregation)
* [dplyr Joins]({{ site.baseurl }}/materials/dplyr-joins)
* [Converting between data frames and vectors]({{ site.baseurl }}/materials/converting-dataframes-vectors)
