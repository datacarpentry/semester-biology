---
layout: exercise
title: Data Frames 2
subtitle: Extract Data from a Database
language: R
---

This is a follow-up to the [SQL Sorting]({{ site.baseurl }}/exercises/Sql-sorting) problem.

Throughout this course we will slowly build on integrating database management with R coding. The first step is figuring one way to get data from your database into R.

Connect to your `portal_mammals.sqlite` database using the SQLite Manager. 
Choose your `100 Largest Individuals` view and export it to .CSV using the 
`Export Wizard`. You may need to initiate the `Export Wizard` by choosing 
`Export View` from the `View` dropdown menu. The defaults provided in the 
`Export Wizard` should give us what we need, so click `OK` and save the file as 
`100-Largest-Individuals.csv` in your working directory.

Import the `100-Largest-Individuals.csv` file and complete the following tasks:

1. Use the `unique()` function to determine how many species are represented in 
the 100 largest individuals sampled.
2. Use the `unique()` function to determine how many years are represented in 
the 100 largest individuals sampled.
3. Use the `min()` and `max()` functions to check how much smaller (*as a 
percent*) the 100th largest individual is than the largest.
