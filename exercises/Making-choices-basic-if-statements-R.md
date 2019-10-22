---
layout: exercise
topic: Making Choices
title: Basic If Statements
language: R
---

1\. Complete (i.e., copy into your code and them modify) the following `if`
   statement so that if `age_class` is equal to "sapling" it sets `y <- 10`.

```r
age_class = "sapling"
if (){
  
}
y
```

2\. Complete the following `if` statement so that if `age_class` is equal to
   "sapling" it sets `y <- 10` and if `age_class` is equal to "seedling" it
   sets `y <- 5`.

```r
age_class = "seedling"
if (){
  
}
y
```

3\. Complete the following `if` statement so that if `age_class` is equal to
   "sapling" it sets `y <- 10` and if `age_class` is equal to "seedling" it
   sets `y <- 5` and if `age_class` is something else then it sets the value of
   `y <- 0`.

```r
age_class = "adult"
if (){
  
}
y
```

4\. Convert your conditional statement from (3) into a function that takes
   `age_class` as an argument and returns `y`. Call this function 5 times, once
   with each of the following values for `age_class`: "sapling", "seedling",
   "adult", "mature", "established".
