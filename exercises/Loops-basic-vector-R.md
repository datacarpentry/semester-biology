---
layout: exercise
topic: Loops
title: Basic Vector
language: R
---

The following code capitalizes the first letter of `pet` and stores it as
`name`:

```
library(stringr)
pet <- "spot"
pet_letters <- str_split(pet, "")[[1]]
first <- toupper(pet_letters[1])
others <- str_c(pet_letters[-1], collapse = "")
name <- str_c(first, others, sep = "")
```

Modify the code to loop over a vector of multiple pet names and print them to
the screen one line at a time. Use the vector of pet names:

```
pets <- c("spot", "gigantor", "fluffy")
```

This code uses the excellent
[`stringr` package](http://cran.r-project.org/web/packages/stringr/stringr.pdf)
for working with the sequence data. You'll need to install this package before
using it.