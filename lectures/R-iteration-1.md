---
layout: page
element: lecture
title: Repeating Things 1
language: R
---

### Setup

```r
install.packages(c('dplyr', 'ggplot2', 'readr'))
download.file("https://datacarpentry.org/semester-biology/data/dinosaur_lengths.csv",
  "surveys.csv")
download.file("https://datacarpentry.org/semester-biology/data/ramesh2010-macroplots.csv",
  "ramesh2010-macroplots.csv")
download.file("https://ndownloader.figshare.com/files/5629536",
  "TREE_SURVEYS.txt")
```

### Lecture Notes

* [Iteration using vectorization and apply]({{ site.baseurl }}/materials/iteration-without-loops-R)
* [Detecting substrings with stringr]({{ site.baseurl }}/materials/stringr-detecting-substrings)
* [Style]({{ site.baseurl }}/materials/r-style)
