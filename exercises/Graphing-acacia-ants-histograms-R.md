---

layout: exercise
topic: Graphing
title: Acacia and Ants Histograms
language: R
---

An experiment in Kenya has been exploring the influence of large herbivores on plants.

If [`ACACIA_DREPANOLOBIUM_SURVEY.txt`](https://esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt) is not in your workspace download it.
Read it into R using the following command:

```r
acacia <- read_tsv("data/ACACIA_DREPANOLOBIUM_SURVEY.txt", na = c("dead"))
```

1. Make a bar plot of the number of acacia with each mutualist ant species (using the `ANT` column).
2. Make a histogram of the height of acacia (using the `HEIGHT` column). Label
   the x axis "Height (m)" and the y axis "Number of Acacia".
3. Make a bar plot of the number of acacia in each `TREATMENT`. Label the x
   axis "Treatment" and the y axis "Number of Acacia".
4. Make a histogram of the circumference of acacia (using the `CIRC` column)
   with a `binwidth` of 5. Label the x axis "Circumference (cm)" and the y
   axis "Number of Acacia".
