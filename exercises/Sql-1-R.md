---
layout: exercise
title: R-SQL 1
subtitle: Connect and Query
language: R
---

This is a follow up to the [SQL Filtering]({{ site.baseurl }}/exercises/Sql-filtering) problem.

It is clear Dr. Undómiel appreciates your skill working with large databases and 
she seems to expect you will maintain your benevolence. (*Such is a fair 
expectation of a true wizard*). This time though, she's looking for some extra 
detail in her queries. She's curious if desert rodents are [dimorphic](https://en.wikipedia.org/wiki/Sexual_dimorphism) in size.
 

1. Connect to the `portal-database.sqlite` using the `RSQLite` package. 
2. From the `surveys` table, `SELECT` and print out the average (`AVG()`) hind 
foot length and average weight of:
  - all *Dipodomys spectabilis* individuals
  - male *D. spectabilis*
  - female *D. spectabilis*.


