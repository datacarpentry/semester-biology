---
layout: exercise
topic: Loops
title: Size Estimates Vectorized
language: R
---

This is a followup to [Use and Modify]({{ site.baseurl }}/exercises/Functions-use-and-modify-R).

1. Write a function that takes `length` as an argument to get an estimate of mass values for the dinosaur *Theropoda*. Use the equation `mass <- 0.73 * length^3.63`. Copy the data below into R and pass the entire vector to your function to calculate the estimated mass for each dinosaur.

	`theropoda_lengths <- c(17.8013631070471, 20.3764452071665, 14.0743486294308, 25.65782386974, 26.0952008049675, 20.3111541103134, 17.5663244372533, 11.2563431277577, 20.081903202614, 18.6071626441984, 18.0991894513166, 23.0659685685892, 20.5798853467837, 25.6179254233558, 24.3714331573996, 26.2847248252537, 25.4753783544473, 20.4642089867304, 16.0738256364701, 20.3494171706583, 19.854399305869, 17.7889814608919, 14.8016421998303, 19.6840911485379, 19.4685885050906, 24.4807784966691, 13.3359960054899, 21.5065994598917, 18.4640304608411, 19.5861532398676, 27.084751999756, 18.9609366301798, 22.4829168046521, 11.7325716149514, 18.3758846100456, 15.537504851634, 13.4848751773738, 7.68561192214935, 25.5963348603783, 16.588285389794)`

2. Rewrite the function to use the equation `mass <- a * length^b` and take `length`, `a` and `b` as arguments. Set the default values for `a` to `0.73` and `b` to `3.63` so that the code from (1) still works. Copy the data below into R and call your function using vector of lengths (above) and these vectors of `a` and `b` values to estimate the mass for the dinosaurs using different values of `a` and `b`.

	`a_values <- c(0.759, 0.751, 0.74, 0.746, 0.759, 0.751, 0.749, 0.751, 0.738, 0.768, 0.736, 0.749, 0.746, 0.744, 0.749, 0.751, 0.744, 0.754, 0.774, 0.751, 0.763, 0.749, 0.741, 0.754, 0.746, 0.755, 0.764, 0.758, 0.76, 0.748, 0.745, 0.756, 0.739, 0.733, 0.757, 0.747, 0.741, 0.752, 0.752, 0.748)`

	`b_values <- c(3.627, 3.633, 3.626, 3.633, 3.627, 3.629, 3.632, 3.628, 3.633, 3.627, 3.621, 3.63, 3.631, 3.632, 3.628, 3.626, 3.639, 3.626, 3.635, 3.629, 3.642, 3.632, 3.633, 3.629, 3.62, 3.619, 3.638, 3.627, 3.621, 3.628, 3.628, 3.635, 3.624, 3.621, 3.621, 3.632, 3.627, 3.624, 3.634, 3.621)`

3. Create a data frame for this data using `dino_data <- data.frame(theropoda_lengths, a_values, b_values)`. Using `dplyr` add a new `masses` column to this data frame (using `mutate` and your function).