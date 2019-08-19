---
layout: exercise
topic: Data Frames
title: Shrub Volume Data Frame
language: R
---

This is a follow up to [Shrub Volume Vectors]({{ site.baseurl }}/exercises/Vectors-shrub-volume-vectors-R).

One of your collaborators has posted [a comma-delimited text file]({{
site.baseurl }}/data/shrub-dimensions-labeled.csv) online for you to analyze.
The file contains dimensions of a series of shrubs (shrubID, length, width,
height) and they need you to determine their volumes
(`length * width * height`). You could do this using a spreadsheet, but the
project that you are working on is going to be generating lots of these files so
you decide to write a program to automate the process.

Download the data, use `read.csv()` to import it into R, and use it to produce the following information:

1. A vector of shrub lengths
2. A vector of the volume of each of the shrubs
3. A data frame with just the shrubID and height columns
4. A data frame with the second row of the full data frame
5. A data frame with the first 5 rows of the full data frame