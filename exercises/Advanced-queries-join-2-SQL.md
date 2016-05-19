---
layout: exercise
topic: Advanced Queries
title: JOIN 2
language: SQL
---

You are curious about what other kinds of animals get caught in the Sherman
traps used to census the rodents. Write a query that returns a list of the
`genus`, `species`, and `taxa` (from the species table) for non-rodent
individuals that are caught on the `Control` plots. Non-rodents are indicated in
the `taxa` column of the `Species` table. You are only interested in which
species are captured, so make this list unique (only one line for each
species). Save this query as `non_rodents_on_controls`.
