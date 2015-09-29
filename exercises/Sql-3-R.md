---
layout: exercise
title: R-SQL 3
subtitle: Data Stream
language: R
---

This is a follow-up to [R-SQL 2]({{ site.baseurl }}/exercises/Sql-2-R).

Dr. Undómiel is really testing your kindness now. She's seen that all of the 
average hind foot length and average weights are pretty similar within species, 
but she wants to support the idea with some statistics. 

1. Modify your species list to remove `species_id` with insufficient data 
(*i.e., remove species that return <NA> in the R-SQL 2 results table for either `sex` AND remove `species=='PX'` because it only has one entry per `sex` *). 

2. Write a function that selects the `sex`, `hindfoot_length` and `weight` data 
for a species and returns the results of a `t.test()` of each measurement 
factored by sex. A `t.test()` takes two primary arguments: a vector or data 
frame of values for group a and the same class of data for group b. The 
arguments can also be expressed in formula form similar to `aov()`. Be sure to 
assign the results to an object (`test <- t.test()`), so you can extract the  
*p*-value from the object (`test$p.value`) to include in your results.  

3. Loop the updated species list and generate an output data frame with the 
`species_id`, `p_hindfoot_length`, `p_weight`.