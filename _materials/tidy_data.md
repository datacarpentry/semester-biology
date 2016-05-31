---
layout: page
element: notes
title: Tidy Database Structure
language: R
--- 

## Multiple tables

* It is often not efficient to include all information of interest in a single
table.

![Table with redundant information](databases_redundant_table.png)

* To solve these problems we store data in multiple tables
* And connect the data in different tables using Joins or Relationships (hence
  "relational" database)
* Each table contains a single data type

![Restructuring a redundant table into two](databases_redundant_table_restructure.png)

## Alternative structures

Cross-tablulated data

![Cross-tabulated data table](databases_crosstab_table.png)

![Cross-tab table restructure](databases_crosstab_restructured.png)

