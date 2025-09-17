---

layout: exercise
topic: Graphing
title: Acacia and Ants Histograms
language: R
---

An experiment in Kenya has been exploring the influence of large herbivores on plants.

Check to see if `ACACIA_DREPANOLOBIUM_SURVEY.txt` is in your workspace.
If not, [download it](https://esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt).
Read it into R using the following command:

```r
acacia <- read_tsv("data/ACACIA_DREPANOLOBIUM_SURVEY.txt", na = c("dead"))
```

1. Make a bar plot of the number of acacia with each mutualist ant species (using the `ANT` column).
2. Make a histogram of the height of acacia (using the `HEIGHT` column). Label
   the x axis "Height (m)" and the y axis "Number of Acacia".
3. Make a **non-stacked** histogram of the height of acacia (using the `HEIGHT` column) colored by the `TREATMENT`.
   Set the transparency (using `alpha`) to 0.5 so that you can see all of the bars.
   Label the x-axis "Heigth (m)" and the y-axis "Count of Acacia".
   Set the binwidth to 0.5.
