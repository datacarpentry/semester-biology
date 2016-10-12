---
layout: exercise
topic: dplyr Databases
title: Manipulate Query
language: R
---

This is a follow-up to [Source and Query]({{ site.baseurl }}/exercises/Dplyr-databases-source-and-query-R).

Dr. Undómiel agrees with you that the difference in male and female
*D. spectabilis* hind foot length and weight seems pretty small, but wants to
make a more detailed comparison. She wants you to find the male and female
hind foot length and weight for all species of rodent on all of the plots (*not
just the controls*) and quantitatively define the size differences among species.

1. Produce a data frame with `species_id`, `sex`, `avg_hindfoot_length`, and
   `avg_weight` for each species.  Your data frame should have two rows for each
   species, one row for each sex.

   *You can solve this problem with `dplyr` in a variety of ways including
   writing a query or using data manipulation verbs to group and select the
   data. You could also decide to use `for` loops or `apply` statements. Take
   whichever approach you like best.*

2. Write a function that determines if the absolute difference in average male
   and female size is less than the standard deviation of sizes for all
   individuals (`abs(male - female) <= stdev`).

3. Manipulate the data so that you have a local data frame that has average male 
   and female `hindfoot_length` and `weight` and the standard deviations in a
   single row for each species. 

4. Use `transmute()` and an `ifelse()` with your function to take each species 
   `hindfoot_length` and `weight` from your local data frame and make a new data 
   frame as that labels the results of your simple calculation as `"SAME"` or 
   `"DIFF"`.

   *You may find that you get an `Error: non-numeric argument to binary 
   operator`. The missing size data causes `mean()` to return results as a
   `character`. Remove the missing data from your query or re-class the results
   `as.numeric()` to make your calculation.*
