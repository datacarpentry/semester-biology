---
layout: exercise
topic: Lists
title: Nested Lists 2
language: Python
---

One of your collaborators has posted [a comma-delimited text
file](http://www.programmingforbiologists.org/sites/programmingforbiologists.org/files/shrub_dimensions.txt)
online for you to analyze. The file contains dimensions of a series of
shrubs (ShrubID, Length, Width, Height) and they need you to determine
their volumes. You could do this using a spreadsheet, but the project
that you are working on is going to be generating lots of these files so
you decide to write a program to automate the process.

The following function will download the text from the web and return it
as a list of lists:

```
def get_file_from_web(url):
    """Download CSV data from web"""
    webpage = urllib.urlopen(url)
    datareader = csv.reader(webpage)
    data = []
    for row in datareader:
        data.append(row)
    return data
```

It requires the use of the urllib and csv modules, so you will need to
import those modules before using the function.

Use this function to download the data and then use a for loop to
calculate the volumes and return a list of lists where the first item in
each sublist contains the ShrubID and the second item contains the
volume. There should be one sublist for each ShrubID. Once you have
created this list, use another for loop to print out each combination of
ShrubID and volume on it's own line in a string like 'The volume of
shrub a1 is 22.5.'
