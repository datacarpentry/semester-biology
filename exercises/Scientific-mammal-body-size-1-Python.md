---
layout: exercise
topic: Scientific
title: Mammal Body Size 1
language: Python
---

There were a relatively large number of extinctions of mammalian species
roughly 10,000 years ago. To help understand why these extinctions
happened scientists are interested in understanding whether there were
differences in the body size of those species that went extinct and
those that did not. Since we're starting to get pretty good at this
whole programming thing let's stop messing around with made up datasets
and do some serious analysis.

Download the
[largest dataset on mammalian body size in the world](http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt).
Fortunately this dataset has data on the mass of recently extinct mammals as
well as extant mammals (i.e., those that are still alive today). Take a look at
the [metadata](http://www.esapubs.org/archive/ecol/E084/094/metadata.htm) to
understand the structure of the data. One key thing to remember is that species
can occur on more than one continent, and if they do then they will occur more
than once in this dataset. Also let's ignore species that went extinct in the
very recent past (designated by the word 'historical' in the 'status' column).

Import the data into Python. If you've looked at a lot of data you'll realize
that this dataset is tab delimited. The special character to indicate tab in
Python is `\t`.

To start let's explore the data a little and then start looking at the major question.

1. The following code will determine how many genera (plural of genus) there are
   in the dataset: `len(data.groupby(['genus']))`. Modify this code to determine
   the number of species. Remember that a species is uniquely defined by the
   combination of its genus name and its species name. Print the result to
   the screen. The number should be between 4000 and 5000.
2. Find out how many of the species are extinct and how many are extant, print
   the result to the screen. *Hint: first separate the data into the extinct and
   extant components and then count the number of species*.
3. Find out how many families are present in the dataset.
4. Now print the genus name, the species name, and the mass of the largest and
   smallest species (*note, it is not possible for a mammal to have negative mass*)
5. Now let's get to work. Calculate the average (i.e., mean) mass of an extinct
   species and the average mass of an extant species. The function `mean()`
   should help you here. It is available as both a numpy function and a Pandas
   DataFrame method. Don't worry about species that occur more than once.  We'll
   consider the values on different continents to represent independent data
   points. Print out the the average mass of extant species and the average mass    
   of extinct species.
