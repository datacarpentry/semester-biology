---
layout: exercise
topic: Loops
title: Basic Vector
language: R
---

The following code capitalizes the first letter of `pet`, puts it in a sentence,
and stores it as `my_pet`:

```
pet <- "spot"
pet_name <- stringr::str_to_title(pet)
my_pet <- paste("My pet's name is ", pet_name, ".", sep = "")
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