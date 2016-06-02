---
layout: exercise
topic: Basic Queries
title: SELECT
language: SQL
---

For this and many of the following problems you will create queries that 
retrieve the relevant information from the Portal small mammal survey database. 
As you begin to familiarize yourself with the database you will need to know 
some details regarding what is in this database in order to answer the 
questions. For example, you may need to know what species is associated with the 
two character species ID or you may need to know the units for the individual's weight. This type of information associated with data is called metadata and the 
metadata for this dataset is available online at [Ecological Archives](http://esapubs.org/archive/ecol/E090/118/metadata.htm).

1.  Write a query that displays all of the records for all of the fields (`*`)
    in the main table. Save it as a view named `all_survey_data`.
2.  We want to generate data for an analysis of body size differences
    between males and females of each species. We have decided that we
    can ignore the information related to when and where the individuals
    were trapped. Create a query that returns all of the necessary
    information, but nothing else. Save this as 
    `size_differences_among_sexes_data`.

