---
layout: exercise
topic: Loops
title: Shrub Dimensions 2
language: Python
---

This is a follow up to [Shrub Dimensions 1]({{ site.baseurl }}/exercises/Loops-shrub-dimensions-1-Python)

One of your collaborators has posted [a comma-delimited text
file]({{ site.baseurl }}/data/shrub_dimensions.csv)
online for you to analyze. The file contains dimensions of a series of
shrubs (ShrubID, Length, Width, Height) and they need you to determine
their volumes. You could do this using a spreadsheet, but the project
that you are working on is going to be generating lots of these files so
you decide to write a program to automate the process.

Use this function to download the data and then use a for loop to
calculate the volumes and return a list of lists where the first item in
each sublist contains the ShrubID and the second item contains the
volume. There should be one sublist for each ShrubID. Once you have
created this list, use another for loop to print out each combination of
ShrubID and volume on it's own line in a string like 'The volume of
shrub a1 is 22.5.'

Download the data (note that it has a header this time), use `np.loadtxt()` to
import it into Python, and then use a for loop to calculate the volumes and
return a list of lists where the first item in each sublist contains the ShrubID
and the second item contains the volume. There should be one sublist for each
ShrubID. Once you have created this list, use another for loop to print out each
combination of ShrubID and volume on it's own line in a string like 'The volume
of shrub a1 is 22.5.'
