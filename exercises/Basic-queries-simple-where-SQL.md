---
layout: exercise
topic: Basic Queries
title: Simple WHERE
language: SQL
---

A population biologist (Dr. Undomiel) who studies the population dynamics of
*Dipodomys spectabilis* would like to use some data from the Portal Project, but
she doesn't know how to work with large datasets.

Write a query that returns the `month`, `day`, `year`, and `weight` of each
individual of *Dipodomys spectabilis* (`DS` in the `species_id` column). Do not
include the `species_id` column in the output. Save this query as a view with
the name `spectabilis_population_data`.
