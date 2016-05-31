---
layout: exercise
topic: Scientific
title: Mammal Body Size 1
language: R
---

There were a relatively large number of extinctions of mammalian species
roughly 10,000 years ago. To help understand why these extinctions
happened scientists are interested in understanding whether there were
differences in the body size of those species that went extinct and
those that did not.

To address this question we can use the
[largest dataset on mammalian body size in the world](http://www.esapubs.org/archive/ecol/E084/094/#data),
which has data on the mass of recently extinct mammals as well as extant mammals
(i.e., those that are still alive today). Take a look at the
[metadata](http://www.esapubs.org/archive/ecol/E084/094/metadata.htm) to
understand the structure of the data. One key thing to remember is that species
can occur on more than one continent, and if they do then they will occur more
than once in this dataset. Also let's ignore species that went extinct in the
very recent past (designated by the word `"historical"` in the `status`
column).

Import the data into R. If you've looked at a lot of data you'll realize
that this dataset is tab delimited. Use the argument `sep = "\t"` in 
`read.csv()` to properly format the data. There is no header row, so use `head = FALSE`.

Add column names to help identify columns.
 
```
colnames(mammal_sizes) <- c("continent", "status", "order", 
"family", "genus", "species", "log_mass", "combined_mass", 
"reference")
```

To start let's explore the data a little and then start looking at the major question.

1. The following `dplyr` code will determine how many genera (*plural of genus*) are
   in the dataset:
   ```
   nrow(distinct(select(mammal_sizes, genus)))

   ```
   Modify this code into a function to determine the number of species. 
   Remember that a species is uniquely defined by the combination of its 
   genus name and its species name. Print the result to the screen. The number 
   should be between 4000 and 5000.
2. Find out how many of the species are extinct and how many are extant, print
   the result to the screen. *HINT: first separate the data into the extinct and
   extant components and then count the number of species*.
3. Print out how many families are present in the dataset.
4. Now print the genus name, the species name, and the mass of the largest and
   smallest species (*note, it is not possible for a mammal to have negative mass.*)
5. Calculate the average (i.e., mean) mass of an extinct species and the 
   average  mass of an extant species. The function `mean()` should help you here. 
   Don't worry about species that occur more than once. We'll consider 
   the values on different continents to represent independent data points.    
   Print out the results for extinct then extant.
