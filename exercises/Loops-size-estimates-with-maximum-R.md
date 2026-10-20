---
layout: exercise
topic: Loops
title: Size Estimates With Maximum
language: R
---

Copy the vector below into R.

```r
dinosaur_lengths <- c(17.8013631070471, 20.3764452071665, 14.0743486294308, 25.65782386974, 26.0952008049675, 20.3111541103134, 17.5663244372533, 11.2563431277577, 20.081903202614, 18.6071626441984, 18.0991894513166, 23.0659685685892, 20.5798853467837, 25.6179254233558, 24.3714331573996, 26.2847248252537, 25.4753783544473, 20.4642089867304, 16.0738256364701, 20.3494171706583, 19.854399305869, 17.7889814608919, 14.8016421998303, 19.6840911485379, 19.4685885050906, 24.4807784966691, 13.3359960054899, 21.5065994598917, 18.4640304608411, 19.5861532398676, 27.084751999756, 18.9609366301798, 22.4829168046521, 11.7325716149514, 18.3758846100456, 15.537504851634, 13.4848751773738, 7.68561192214935, 25.5963348603783, 16.588285389794)
```

1. Write a function named `mass_from_length_max` that takes `dino_length` as an argument. If `dino_length` is less than 20 estimate the mass of the dinosaur using the equation `mass <- 0.73 * dino_length ^ 3.63`. If `dino_length` is greater than or equal to 20 return `NA` instead. Run this function with 18 as the input.
2. Use `map_dbl()` and this function to estimate the mass for every length in `dinosaur_lengths`.
3. Write a function named `mass_from_length_min` that takes `dino_length` as an argument. If `dino_length` is greater than 23 estimate the mass of the dinosaur using the equation `mass <- 0.73 * dino_length ^ 3.63`. If `dino_length` is less than or equal to 23 use the equation `mass <- 1.2 * dino_length ^ 1.5` instead. Run this function with 24 as the input.
4. Use `map_dbl()` and this function to estimate the mass for every length in `dinosaur_lengths`.
