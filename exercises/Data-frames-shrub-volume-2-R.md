---
layout: exercise
topic: Data Frames
title: Shrub Volume 2
language: R
---

This is a follow up to [Shrub Volume 1]({{ site.baseurl }}/exercises/Vectors-shrub-volume-1-R).

One of your collaborators has posted [a comma-delimited text
file]({{ site.baseurl }}/data/shrub_dimensions_labeled.csv)
online for you to analyze. The file contains dimensions of a series of
shrubs (ShrubID, Length, Width, Height) and they need you to determine
their volumes (`l * w * h`). You could do this using a spreadsheet, but the 
project that you are working on is going to be generating lots of these files so
you decide to write a program to automate the process.

Download the data, use `read.csv()` to import it into R, and then use the `$` operator to print out:

1. The shrub lengths
2. The volume of each of the shrubs
