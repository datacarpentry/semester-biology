---
layout: exercise
title: Loops 3
subtitle: Shrub Volume Pt 2
language: R
---

This is a follow up to [Loops 2]({{ site.baseurl }}/exercises/Loops-2-R)

One of your collaborators has posted [a comma-delimited text
file]({{ site.baseurl }}/data/shrub_dimensions_labeled.csv)
online for you to analyze. The file contains dimensions of a series of
shrubs (ShrubID, Length, Width, Height) and they need you to determine
their volumes `l * w * h`. You could do this using a spreadsheet, but the 
project that you are working on is going to be generating lots of these files so
you decide to write a program to automate the process.

Download the data (note that it has a header this time), use `read.csv()` to
import it into R, and then calculate the volumes in a data.frame where the first 
column contains the ShrubIDs and the second column contains the volume. Use a 
`for` loop to print out each combination of ShrubID and volume.
