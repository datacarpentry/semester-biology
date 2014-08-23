---
layout: exercise
title: Numpy 1
---

There were a relatively large number of extinctions of mammalian species
roughly 10,000 years ago. To help understand why these extinctions
happened scientists are interested in understanding whether there were
differences in the body size of those species that went extinct and
those that did not. Since we're starting to get pretty good at this
whole programming thing let's stop messing around with made up datasets
and do some serious analysis.

-   Download the [largest dataset on mammalian body size in the
    world](http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt).
    Fortunately this dataset has data on the mass of recently extinct
    mammals as well as extant mammals (i.e., those that are still alive
    today). Take a look at the
    [metadata](http://www.esapubs.org/archive/ecol/E084/094/metadata.htm)
    to understand the structure of the data. One key thing to remember
    is that species can occur on more than one continent, and if they do
    then they will occur more than once in this dataset. Also let's
    ignore species that went extinct in the very recent past (designated
    by the word 'historical' in the 'status' column).
-   Import the data into Python. If you've looked at a lot of data
    you'll realize that this dataset is tab delimited. The special
    character to indicate tab in Python is “\\t”
-   To start let's explore the data a little
    -   Find out how many species are in this massive dataset and print
        the result to the screen
        -   If the value you see is over 5000 (which is more than the
            total number of mammal species) remember that species can
            occur more than once in the dataset. You might want to look
            at a function in numpy called unique.
    -   Find out how many of the species are extinct and how many are
        extant, print the result to the screen
    -   Find out how many genera are present in the dataset
    -   Now print the names and mass of the largest and smallest species
        (note, it is not possible for a mammal to have negative mass ;)
-   Now let's get to work. Calculate the average (i.e., mean) mass of an
    extinct species and the average mass of an extant species and print
    them to the screen. There is a numpy function that should help you
    here as well. Don't worry about species that occur more than once.
    We'll consider the values on different continents to represent
    independent data points.
-   Does it look like there's a difference in size between the species
    that went extinct and those that didn't?
