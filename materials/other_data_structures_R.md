---
layout: page
element: notes
title: Other Data Structures
language: R
---

> Remind students to [Install Bioconductor](http://www.bioconductor.org/install/).

> Remember to downloade [*E. coli* genome data]({{ site.baseurl }}/data/ecoli_coding.fasta)
 
> Set up R console:

```
source("https://bioconductor.org/biocLite.R")
biocLite("ShortRead")
library("ShortRead")
```
 
## Lists

Lists are generic vectors that can hold other things.

```
sites <- c("a", "b", "c")
notes <- "It was a good day in the field today. Warm, sunny, lots of gators"
helpers <- 4
field_notes <- list(sites, notes, helpers)
field_notes[1]
field_notes[[1]]
```

We can also give the values names:

```
field_notes <- list(sites=sites, notes=notes, helpers=helpers)
field_notes$sites
field_notes$helpers
```

## Objects 

* The several data structures that we've looked at so far are objects. 
    * `vector()`
    * `data.frame()`
    * `list()`
* We can also make arbitrary objects that store whatever kinds of
data we need.

### Bioconductor

* As an example we'll briefly look at Bioconductor, which is used for working 
with genomic data in R.

I've downloaded data on the coding regions of the *E. coli* genome from
[Genbank](http://www.ncbi.nlm.nih.gov/) in a format called `FASTA`, which is one
format used for storing nucleotide sequences.

```
reads <- readFasta("data/ecoli_coding.fasta")
reads
```

This tells us that `reads` is it's own special kind of object called a
`ShortRead`.

`str(read)`

Using `str` we can see that inside this object are other kinds of objects,
including something called `DNAStringSet`, which holds groups of sequences.

```
reads@sread
reads@sread@ranges
reads@sread@ranges@start
```

We can use functions to access and work with pieces of these objects.

```
sequences <- sread(reads)
sequences
sequences[1]
```

These kinds of objects can then be used with special functions designed to work
with specific kinds of data.

```
firstseq <- sequences[[1]]
reverse(firstseq)
complement(firstseq)
reverseComplement(firstseq)
alphabetFrequencies(firstseq)]
translate(firstseq)
```

* **Someone has probably already written it. See if you can use their work.**
* Parsing and manipulating data is hard to get right in all cases, it's best to
  rely on existing tools to handle this when possible

```
reverse(sequences)
complement(sequences)
reverseComplement(sequences)
```
