---
layout: exercise
topic: dplyr
title: Shrub Volume Data Basics
language: R
---

Dr. Granger is interested in studying the factors controlling the size and
carbon storage of shrubs. She has conducted an experiment looking at the effect
of three different treatments on shrub volume at four different locations. She
has placed the data file on the web for you to download:

* [Shrub dimensions data]({{ site.baseurl }}/data/shrub-volume-data.csv)

Download this into your `data` folder and get familiar with the data by
importing it using `read.csv()` and then:

1. Check the column names in the data using the function `names()`.
2. Use `str()` to show the structure of the data frame and its individual 
   columns.
3. Print out the first few rows of the data using the function `head()`.

   *Use `dplyr` to complete the remaining tasks.*
4. Select the data from the length column and print it out.
5. Select the data from the site and experiment columns and print it out.
6. Filter the data for all of the plants with heights greater than 5 and
   print out the result.
7. Create a new data frame called `shrub_data_w_vols` that includes all of the
   original data and a new column containing the volumes, and display it.