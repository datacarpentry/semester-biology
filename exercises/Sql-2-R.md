---
layout: exercise
title: R-SQL 2
subtitle: Automate Query
language: R
---

This is a follow-up to [R-SQL 1]({{ site.baseurl }}/exercises/Sql-2-R).

Dr. Undómiel agrees with you that the difference in male and female
*D. spectabilis* hind foot length and weight seems pretty small, but wants to
have a reference point for comparison. She wants you to find the male and female
hind foot length and weight for all species of rodent on all of the plots (not
just the controls).

Produce a data frame with `species_id`, `sex`, `avg_hindfoot_length`, and
`avg_weight` for each species.  Your data frame should have two rows for each
species, one row for each sex.

You can solve this problem in a variety of ways including using `dplyr`, a
`GROUP BY` in your SQL query, a `for` loop, or using `apply` statements. Take
whichever approach you like best.
