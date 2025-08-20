---
layout: page
element: lecture
title: Solving Bigger Problems
language: R
---

### Setup

```r
install.packages(c('dplyr', 'ggplot2', 'readr', 'tidyr'))
download.file("https://ndownloader.figshare.com/files/2292172",
  "surveys.csv")
download.file("https://ndownloader.figshare.com/files/3299474",
  "plots.csv")
download.file("https://ndownloader.figshare.com/files/3299483",
  "species.csv")
download.file("https://datacarpentry.org/semester-biology/data/mammal-size-data-clean.tsv",
  "mammal-size-data-clean.tsv")
download.file("https://datacarpentry.org/semester-biology/data/ramesh2010-macroplots.csv",
  "ramesh2010-macroplots.csv")
download.file("https://datacarpentry.org/semester-biology/data/ramesh2010-species-list.tsv",
  "ramesh2010-species-list.tsv")
```

### Lecture Notes

1. [Problem Decomposition]({{ site.baseurl }}/materials/problem-decomposition)
2. [Basic Debugging]({{ site.baseurl }}/materials/basic-debugging-R)
3. [Searching For Help]({{ site.baseurl }}/materials/googling-for-help)
4. [Paths]({{ site.baseurl }}/materials/paths-R)
5. [Basic Reproducibility]({{ site.baseurl }}/materials/basic-reproducibility-R)