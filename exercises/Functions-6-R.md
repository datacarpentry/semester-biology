---
layout: exercise
title: Functions 6
language: R
---

This is a follow up to [Strings 6]({{ site.baseurl }}/exercises/Strings-6-R/).

A colleague has produced a file with one DNA sequence on each line. Download
[the file]({{ site.baseurl }}/data/dna_sequences_1.txt) and load it into R using
`read.csv()`. The file has no header.

Write a function to calculate GC content. GC content is the percentage of bases 
that are either G or C as a percentage of total base pairs. Your function should 
take a dna sequence as input and return the GC-content of that sequence. Print 
the result for each sequence. Before we knew about functions we had to take each 
dna sequence one at a time and then rewrite or copy-paste the same code to 
analyze each one. Isn't this better?

NB: You may have noticed that [Functions 5]({{ site.baseurl }}/exercises/Functions-5/) prints the results differently. `read.csv()` imports the data as a `data.frame()`, unlike the numeric vector in the previous exercise.
