---
layout: exercise
topic: Data Frames
title: Database CSV
language: R
---

Throughout this course we will slowly build on integrating database management
with R coding. The first and most basic way to get data from your database into
R is to export it from the database and then import it into R.

[Download a new copy](https://ndownloader.figshare.com/files/2292171)
of the `portal_mammals.sqlite` database. Using the SQLite Manager, write a query
to extract the year of capture, genus, species, and weight of the 500 largest
individuals captured at the site. Save your query as a View and export it to as
a `csv` file using the `Export Wizard`. You can initiate the `Export Wizard` by
clicking on the view's `Structure` tab and choosing `Export` or by selecting
`Export View` from either the `View` menu or the right click menu for the
view. You should check the `First row contains column names` box so that it is
clear what is in your exported file, and save the file as
`500-Largest-Individuals.csv` in your working directory.

Import the `500-Largest-Individuals.csv` file into R and complete the following
tasks:

1. Use `str()` to show the structure of the data frame and its individual columns
2. Use the `unique()` function to print the genus and the species for each
species represented in the 500 largest individuals sampled.
3. Use the `nrow()` and `unique()` functions to determine how many years are
represented in this dataset.
4. Use the `min()` and `max()` functions to check how much smaller (*as a 
percent*) the 500th largest individual is than the largest (i.e., (max - min) /
max * 100).
5. Calculate the average size of a *Neotoma Albigula* in this dataset.
