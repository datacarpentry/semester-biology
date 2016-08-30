---
layout: page
element: notes
title: Other Data Structures
language: R
---

> Remind students to [install Bioconductor](http://www.bioconductor.org/install/).

> Remember to download [Archaea genome data]({{ site.baseurl }}/data/archaea-dna.zip).
 
> Set up R console:

```
source("https://bioconductor.org/biocLite.R")
biocLite("ShortRead")
library(ShortRead)
```
 
### Lists

* Lists are generic vectors that can hold other things.

```
sites <- c("a", "b", "c")
notes <- "It was a good day in the field today. Warm, sunny, lots of gators."
helpers <- 4
field_notes <- list(sites, notes, helpers)
field_notes[1]
field_notes[[1]]
```

* We can also give the values names.

```
field_notes <- list(sites=sites, notes=notes, helpers=helpers)
field_notes$sites
field_notes[["sites"]]
```

### Objects 

* Data structures are defined in R as `class()` and stored in `objects()`. 
    * `vector()`
        * `"character"` 
        * `"integer"` 
        * `"numeric"`
    * `data.frame()`
        * `"data.frame"`
    * `list()`
        * `"list"`
* We can also make arbitrary objects that store whatever kinds of
data we need.
    * Genome sequences
    * Geographical information
    * Evolutionary trees

### Bioconductor

* [Bioconductor](http://www.bioconductor.org/) is software for bioinformatics, that includes `ShortRead` 
for working with genomic data in R.

* We're using genomic data from [Genbank](http://www.ncbi.nlm.nih.gov/).
    * Archaea genome
    * Coding regions
    * `.FASTA`
        * Format stores nucleotide sequences

```
reads <- readFasta("data/archaea_dna/T-pendens.fasta")
```

* `reads` is a special kind of object class, `ShortRead`.

```
reads
```

* The `str()` of `ShortRead` includes other kinds of objects.
    * Object access:
        * using the `@` operator
        * `ShortRead` functions
    * `"DNAStringSet"` holds groups of sequences
        * `@sread` 
        * `sread()`

```
str(reads)

reads@sread
reads@sread[[1]]

reads@sread@ranges
reads@sread@ranges@start

sread(reads)
```

* Managing and manipulating complex data structures
    * Hard to get right in all cases 
    * Best to rely on existing tools
    * Someone has probably already developed a tool for your data structure.
* Other useful `ShortRead` functions

```
reverse(reads@sread)
complement(reads@sread)
reverseComplement(reads@sread)
alphabetFrequency(reads@sread)
translate(reads@sread)
```

> Assign [Exercise 6 - Multiple Files]({{ site.baseurl }}/exercises/Loops-multiple-files-R).
