---
layout: exercise
topic: Basic Queries
title: Selecting
language: Access
---

For this and many of the following problems you will create queries that
retrieve the relevant information from the Portal small mammal survey data that
you imported in the [Importing Tables problem]({{ site.baseurl }}/exercises/Database-control-importing-tables-Access). You may need to
know more about the database than you currently do in order to answer the
questions. For example, you may need to know what species is associated with the
two character species ID or you may need to know the units for the individual's
weight. This type of information associated with data is called metadata and the
metadata for this dataset is available online at
[Ecological Archives](http://esapubs.org/archive/ecol/E090/118/metadata.htm).

1.  Open the table with the Portal Survey Data that you created in the
    [Importing Tables problem]({{ site.baseurl }}/exercises/Database-control-importing-tables-Access). Click the button at the bottom
    that looks like `>|` to jump to the end of the table. How many records are
    there? If you open the raw data file in Excel how many lines are there? Do
    they match (keeping in mind that one row in the raw data file is the
    headers)? If not then there was an error in your import. You should always
    do some basic santity checks like this one when working with computers to
    make sure that they are doing what you think they are doing.
2.  Write a query that displays all of the records for all of the fields
    in the table. Save it as `All Survey Data`.
3.  We want to generate data for an analysis of body size differences
    between males and females of each species. We have decided that we
    can ignore the information related to when and where the individuals
    were trapped. Create a query that returns all of the necessary
    information, but nothing else. Save this as `Size Differences Among
    Sexes Data`.
