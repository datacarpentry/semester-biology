---
layout: exercise
topic: Loops
title: stringr
language: R
---

A colleague has produced a file with one DNA sequence on each line. Download
[the file]({{ site.baseurl }}/data/dna_sequences_1.txt) and load it into R using 
`read.csv()`. The file has no header.

Your colleague wants to calculate the GC content of each DNA sequence (i.e., the
percentage of bases that are either G or C) and knows just a little R. They sent
you the following code which will calculate the GC content for a single
sequence:

```
library(stringr)

sequence <- "attggc"
Gs <- str_count(sequence, "g")
Cs <- str_count(sequence, "c")
gc_content <- (Gs + Cs) / str_length(sequence) * 100 
```

This code uses the excellent
[`stringr` package](http://cran.r-project.org/web/packages/stringr/stringr.pdf)
for working with the sequence data. You'll need to install this package before
using it.

Convert the last three lines of this code into a function to calculate the GC
content of a DNA sequence.

Use a `for` loop and your function to calculate the GC content of each sequence 
and print them out individually. The function should work on a single sequence 
at a time and the `for` loop should repeatedly call the function and print out 
the result.

*You may have noticed that [for Loop]({{ site.baseurl }}/exercises/Functions-for-loop-R/)
prints the results differently. `read.csv()` imports the data as a
`data.frame()`, unlike the numeric vector in the previous exercise.*
