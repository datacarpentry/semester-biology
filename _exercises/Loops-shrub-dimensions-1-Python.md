---
layout: exercise
topic: Loops
title: Shrub Dimensions 1
language: Python
---

One of your collaborators has posted
[a comma-delimited text file]({{ site.baseurl }}/data/shrub_dimensions.csv) online for you to
analyze. The file contains dimensions of a series of shrubs (length, width,
height) and they need you to determine the associated volumes. You could do this
using a spreadsheet, but the project that you are working on is going to be
generating lots of these files so you decide to write a program to automate the
process.

Download the data, use `np.loadtxt()` to import it into Python, and then use a
`for` loop to calculate the volumes (`l * w * h`)and return a list the volumes. 
There should be one value in the list for each shrub. Once you have created this 
list, use another for loop to print out each volume on it's own line in a string 
like 'The volume the shrub is 22.5.'
