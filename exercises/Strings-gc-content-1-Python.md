---
layout: exercise
topic: Strings
title: GC Content 1
language: Python
---

A colleague has produced a file with one DNA sequence on each line. Download
[the file]({{ site.baseurl }}/data/dna_sequences_1.txt) and load it into Python using
`numpy.loadtxt()`. You will need to use the optional argument `dtype = str` to
tell `loadtxt()` that the data is composed of strings.

Calculate the GC content of each sequence. The GC content is the percentage of
bases that are either G or C (as a percentage of total base pairs). Print the
result for each sequence as "The GC content of the sequence is XX.XX%" where
XX.XX is the actual GC content.
