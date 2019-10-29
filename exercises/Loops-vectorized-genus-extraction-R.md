---
layout: exercise
topic: Loops
title: Vectorized Genus Extraction
language: R
---

The following code extracts the genus from strings that are scientific names (include both genus and species). The `str_extract` function is from the [`stringr` package](https://cran.r-project.org/web/packages/stringr/vignettes/stringr.html), which is great for working with strings. 

```
waterbird <- "cygnus olor"
str_extract(waterbird, "\\w+")
```

`str_extract` is a vectorized function meaning it can take a multiple species names as input and return one genera for each species.

1\. Copy and modify the code above to display a vector of genera for the following vector of species names:

```r
waterbirds <- c("cygnus olor", "aix sponsa", "anas acuta")
```

2\. Copy the code below to create a data frame and then add a new `genus` column to that data frame that contains the just the genus (the first word in each pair). Display the data frame.

```r
bird_data <- data.frame(species = c("cygnus olor", "aix sponsa", "anas acuta"))
```

