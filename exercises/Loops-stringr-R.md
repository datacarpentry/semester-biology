---
layout: exercise
topic: Loops
title: stringr
language: R
---

A colleague has produced a file with one DNA sequence on each line. Download
[the file]({{ site.baseurl }}/data/dna-sequences-1.txt). Load it into R with`read.csv()` and name the data frame `sequences`.

Your colleague wants to calculate the GC content of each DNA sequence (i.e., the
percentage of bases that are either G or C) and knows just a little R. They sent
you the following code, which will calculate the GC content for a single
sequence using the `stringr` package:

```
sequence <- "attggc"
num_g <- str_count(sequence, "g")
num_c <- str_count(sequence, "c")
gc_content <- (num_g + num_c) / str_length(sequence) * 100 
```

1. Convert the last three lines of this code into a function to calculate the GC
content of a DNA sequence. Name that function `get_gc_content`.

2. Use a `for` loop and your function to calculate the GC content of each sequence
and store the results in a new data frame using an index. The following code will help you create this data frame:

```
# create an empty data frame with one row for each sequence
gc_contents <- data.frame(gc_content = numeric(nrow(_______)))

# loop over sequences using an index for the row and
# store the output in the new data frame
for (i in 1:nrow(__________)){
  ________[i,] <- get_gc_content(sequences$____[____])
}
```
