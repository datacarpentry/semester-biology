---
layout: page
element: lecture
title: Repeating Things 1
language: R
---

### Setup

```r
install.packages(c('dplyr', 'ggplot2', 'readr', 'tidyr'))
download.file("https://datacarpentry.org/semester-biology/data/dinosaur_lengths.csv",
  "dinosaur_lengths.csv")
download.file("https://datacarpentry.org/semester-biology/data/ramesh2010-macroplots.csv",
  "ramesh2010-macroplots.csv")
download.file("https://ndownloader.figshare.com/files/5629536",
  "TREE_SURVEYS.txt")
download.file("https://ndownloader.figshare.com/files/2292172",
  "surveys.csv")
download.file("https://ndownloader.figshare.com/files/3299474",
  "plots.csv")
download.file("https://ndownloader.figshare.com/files/3299483",
  "species.csv")
```

### Lecture Notes

* [Iteration using vectorization and apply]({{ site.baseurl }}/materials/iteration-without-loops-R)
* [Detecting substrings with stringr]({{ site.baseurl }}/materials/stringr-detecting-substrings)
* [Style]({{ site.baseurl }}/materials/r-style)
