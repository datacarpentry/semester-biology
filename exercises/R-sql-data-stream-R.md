---
layout: exercise
topic: R-SQL
title: Data Stream
language: R
---

This is a follow-up to [Automate Query]({{ site.baseurl }}/exercises/R-sql-automate-query-R).

Dr. Undómiel is really testing your kindness now. She's seen that all of the 
average hind foot length and average weights are pretty similar within species, 
but she wants to support the idea with some statistics. 

1. Write a function that selects the `sex`, `hindfoot_length` and `weight` data 
for a given species. 

2. Write a function that uses the data from the first function and returns the results of a 
`t.test()` of each measurement factored by sex. (*HINT: A `t.test()` takes two primary 
arguments: a vector or data frame of values for group a and the same class of data for group 
b. The arguments can also be expressed in formula form similar to `aov()`. Be sure to 
assign the results to an object (`test <- t.test()`), so you can extract the  *p*-value from the 
object (`test$p.value`) to include in your results.*)  

3. Loop through the rodent species at Portal and generate an output data frame 
with the `species_id`, `p_hindfoot_length`, `p_weight`. (*HINT: You are 
likely to run into some issues of insufficient data that you should skip in your loop.*)
