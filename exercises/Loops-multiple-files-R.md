---
layout: exercise
topic: Loops
title: Multiple Files
language: R
---

A colleague wants to do a comparitive analysis of the GC content (i.e., the
percentage of bases in a DNA sequence that are either G or C) on data from the
[PATRIC](http://www.patricbrc.org) bacterial phytogenomic database. They want to
know the GC content of all of the bacteria in the database and have started
working initially with a handful of
[archaea](https://en.wikipedia.org/wiki/Archaea). They know a little R and wrote
the following code to load a single sequence and caculate it's GC content.

```
library(ShortRead)
library(Biostrings)

reads <- readFasta("archaea-dna/A-saccharovorans.fasta")
seq <- sread(reads)
base_freq <- alphabetFrequency(seq)
gc_content <- (base_freq[1, "G"] + base_freq[1, "C"]) / sum(base_freq) * 100
```

The first two lines load a [.fasta file](https://en.wikipedia.org/wiki/FASTA_format)
using the [ShortRead package](http://www.bioconductor.org/packages/release/bioc/html/ShortRead.html)
in Bioconductor. The second two lines determine the frequency of all of the bases in sequence and then
calculate the GC content.

Start by installing [Bioconductor](http://www.bioconductor.org/install/)
with the following code (this may take a while, so be patient):

```
source("https://bioconductor.org/biocLite.R")
biocLite("ShortRead")
biocLite("Biostrings")
```

Each fasta file contains one long sequence of DNA for an archaea species. The 
following code loads one sequence file, where `seq` is the variable name for the data 
file:

```
library(ShortRead)
reads <- readFasta("archaea-dna/A-saccharovorans.fasta")
seq <- sread(reads)
```

Help out your colleagues by downloading
[the data]({{ site.baseurl }}/data/archaea-dna.zip) and looping over the files
to determine the GC content for each file. Once downloaded, either unzip the
.zip file manually or use the `unzip` function.

Use `list.files()`, with `full.names` set to true, to generate a list of the
names of all the sequence files. Then create a for loop that uses the above code
to read in each sequence file and calculate it's GC content. Store the resulting
values in a data frame with one column with file names and a second column with
GC contents.
