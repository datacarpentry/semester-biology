---
layout: exercise
topic: Loops
title: Multiple Files
language: R
---

This is a follow-up to [stringr]({{ site.baseurl }}/exercises/Loops-stringr-R).

The same colleague wants to scale up their analysis to work on data from the [PATRIC](http://www.patricbrc.org) bacterial phytogenomic database. They want to know the GC content of all of the bacteria in the database and have started working initially 
with just a handful of [archaea](https://en.wikipedia.org/wiki/Archaea). 

Help out by downloading [the data]({{ site.baseurl }}/data/archaea-dna.zip)
and looping over the files to determine the GC content for each file. Once 
downloaded, either unzip the .zip file manually or use the `unzip` function. 

Read the [.fasta files](https://en.wikipedia.org/wiki/FASTA_format) in the unzipped 
folder into R using the [ShortRead package](http://www.bioconductor.org/packages/release/bioc/html/ShortRead.html) in Bioconductor. Start by installing [Bioconductor](http://www.bioconductor.org/install/) with the following code (this may take a
while, so be patient): 

```
source("https://bioconductor.org/biocLite.R")
biocLite("ShortRead")
```

Each fasta file contains one long sequence of DNA for an archaea species. The 
following code loads one sequence file, where `seq` is the variable name for the data 
file:

```
library(ShortRead)
reads <- readFasta("archaea-dna/A-saccharovorans.fasta")
seq <- sread(reads)
```

Use `list.files()`, with `full.names` set to true, to generate a list of the names
of all the sequence files. Then create a for loop that uses the above `seq` code to 
read in each sequence file. When this works, add to the loop a function that 
calculates GC content of each file. You can use the GC content function you wrote for 
[stringr]({{site.baseurl}}/exercises/Loops-stringr-R), but you will have to 
capitalize the “g” and “c” strings in the `str_count` functions because the sequences 
in these files are upper case. Once this is working, create an empty data frame to 
store the output and fill it with values from the for loop, one column with file 
names and the second column with GC contents. 
