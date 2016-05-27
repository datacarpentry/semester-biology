---
layout: exercise
topic: Database Structure
title: Redundancy
language: SQL
---

Here's where we tell you that you have been working with a simplified version of the Portal database. (*We're sure that you had suspicions that the data was too clean, anyway*). Download the original [`Plots` table]({{ site.baseurl }}/data/Portal_plots_original.csv) and follow the steps from [Importing Data]({{ site.baseurl }}/exercises/Database-control-importing-data-SQL). Name the `New Database` something like `portal_mammals_original.sqlite`. Then,

**Before starting this problem make sure that you have a backup of your database** In general, when developing a database it's probably 
best to work on a copy that is specifically just for development. Once it's working then apply it to your actual database. *Always, always, backup your databases before messing with them in this manner. 
**Seriously.***

The `Plots` table in this version of the Portal database violates one of the 
major rules of database structure (*the whole gosh dang table is redundant for 
Pete's sake!*). Figure out a better design using one table to link each plot 
number to a single experimental code (save this as `PlotsSingleCode`) and a 
second table that includes various versions of each type of code (save this as 
`Experiments`). Create these tables and add the appropriate data by extracting 
the necessary information from the old table and insert it into the new tables.

Using your new plot related tables write a query that determines the `description` and the `number of plots` of each `plot type`.
