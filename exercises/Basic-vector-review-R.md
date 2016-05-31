---
layout: exercise
topic: Basic
title: Vector Review
language: R
---

The number of birds banded at a series of sampling sites has been counted by
your field crew. The data are organized in two vectors. The first vector contains the alphanumeric code for each site and the second vector contains the number
of birds banded per site. Cut and paste the vectors into your assignment and then answer the following questions by printing them to the screen.

```
sites <- c("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", 
"B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "C1", "C2", 
"C3", "C4", "D1", "D2", "D3", "D4", "D5", "D6")

counts <- c(28, 32, 1, 0, 10, 22, 30, 19, 145, 27, 36, 25, 9, 
38, 21, 12, 122, 87, 36, 3, 0, 5, 55, 62, 98, 32)
```

1.  How many sites are there?
2.  How many birds were counted at the 7th site?
3.  How many birds were counted at the last site?
4.  What is the total number of birds counted across all sites?
5.  What is the average number of birds seen on a site?
6.  What is the total number of birds counted on sites with codes
    beginning with C? *Don't just identify this sites by eye, in the
    real world there could be hundreds or thousands of sites.*
