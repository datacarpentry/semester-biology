---
layout: exercise
title: R-SQL 2
subtitle: Automate Query
language: R
---

This is a follow-up to [R-SQL 1]({{ site.baseurl }}/exercises/Sql-2-R).

Dr. Undómiel agrees with you that the difference in male and female *D. spectabilis* hind foot length and weight seems pretty small, but wants to have a reference point for comparison. She wants you to find the male and female hind foot length and weight for all species of rodent. 

1. Generate a list of all of the rodent species at Portal.
2. Automate the queries you used to `SELECT` the average hind foot length and 
average weight of male and female *D. spectabilis* by using a `for` loop and the 
`paste()` function to cycle through the 
3. Store the results in a data frame with the 
`species_id`, `sex`, `avg_hindfoot_length`, and `avg_weight`.