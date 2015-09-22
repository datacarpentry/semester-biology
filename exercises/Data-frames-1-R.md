---
layout: exercise
title: Data Frames 1
subtitle: Shrub Volume Pt 2
language: R
---

This is a follow up to [Vectors 2]({{ site.baseurl }}/exercises/Vectors-2-R)

One of your collaborators has posted [a comma-delimited text
file]({{ site.baseurl }}/data/shrub_dimensions_labeled.csv)
online for you to analyze. The file contains dimensions of a series of
shrubs (ShrubID, Length, Width, Height) and they need you to determine
their volumes (`l * w * h`). You could do this using a spreadsheet, but the 
project that you are working on is going to be generating lots of these files so
you decide to write a program to automate the process.

Download the data, use `read.csv()` to import it into R, and then print out:

1. The lengths as a vector
2. The lengths as a data frame
3. The shrub IDs and widths as a data frame
4. Use `subset()` to get the data records (i.e., rows) for shrubs with heights
   greater than 3
5. The volume of each of the shrubs as a vector
6. The volumes of each of the shrubs in a `data.frame` where the first column
contains the ShrubIDs and the second column contains the volume. Print out the
ShrubID and volume `data.frame`.
