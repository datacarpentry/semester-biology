---
layout: exercise
topic: Loops
title: stringr
language: R
---

A colleague has produced a file with one DNA sequence on each line. Download
[the file]({{ site.baseurl }}/data/dna-sequences-1.txt) and load it into R using 
`read.csv()`. The file has no header. Name the resulting data frame `sequences`.

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

1. Convert the last three lines of this code into a function to calculate the GC
content of a DNA sequence. Name that function `get_gc_content`.

2. Use a `for` loop and your function to calculate the GC content of each
sequence and store the results in a new vector. The function should work on a
single sequence at a time and the `for` loop should repeatedly call the function
and store the output.

3. Use a `for` loop and your function to calculate the GC content of each sequence
and store the results in a new data frame. To do this you'll need to use an
`index` to loop over the rows of the data frame.

    Fill in the following `for` loop to complete this exercise:

```
# pre-allocate the memory with one row for each sequence
gc_contents <- data.frame(gc_content = numeric(nrow(_______)))

# loop over sequences using an index for the row and
# store the output in gc_contents
for (i in 1:nrow(__________)){
  ________[i,] <- get_gc_content(sequences[____])
}
```
