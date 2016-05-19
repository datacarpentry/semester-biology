---
layout: exercise
topic: SQL Practice
title: Basic Queries Review
language: R
---

This is a follow-up to [Introduction to Databases]({{ site.baseurl }}/assignments/sql-intro).

Download the [`sql_practice.sqlite` database]({{ site.baseurl }}/data/sql_practice.sqlite). Open it in SQLite Manager and write a query for each of the following:

*When writing the solution to each review problem, take a second to think carefully about which fields are actually relevant to the problem. Write your query so that only these relevant fields are selected for the final output. In other words, if you are going to do some form of analysis with the data you select, which fields do you actually need?* (**HINT: none of these problems should have SELECT \* in the answer.**)

1. Write a query that lists all the males in order by weight, starting with the heaviest.

2. Write a query that lists all males with a weight greater than 10 and all females with a weight less than 10.

3. Write a query that displays the number of females at each site. Name the field with the number of females something meaningful.
