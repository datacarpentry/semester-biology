---
layout: exercise
topic: Combining Basics
title: Shrub Volume
language: Python
---

Dr. Granger is interested in studying the factors controlling the size and
carbon storage of shrubs. This research is part of a larger area of research
trying to understand carbon storage by plants. She has conducted a small
preliminary experiment looking at the effect of three different treatments on
shrub volume at four different locations. She wants to conduct a preliminary
analysis of these data to include in a grant proposal and she would like you to
conduct the analysis for her (she might be a world renowned expert in carbon
storage in plants, but she sure doesn't know much about computers). She has
placed a data file on the web for you to
[download]({{ site.baseurl }}/data/shrub_volume_experiment.csv).

You might be able to do this analysis by hand in Excel, but Dr. Granger seems to
always get funded meaning that you'll be doing this again soon with a much
larger dataset. So, you decide to write a script so that it will be easy to do
the analysis again.

Write a Python script that:

- Imports the data using `numpy`. It has a header row so you'll need to tell
   `numpy.loadtxt()` to ignore it by providing the optional argument
   `skiprows=1`.
- Loops over the rows in the dataset
- Uses a `for` loop to check each row in the dataset, groups by height as 
`'tall'` `if (height > 5)`, `'medium'` `if (2 <= height < 5)`, or `'short'` `if (height < 2)`, 
and determines the total amount of carbon in the shrub. 

   The total amount of carbon is equal to 
   `1.8 + 2 * log(volume)` where `volume` is the volume of the shrub (`length * width * height`).
- Stores this information as table in a nested list (i.e., a list that contains
   a bunch of lists, with each of these sub-lists holding the results for one
   shrub) where the first column has the experiment number, the second column
   contains the string `'tall'`, `'medium'` or `'short'` depending on the height of
   the shrub, and the third column contains the shrub carbon.
- Exports this table to a `csv` (*comma delimited text*) file titled
   `shrubs_experiment_results.csv`.
- Use functions to break the code up into manageable pieces. 

To help you get started here is a function for exporting the results to a CSV
file. To use it you'll need to copy and paste it into your code. It uses the
`csv` module so you'll need to remember to import it.

```
def export_to_csv(data, filename):
    """Export list of lists to comma delimited text file"""
	outputfile = open(filename, 'wb')
	datawriter = csv.writer(outputfile)
	datawriter.writerows(data)
	outputfile.close()
```

*Optional: If you'd like to test your skills a little more, try: 1. Adding a
 header row to you output file; and 2. Determining the average carbon in a shrub
 for each of the different experiments and printing those values to the screen.*
