---
layout: exercise
topic: Loops
title: Basic Vector
language: R
---

The following code gets just the genus from strings that are scientific names and capitalizes the first letter of the genus name. The `str_extract` and `str_to_title` functions are from the [`stringr` package](https://cran.r-project.org/web/packages/stringr/vignettes/stringr.html), which is great for working with strings. 

```
waterbird <- "cygnus olor"
waterbird_genus <- str_extract(waterbird, "\\w+")
waterbird_genus_cap <- str_to_title(waterbird_genus)
print(waterbird_genus_cap)
```

Modify the code to loop over a vector of multiple scientific names and print the capitalized genus names to the screen one line at a time, using the following vector: 

```
waterbirds <- c("cygnus olor", "aix sponsa", "anas acuta")
```
