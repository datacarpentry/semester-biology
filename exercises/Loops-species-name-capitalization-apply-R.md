---
layout: exercise
topic: Loops
title: Species Name Capitalization with Apply
language: R
---

You have some data with species names that are stored in capital letters.
You want to capitalize them properly so that the genus starts with a capital letter and the other letters are lower case.
The `str_to_sentence` function from the `stringr` package can do this:

```r
library(stringr)

species <- "CYGNUS OLOR"
species_clean <- str_to_sentence(species)
```

1\. Use `sapply` and `str_to_sentence` to produce a vector of properly capitalized species names from the following vector of species names:

```r
species <- c("CYGNUS OLOR", "AIX SPONSA", "ANAS ACUTA")
```

2\. Replace `sapply` with `lapply` to get the answer as a list instead of a vector.

3\. Use `lapply` to get the properly capitalized species and the use `unlist` to convert the result to a vector.

*Note: this exercise doesn't technically require the use of an apply function, but we're going to use one to keep our first use of apply simple.*
