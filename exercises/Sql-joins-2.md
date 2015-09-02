---
layout: exercise
title: Joins 2
subtitle: JOIN for Non-rodents
language: SQL
---

You are curious about what other kinds of animals get caught in the Sherman
traps used to census the rodents. Write a query that returns a list of the
`genus`, `species`, and `taxa` (from the species table) for non-rodent 
individuals that are caught on the control plots. Non rodents are indicated in the `taxa` column of the `Species` table. You are only interested in 
which species are captured, so make this list unique (only one line for each
species). Save this query as `Non-rodents On Controls`.
