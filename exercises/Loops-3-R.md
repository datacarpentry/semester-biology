---
layout: exercise
title: Loops 3
subtitle: Multiple Files
language: R
---

This is a follow-up to [Loops 2]({{ site.baseurl }}/exercises/Loops-2-R).

Dr. Jekyll is hard at work to perfect his serum and correct the imbalance with 
his alter ego, Mr. Hyde. Dr. Jekyll is convinced that some mutation in his DNA 
is responsible for his transformations and he's looking in the [PATRIC](www.patricbrc.org) 
bacterial phytogenomic database for clues. He wants to know the GC content of 
all of the bacteria in the database and got started working with a handful of 
[archaea](https://en.wikipedia.org/wiki/Archaea). Sadly, his skill with a burner and pipette has not prepared him at 
all for work on a computer. He's managed to find a help forum that you watch 
and shared the data for [download]({{ site.baseurl }}/data/archea_dna.zip). You're just a sucker for mysterious 
characters with a programming problem and decide to help.

Modify the GC content function from [Loops 2]({{ site.baseurl }}/exercises/Loops-2-R) to accommodate the [FASTA dna 
sequence format](https://en.wikipedia.org/wiki/FASTA_format) in which Dr. Jekyll provided his data. Each file represents a 
single archaea species. FASTA files have no header and a single line for 
comments that you'll want to `skip`, followed by multiple lines of DNA bases. 
Use a `for` loop and your function to calculate the GC content of each file and 
print them out individually. You might find the `list.files()` function useful 
for working with multiple files in a `for` loop. The function should work on a 
single file at a time and the `for` loop should repeatedly call the function and 
print out the result as a vector of species name (*extracted from the file 
name*) and GC content.