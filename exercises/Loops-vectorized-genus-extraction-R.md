---
layout: exercise
topic: Loops
title: Vectorized Genus Extraction
language: R
---

The following code gets extracts the genus from strings that are scientific names (include both genus and species). The `str_extract` function is from the [`stringr` package](https://cran.r-project.org/web/packages/stringr/vignettes/stringr.html), which is great for working with strings. 

```
waterbird <- "cygnus olor"
waterbird_genus <- str_extract(waterbird, "\\w+")
```

`str_extract` is a vectorized function meaning it can take a multiple species names as input and return one genera for each species. Modify the code to produce a vector of genera for the following vector of species names:

```r
waterbirds <- c("cygnus olor", "aix sponsa", "anas acuta")
```
