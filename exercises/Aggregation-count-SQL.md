---
layout: exercise
topic: Aggregation
title: COUNT
language: SQL
---

Write a query that returns the number of individuals trapped in each year. Count
the `species_id` column so that you only include cases where an individual was
identified to species. Name the count column `total_abundance` and sort it
chronologically. Include the year in the output. Save it as
`total_abundance_by_year`. There should only be one value for each year since
this is a count of the individuals across all species in that year.
