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

The following function takes a subset of the data for a given `ANT` symbiont
and evaluates the linear regression (`lm()`) for a given relationship, returning
the symbiont `species` used for the subset and the `r2` of the model. 

```
report_rsquared <- function(data, species, formula){
  subset <- dplyr::filter(data, ANT == species)
  test <- lm(formula, data = subset)
  rsquared <- round(summary(test)$r.squared, 3)
  output <- data.frame(species = species, r2 = rsquared)
  return(output)
}
```

1. Execute the function using the [UHURU data](http://www.esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt)
   and specifying `species = "CM"` and `formula = "AXIS1~CIRC"`.
2. Modify the function so that it also determines `if()` the `rsquared` is
   significant based on a given `threshold`. The modified function should 
   `return()` the `species`, `rsquared` and a `significance` value of `"S"` for
   a relationship with an `rsquared > threshold` or `"NS"` for an `rsquared <
   threshold`.
3. Execute your modified function for `species` of `"CM"`, `"CS"`, and `"TP"`
   given a `threshold = 0.667`. 
