---
layout: exercise
topic: Advanced Queries
title: JOIN 1
language: SQL
---

The `Plots` table in the Portal database can be joined to the `Surveys` table
by joining `plot_id` to `plot_id` and the `Species` table can be joined to
the `Surveys` table by joining `species_id` to `species_id`.

The Portal mammal data include data from a number of different
experimental manipulations. You want to do a time-series analysis of the
natural population dynamics of all of the rodent species at the site, so
write a query that returns the `year`, `month`, `day`, `genus` and `species`
of every individual captured on the `Control` plots. Choose only
rodent species (i.e., species for which the `taxa` field in the
species table is `Rodent`) and exclude all individuals that have not been
identified to genus (i.e., species for which the `species_id` field in the
species table is `UR`). Save this query as `data_from_controls`.
