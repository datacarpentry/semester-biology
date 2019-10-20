---
layout: exercise
topic: Making Choices
title: DNA or RNA
language: R
---

Write a function that determines if a sequence of base pairs is DNA, RNA, or if
it is not possible to tell given the sequence provided. RNA has the base Uracil
(`"u"`) instead of the base Thymine (`"t"`), so sequences with u's are RNA,
sequences with t's are DNA, and sequences with neither are unknown.

You can check if a string contains a character (or a longer substring) in R
using `grepl(substring, string)`, so `grepl("u", sequence)` will check if the
string in the `sequence` variable has the base `u`.

Name the function `dna_or_rna()` and have it take `sequence` as an argument.
Have the function return one of three outputs: `"DNA"`, `"RNA"`, or `"UNKNOWN"`.
Add documentation describing what the function does. Call the function on each
of the following sequences.

```
seq1 <- "ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg"
seq2 <- "gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau"
seq3 <- "gaaagcaagaaaaggcaggcgaggaagggaagaagggggggaaacc"
```

*Challenge (**optional**)*: Figure out how to make your function work with both
upper and lower case letters, or even strings with mixed capitalization*
