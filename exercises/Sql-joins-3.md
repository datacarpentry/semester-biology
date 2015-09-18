---
layout: exercise
title: Joins 3
subtitle: JOIN Control vs Krat
language: SQL
---

We want to do an analysis comparing the size of individuals on the control plots
to the Long-term Krat Exclosures. Write a query that returns the `year`,
`genus`, `species`, `weight` and the `plot_type` for all cases where the plot
type is either `Control` or `Long-term Krat Exclosure`. Be sure to choose only
rodents and exclude individuals that have not been identified to genus as in
[Joins 1]({{ site.baseurl }}/exercises/Sql-joins-1). Remove any records where
the `weight` is missing. Save this query as `Size Comparison Controls vs. LT
Krat Exclosures`.
