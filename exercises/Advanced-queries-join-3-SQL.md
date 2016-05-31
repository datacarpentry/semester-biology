---
layout: exercise
topic: Advanced Queries
title: JOIN 3
language: SQL
---

We want to do an analysis comparing the size of individuals on the control plots
to the Long-term Krat Exclosures. Write a query that returns the `year`,
`genus`, `species`, `weight` and the `plot_type` for all cases where the plot
type is either `Control` or `Long-term Krat Exclosure`. Be sure to choose only
rodents and exclude individuals that have not been identified to genus as in
[Joins 1]({{ site.baseurl }}/exercises/Advanced-queries-join-1-SQL). Remove any records where the `weight` is missing. Save this query as `size_comparison_controls_vs_krat_exclosures`.
