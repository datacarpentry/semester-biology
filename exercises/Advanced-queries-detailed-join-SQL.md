---
layout: exercise
topic: Advanced Queries
title: Detailed Join
language: SQL
---

We want to do an analysis comparing the size of individuals on the `Control`
plots to the `Long-term Krat Exclosures`. Write a query that returns the `year`,
`genus`, `species`, `weight` and the `plot_type` for all cases where the plot
type is either `Control` or `Long-term Krat Exclosure`. Be sure to choose only
rodents and exclude individuals that have not been identified to species (i.e.,
exclude species with `sp.` in the species column). Remove any records where the
`weight` is missing. Save this query as
`size_comparison_controls_vs_krat_exclosures`.
