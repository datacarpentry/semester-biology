---
layout: exercise
title: Loops 2
subtitle: stringr
language: R
---

A colleague has produced a file with one DNA sequence on each line. Download
[the file]({{ site.baseurl }}/data/dna_sequences_1.txt) and load it into R using 
`read.csv()`. The file has no header.

Write a function to calculate the GC content of a DNA sequence. The GC content 
is the percentage of bases that are either G or C (as a percentage of total base 
pairs). You'll want to use the `str_count()` function from the 
[`stringr` package](http://cran.r-project.org/web/packages/stringr/stringr.pdf) to find the number of Gs and Cs in each sequence. You'll 
notice in the documentation that `str_count()` requires two arguments, a 
`string` and a `pattern`. In our case, the `string` is the DNA sequence and the 
`pattern` is a string of either `"G"` or `"C"`. *Note: It is important that you 
count Gs and Cs separately for the function to work properly.* `str_length()` will give you the length of the DNA sequence you'll need for the divisor of your 
percentage calculation. 

Use a `for` loop and your function to calculate the GC content of each sequence 
and print them out individually. The function should work on a single sequence 
at a time and the `for` loop should repeatedly call the function and print out 
the result.

*You may have noticed that [Functions 5]({{ site.baseurl }}/exercises/Functions-5-R/) prints the results differently. `read.csv()` imports the data as a `data.frame()`, unlike the numeric vector in the previous exercise.*