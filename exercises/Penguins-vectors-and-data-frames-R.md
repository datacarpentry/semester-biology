---
layout: exercise
topic: dplyr
title: Penguins Vectors and Data Frames
language: R
---

If the file [`penguins_no_na.csv`]({{ site.baseurl }}/data/penguins_no_na.csv) is not already in your working directory then download it into your working directory.

Load `penguins_no_na.csv` into R using `read_csv()`.

Copy the following vectors into R:

```r
region = c("Anvers", "Anvers", "Anvers")
island = c("Biscoe", "Dream", "Torgersen")
area = c(26.2, 42.0, 6.7)
```

1. Use $ to extract the flipper length column into a vector
2. Use [] to extract the body mass column into a vector
3. Extract the bill length column into a vector using pull() and use this vector to determine the maximum bill length
4. Using the vectors you copied into R, create a new data frame named `islands` with `region`, `island`, and `area` columns
5. Create a combined table including the information from both the penguins and the islands tables together
