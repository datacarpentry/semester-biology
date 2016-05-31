---
layout: exercise
topic: Making Choices
title: GC Content 3
language: Python
---

As part of the [GC Content 2]({{ site.baseurl }}/exercises/Functions-gc-content-2-Python) problem you wrote a function to calculate the 
GC-content of a DNA sequence. Improve this function by making two additions/
changes to it:

1.  Allow the function to handle both lower case and upper case
    sequences
2.  If the number of bases in the DNA sequence is less than 100 have the
    function also print the following string: "Warning: The sequence is
    less than 100 base pairs long and therefore the calculated GC
    content may not accurately reflect that of the the broader region of
    the genome."

Use this function to print the output for the following sequences:

a. `ctgccctgcccctggagggtggccccaccggccgagacag`

b. `ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA`

c. `ccctgcccctggagggtctgccctgcccctggagggtctgccctgcccctggagggtctgccctgcccctggagggtctgccctgcccctggagggttgc`

d. `CTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG`
