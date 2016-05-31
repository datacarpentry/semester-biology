---
layout: exercise
topic: Loops
title: Multiple Files
language: R
---

This is a follow-up to [stringr]({{ site.baseurl }}/exercises/Loops-stringr-R).

Dr. Jekyll is hard at work to perfect his serum and correct the imbalance with 
his alter ego, Mr. Hyde. Dr. Jekyll is convinced that some mutation in his DNA 
is responsible for his transformations and he's looking in the [PATRIC](http://www.patricbrc.org) 
bacterial phytogenomic database for clues. He wants to know the GC content of 
all of the bacteria in the database and got started working with a handful of 
[archaea](https://en.wikipedia.org/wiki/Archaea). Sadly, his skill with a burner and pipette has not prepared him at 
all for work on a computer.

Help him out by downloading [the data]({{ site.baseurl }}/data/archaea_dna.zip)
and looping over the files to determine the GC content for each file. Unzip the
the .zip file into your `data` directory. If you look at the data you'll see
that it's made up of one file per species using the [FASTA dna sequence format](https://en.wikipedia.org/wiki/FASTA_format). We 
could try to load using `read.csv`, but the [ShortRead package in Bioconductor](http://www.bioconductor.org/packages/release/bioc/html/ShortRead.html) 
already exists for parsing fasta files, so we'll use that instead. [Install Bioconductor](http://www.bioconductor.org/install/) if 
you haven't already. 

```
source("https://bioconductor.org/biocLite.R")
biocLite("ShortRead")
```

The following code will then load a single sequence file:

```
library(ShortRead)
reads <- readFasta("data/archaea_dna/A-saccharovorans.fasta")
seq <- sread(reads)
```

You can reuse the GC content function you wrote for
[stringr]({{site.baseurl}}/exercises/Loops-stringr-R) to calculate the GC content, but
you might need to modify it to accommodate the different capitalization of the
bases.

Each file in the zip represents a single archaea species. Use a `for` loop and
your function to calculate the GC content of each file and print them out
individually. You might find the `list.files()` function useful for working with
multiple files in a `for` loop. The function should work on a single file at a
time and the `for` loop should repeatedly call the function and store the
results in a data frame with a row for each file and columns for both the file
name and GC content.

*Optional*: For a little extra challenge change your answer so that instead of
 printing out the file names it prints out the species name that is encoded in
 the file name, but without the `.fasta` at the end.
