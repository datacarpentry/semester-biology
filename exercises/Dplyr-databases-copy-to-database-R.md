---
layout: exercise
topic: dplyr Databases
title: Copy to Database
language: R
---

Dr. Undómiel has decided to focus on the change in size of a few target rodent 
species over the course of the experiment(1977-2002). She has chosen *Dipodymys 
spectabilis*, *Onychomys torridus*, *Perymiscus erimicus*, *Chaetodipus
penicillatus*. 

Write a script that uses `dplyr` to: 

1. Connect to the `portal_mammals.sqlite`.
2. Generate a data frame with `year`, `species_id`, and the average weight per 
   year (`avg_weight`) for each target species. *You may find the `%in% c()`
   construction useful for your `filter()`.*
3. Use `copy_to()` to include your new data frame in `portal_mammals.sqlite`. 
   Call it something informative so that Dr. Undómiel can find it easily. *Make
   sure it remains after the connection is terminated using `temporary = 
   FALSE`.*
  
