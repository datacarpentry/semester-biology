---
layout: page
element: notes
title: Detecting substrings with stringr
language: R
---

* Remember that in `if` statements there are a couple of different things we can use to decide whether to execute the code in the statement or not
* We can use conditional statements

```r
if (height > 5) {
  
}
```

* But we can also use functions that return boolean values
* So if we want to do something when the value of `height` is null we can use `is.na()`

```r
if (is.na(height)) {
  
}
```

* We're going to use a new function that returns `TRUE` or `FALSE` in an exercise
* That function is from the `stringr` package that is useful for processing strings
  
```r
library(stringr)
```

* Its name is `str_detect()` and it checks if a substring is part of a larger string

```r
str_detect("Halloween is spooky", "scary")
```

* In our exercise we have a `SPECIES` column
* It has a bunch of values that include the word `Acacia` (a genus), but also species names
* We want to do something for all Acacia
* Use `str_detect()`

```r
str_detect(SPECIES, "Acacia")
```
