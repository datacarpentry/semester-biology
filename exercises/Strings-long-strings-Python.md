---
layout: exercise
topic: Strings
title: Long Strings
language: Python
---

For the DNA sequence below determine the following properties and print them to
the screen (*you can cut and paste the following into your code, it's a lot
longer than you can see on the screen, but just select the whole thing and when
you paste it into Python you'll see what it looks like*):

`dna='ttcacctatgaatggactgtccccaaagaagtaggacccactaatgcagatcctgtgtgtctagctaagatgtattattctgctgtggatcccactaaagatatattcactgggcttattgggccaatgaaaatatgcaagaaaggaagtttacatgcaaatgggagacagaaagatgtagacaaggaattctatttgtttcctacagtatttgatgagaatgagagtttactcctggaagataatattagaatgtttacaactgcacctgatcaggtggataaggaagatgaagactttcaggaatctaataaaatgcactccatgaatggattcatgtatgggaatcagccgggtctcactatgtgcaaaggagattcggtcgtgtggtacttattcagcgccggaaatgaggccgatgtacatggaatatacttttcaggaaacacatatctgtggagaggagaacggagagacacagcaaacctcttccctcaaacaagtcttacgctccacatgtggcctgacacagaggggacttttaatgttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcggcagtctgaggattccaccttctacctgggagagaggacatactatatcgcagcagtggaggtggaatgggattattccccacaaagggagtgggattaggagctgcatcatttacaagagcagaatgtttcaaatgcatttttagataagggagagttttacataggctcaaagtacaagaaagttgtgtatcggcagtatactgatagcacattccgtgttccagtggagagaaaagctgaagaagaacatctgggaattctaggtccacaacttcatgcagatgttggagacaaagtcaaaattatctttaaaaacatggccacaaggccctactcaatacatgcccatggggtacaaacagagagttctacagttactccaacattaccaggtaaactctcacttacgtatggaaaatcccagaaagatctggagctggaacagaggattctgcttgtattccatgggcttattattcaactgtggatcaagttaaggacctctacagtggattaattggccccctgattgtttgtcgaagaccttacttgaaagtattcaatcccagaaggaagctggaatttgcccttctgtttctagtttttgatgagaatgaatcttggtacttagatgacaacatcaaaacatactctgatcaccccgagaaagtaaacaaagatgatgaggaattcatagaaagcaataaaatgcatgctattaatggaagaatgtttggaaacct'`

1. How many occurrences of `'gagg'` occur in the sequence?
2. What is the starting position of the first occurrence of `'atta'`?
   *Report the actual base pair position as a human would understand it.*
3. How long is the sequence?
4. What is the GC content of the sequence? The GC content is the percentage of
   bases that are either G or C (as a percentage of total base pairs) Print the
   result as "The GC content of this sequence is XX.XX%" where XX.XX is the
   actual GC content. Do this using a [formatted string](https://docs.python.org/2/library/string.html).
