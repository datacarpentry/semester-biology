---
layout: exercise
topic: R-SQL
title: Export to Database
language: R
---

Dr. Undómiel has decided to focus on the change in size of a few target rodent 
species over the course of the experiment(1977-2002). She has chosen , *Dipodymys spectabilis*, *Onychomys torridus*, *Perymiscus erimicus*, 
*Chaetodipus penicillatus*. 

Write a script that uses R and SQL to: 

1. Connect to the `portal_mammals.sqlite`.
2. Generate a data frame with `year`, `species_id`, and the average weight per 
year (`avg_weight`) for each target species.
3. Use `dbWriteTable()` to include your new data frame in the 
`portal_mammals.sqlite`. Call it something informative so that Dr. Undómiel can 
find it easily.
  
