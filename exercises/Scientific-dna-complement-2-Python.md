---
layout: exercise
topic: Scientific
title: DNA Complement 2
language: Python
---

Download the file
[sequence_data_complete.txt](http://www.programmingforbiologists.org/sites/programmingforbiologists.org/files/sequence_data_complete.txt)
from the website. This file consists of three columns separate by
commas: 1) A sequence ID (like the primary keys we've using in our
database work); 2) The length of the sequence; and 3) The sequence
itself as a string. Import the file into a Numpy array (using
genfromtxt). Use a for loop to print the following statement for each
row of the datafile:

The complement of Sequence ID **sequence_id** is **complement**. This
sequence is **sequence_length** bases long.

Use the complement function you wrote for the [DNA Complement 1
problem]({{ site.baseurl }}/exercises/Lists-dna-complement-1-Python) to
determine the value of **complement**. **Bold** words indicate that you
should substitute the actual value in place of the word so that an
example sentence looks like:

The complement of Sequence ID 20 is taaccggtgga. This sequence is
11 bases long.
