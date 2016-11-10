---
layout: exercise
topic: Making Choices
title: Choices with Functions
language: R
---

The [UHURU experiment](http://www.esapubs.org/archive/ecol/E095/064/metadata.php)
in Kenya has conducted a survey of *Acacia drepanolobium* among each of their
ungulate exclosure treatments. Data for the survey is available [here](http://www.esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt)
in a tab delimited (`"\t"`) format. Each of the individuals surveyed were
measured for branch circumference (`CIRC`) and canopy width (`AXIS1`) and was
identified for the associated ant-symbiont species present (`ANT`). 

1. Write a function that evaluates the linear regression (`lm()`) for the
   `AXIS1 ~ CIRC` relationship and returns the *r<sup>2</sup>* of the model. 

   *For a `test <- lm()`, get the r<sup>2</sup> using `summary(test)$r.squared`.*

2. Modify the function to take a subset of the data for a given `ANT`.
3. Nest your regression function into another function that determines
   `if()` the `r.squared` is significant based on a `threshold`. The
   function should `return()` the `ANT` designation of the subset and the
   `r.squared` `if()` it is significant, `else()` the function should `return()` 
   the `ANT` designation and `"NS"` for 'not significant'.
4. Use your nested functions to get the `r.squared` for each of the `ANT` 
   subsets for values `"CM"`, `"CS"`, and `"TP"` given a `threshold = 0.667`. 