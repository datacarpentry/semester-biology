---
layout: exercise
topic: Advanced Queries
title: Multi-table Join
language: SQL
---

The `plots` table in the Portal database can be joined to the `surveys` table
by joining `plot_id` to `plot_id` and the `species` table can be joined to
the `surveys` table by joining `species_id` to `species_id`.

The Portal mammal data include data from a number of different experimental
manipulations. You want to do a time-series analysis of the population dynamics
of all of the species at the site, taking into account the different
experimental manipulations. Write a query that returns the `year`, `month`,
`day`, `genus` and `species` of every individual as well as the `plot_id` and `plot_type` of the plot they are captured on. Save this query as 
`species_plot_data`.
