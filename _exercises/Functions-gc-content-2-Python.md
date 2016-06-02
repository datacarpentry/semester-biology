---
layout: exercise
topic: Functions
title: GC Content 2
language: Python
---

This is a follow up to [GC Content 1]({{ site.baseurl }}/exercises/Strings-gc-content-1-Python/).

A colleague has produced a file with one DNA sequence on each line. Download
[the file]({{ site.baseurl }}/data/dna_sequences_1.txt) and load it into Python using
`numpy.loadtxt()`. You will need to use the optional argument `dtype = str` to
tell `loadtxt()` that the data is composed of strings.

Write a function to calculate GC content. GC content is the percentage of bases 
that are either G or C as a percentage of total base pairs. Your function should 
take a dna sequence as input and return the GC-content of that sequence. Print 
the result for each sequence. 

*Before we knew about functions we had to take each dna sequence one at a time 
and then rewrite or copy-paste the same code to analyze each one. Isn't this 
better?*
