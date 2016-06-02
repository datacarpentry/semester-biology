---
layout: exercise
topic: Shell
title: Bird Counts 2
language: Python
---

We have data on bird communities that we've collected that we need to
analyze. The data has three columns, a date, a common name, and a count of the
number of individuals.

```
2013-03-22 bluejay 5
2013-03-22 mallard 9
2013-03-21 robin 1
```

Download the data files using the `curl` command:

```
curl -O http://www.programmingforbiologists.org/data/data_drycanyon_2013.txt
curl -O http://www.programmingforbiologists.org/data/data_greencanyon_2013.txt
curl -O http://www.programmingforbiologists.org/data/data_logancanyon_2013.txt
```

We want to count the total number of individuals of each species that were seen
in each data file. We could solve this problem ourselves, but our lab mate has
already written some code that does this.  Instead of rewriting the code
ourselves we can simply add it to a pipeline. Let's go ahead and download the
file:

`curl -O http://www.programmingforbiologists.org/code/species_counts.py`

To run this code we need to tell the shell to run it using python, which we do
by giving it the name of the program that will run it, then the name of our
program, and then the input.

`python species_counts.py data_greencanyon_2013.txt`

This can then be integrated into our pipeline. So if we want to sort based
on the total number of individuals:

`python species_counts.py data_greencanyon_2013.txt | sort -k 2 -n`

This is great for a single datafile with a particular name, but we've been
collecting data on birds from a number of different places and we'd like to
conduct all of these analyese simultaneously. Write a simple for loop that loops
over all of the files in the current directory that have the general form of
`data_*.txt`, prints out the name of the datafile, and then runs
`species_counts.py` on the datafile. Save this in a text file called `all_species_counts.sh`.
