---
layout: exercise
topic: Vectors
title: Bird Banding Multiple Vectors
language: R
---

The number of birds banded at a series of sampling sites has been counted by
your field crew and entered into the following vector. Counts are entered in 
order and sites are numbered starting at one.
There is also information on the number of trees at each site.
Cut and paste the vector into your
assignment and then answer the following questions by using code and printing the
result to the screen.

```r
number_of_birds <- c(28, 32, 1, 0, 10, 22, 30, NA, 145, 27, 
36, 25, 9, 38, 21, 12, 122, 87, 36, 3, 0, 5, 55, 62, 98, 32, 
900, 33, 14, 39, 56, 81, 29, 38, 1, 0, 143, 37, 98, 77, 92, 
83, 34, 98, 40, 45, 51, 17, 22, 37, 48, NA, 91, 73, 54, 46,
102, 273, 600, 10, 11)
number_of_trees <- c(10, 12, 2, 3, 10, 8, 19, 19, 14, 3, 
4, 5, 8, 4, 8, 1, 12, 10, 3, 1, 2, 3, 5, 6, 8, 2, 
90, 3, 4, 3, 6, 8, NA, 4, 0, 1, 14, 3, 10, NA, 9, 
8, 4, 8, 4, 4, 5, 1, 2, 3, 5, 4, 10, 7, 5, 8,
10, 30, 26, 1, 6)
```

1. How many sites are there?
2. How many birds were counted at the 26th site?
3. What is the largest number of birds counted?
4. What is the average number of birds seen at a site?
5. What is the total number of trees counted across all of the sites?
6. What is the smallest number of trees counted?
7. Produce a vector with the number of birds counted on sites with at least 10 trees.
8. Produce a vector with the number of trees counted on sites with at least 10 trees.
9. Combine the `number_of_birds` and `number_of_trees` vectors into a dataframe that also includes a year column with the year 2012 in every row and site column containing the numbers 1 through 61.