---
layout: exercise
topic: Functions
title: String Data
language: R
---

This is a follow up to [Strings from Data]({{ site.baseurl }}/exercises/Strings-strings-from-data-R/).

A colleague has produced a file with one DNA sequence on each line. Download
[the file]({{ site.baseurl }}/data/dna-sequences-1.txt) and load it into R using
`read_csv()`. The file has no header.

Write a function to calculate GC content. GC content is the percentage of bases 
that are either G or C as a percentage of total base pairs. Your function should 
take a dna sequence as input and return the GC-content of that sequence. Print 
the result for each sequence. 

*Before we knew about functions we had to take each dna sequence one at a time and then rewrite or copy-paste the same code to analyze each one. Isn't this better?*

*You may have noticed that [for Loop]({{ site.baseurl }}/exercises/Functions-for-loop-R/) prints the results differently. `read_csv()` imports the data as a `data.frame()`, unlike the numeric vector in the previous exercise.*
