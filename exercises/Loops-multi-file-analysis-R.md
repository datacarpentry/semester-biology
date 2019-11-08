---
layout: exercise
topic: Loops
title: Multi-file Analysis
language: R
---

You have a satellite collars on a number of different individuals and want to be able to quickly look at all of their recent movements at once.
The data is posted daily to a [url as a zip file]({{ site.baseurl }}/data/individual_collar_data.zip) that contains one csv file for each individual: [{{ site.baseurl }}/data/individual_collar_data.zip]({{ site.baseurl }}/data/individual_collar_data.zip)
Start your solution by:

* Downloading the zip file using `download.file`
* Unziping it using `unzip`
* Obtaining a list of all of the files with file names matching the pattern `"collar-data-.*.txt"`

1. Use a loop to load each of these files into R and make a line plot (using `geom_path`) for each file with `long` on the `x` axis and `lat` on the `y` axis.
Graphs, like other types of output, won't display inside a loop unless you explicitly display them, so you need put your `ggplot` command inside a `print` statement.
Include the name of the file in the graph as the graph title using `labs`.

2. Add code to the loop to calculate the minimum and maximum latitude in the file, and store these values, along with the name of the file, in a data frame.
When you create the empty data frame you'll need to include `stringsAsFactors = FALSE` to prevent the `character` column for the file name becoming a `factor`.
Show the data frame as output.

If you're interested in seeing another application of for loops, [check out the code]({{ site.baseurl }}/code/Data-simulation-for-loops-multi-file-analysis) used to simulate the data for this exercise using for loops. 
