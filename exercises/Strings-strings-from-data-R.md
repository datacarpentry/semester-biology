---
layout: exercise
topic: Strings
title: Strings from Data
language: R
---

A colleague has produced a file with one DNA sequence on each
line. Download [the file]({{ site.baseurl }}/data/dna-sequences-1.txt)
and load it into R using `read_delim()`. The file has no header and is
separated by white space (`""`).

Calculate the GC content of each sequence. The GC content is the
percentage of bases that are either G or C (as a percentage of total
base pairs).  Print each GC content in order to the screen (in %).
