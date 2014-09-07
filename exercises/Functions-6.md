---
layout: exercise
title: Functions 6
---

This is a follow up to [Strings 6](/exercises/Strings-6/).

A colleague has produced a file with one DNA sequence on each line. Download
[the file](/data/dna_sequences_1.txt) and load it into Python using
`numpy.loadtxt()`. You will need to use the optional argument `dtype=str` to
tell `loadtxt()` that the data is composed of strings.

Calculate the GC content\* of each sequence by writing a function that takes a
dna sequence as input and returns the GC-content of that sequence. Print the
result for each sequence. Before we knew about functions we had to take each dna
sequence one at a time and then rewrite or copy-paste the same code to analyze
each one. Isn't this better?

\* The GC content is the percentage of bases that are either G or C (as a
percentage of total base pairs).
