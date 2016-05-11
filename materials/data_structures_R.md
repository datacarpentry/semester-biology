---
layout: page
element: notes
title: Data Structures
language: R
--- 

## Vectors

* sequence of values with the same type
* make one using c(): `sites <- c("a", "a", "b", "b")`
* explore: `str(sites)`, `length(sites)`
* Use the Tab key for autocomplete: Let the computer do repetitious work, easier, few mistakes
* slicing: `sites[1]`, `sites[1:3]`, `1:3` makes a vector so this is the same as
  `sites[c(1, 2, 3)]` which you can use to get any subset or order you want
* math:

```
counts <- c(0, 2, 2, 6)
weights <- c(1.5, 2.6, 8.4, 0.2)
sum(counts)
max(weights)
total_weight <- sum(weights)
```

* subsetting: `counts[sites == 'a']`
* `==` means "equal to" in most languages; `=` means assignment

***Exercise 1***

## Matrices (if linear algebra folks)

```
x <- matrix(1:6, 2)
y <- matrix(1:3, ncol = 1)
x %*% y
```

## Data Frames

* A list of equal length vectors grouped together
* Create: `surveys <- data.frame(sites, counts, weights)` or `read.csv`
* Explore: `str(surveys)`, `length(surveys)`, `nrow(surveys)`,`ncol(surveys)`
* Subsetting columns

```
surveys["sites"]
surveys[c("counts", "weights")]
surveys$sites
surveys[["sites"]]
```

* Subsetting rows: `subset(surveys, sites == 'a')`
* Subsetting values/blocks: `surveys[1,2]`, `surveys[1:2,1:3]`

***Exercise 3***
