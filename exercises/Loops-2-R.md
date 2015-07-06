---
layout: exercise
title: Loops 2
subtitle: Shrub Volume Pt 1
language: R
---

One of your collaborators has posted
[a comma-delimited text file]({{ site.baseurl }}/data/shrub_dimensions.csv) 
online for you to analyze from an urban shrub survey of yew [*Taxus baccata*](https://en.wikipedia.org/wiki/Taxus_baccata). 
The file contains canopy dimensions of each shrub (length, width, height) and 
they need you to determine the associated volumes, which is easy because these 
urban shrubs are conveniently rectangular. You could calculate volume using a 
spreadsheet, but the project that you are working on is going to be generating 
lots of these files so you decide to write a program to automate the process.

Download the data, using `read.csv(…, head = FALSE)` to import it into R, 
and then calculate the volumes `l * w * h` in a new vector using vector algebra. 
There should be one value in the vector for each shrub. Once you 
have created this vector, use a `for` loop to print out each volume in order 
on its own line.
