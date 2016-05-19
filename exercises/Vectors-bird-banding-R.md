---
layout: exercise
topic: Vectors
title: Bird Banding
language: R
---

The number of birds banded at a series of sampling sites has been counted by
your field crew and entered into the following vector. Counts are entered in 
order and sites are numbered starting at one. Cut and paste the list into your
assignment and then answer the following questions by printing them to the
screen. Some R functions that will come in handy include `length()`, `max()`,
`min()`, `sum()`, and `mean()`.

```
number_of_birds <- c(28, 32, 1, 0, 10, 22, 30, 19, 145, 27, 
36, 25, 9, 38, 21, 12, 122, 87, 36, 3, 0, 5, 55, 62, 98, 32, 
900, 33, 14, 39, 56, 81, 29, 38, 1, 0, 143, 37, 98, 77, 92, 
83, 34, 98, 40, 45, 51, 17, 22, 37, 48, 38, 91, 73, 54, 46,
102, 273, 600, 10, 11)
```

1. How many sites are there?
2. How many birds were counted at site 42?
3. How many birds were counted at the last site? Have the computer
choose the last site automatically in some way, not by manually
entering its position.
4. What is the total number of birds counted across all of the sites?
5. What is the smallest number of birds counted?
6. What is the largest number of birds counted?
7. What is the average number of birds seen at a site?
