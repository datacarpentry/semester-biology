---
layout: exercise
topic: Making Choices
title: DNA or RNA
language: R
---

Write a function, `dna_or_rna()`, which takes a `sequence` as an argument, that
determines if a sequence of base pairs is DNA, RNA, or if it is not possible to
tell given the sequence provided. Since all the function will know about the
material is the sequence the only way to tell the difference between DNA and RNA
is that RNA has the base Uracil (`"u"`) instead of the base Thymine (`"t"`). You
can check if a string contains a character (or a longer substring) in R using
`grepl(substring, string)`. Have the function return one of three outputs:
`"DNA"`, `"RNA"`, or `"UNKNOWN"`. Use the function to test each of the following
sequences.

```
seq1 <- "ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg"
seq2 <- "gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau"
seq3 <- "gaaagcaagaaaaggcaggcgaggaagggaagaagggggggaaacc"
```

*Optional: For a little extra challenge make your function work with both upper
and lower case letters, or even strings with mixed capitalization*
