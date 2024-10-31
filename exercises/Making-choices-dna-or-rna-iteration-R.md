---
layout: exercise
topic: Making Choices
title: DNA or RNA Iteration
language: R
---

This is a follow-up to [DNA or RNA]({{ site.baseurl }}/exercises/Making-choices-dna-or-rna-R).

Write a function, `dna_or_rna(sequence)`, that determines if a sequence
of base pairs is DNA, RNA, or if it is not possible to tell given the
sequence provided. Since all the function will know about the material is the
sequence the only way to tell the difference between DNA and RNA is that
RNA has the base Uracil (`"u"`) instead of the base Thymine (`"t"`). Have the
function return one of three outputs: `"DNA"`, `"RNA"`, or `"UNKNOWN"`.

Copy and paste the following sequence data into your script:

```
sequences = c("ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg", "gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau", "gaaagcaagaaaaggcaggcgaggaagggaagaagggggggaaacc", "guuuccuacaguauuugaugagaaugagaguuuacuccuggaagauaauauuagaauguuuacaacugcaccugaucagguggauaaggaagaugaagacu", "gauaaggaagaugaagacuuucaggaaucuaauaaaaugcacuccaugaauggauucauguaugggaaucagccggguc")
```

1. Use the function you wrote and a `for` loop to create a vector of sequence types for the values in `sequences`
2. Use the function and a `for` loop to create a data frame that includes a column of sequences and a column of their types
3. Use the function and `sapply` to create a vector of sequence types for the values in `sequences`
4. Use the function, and `dplyr` to create a data frame that inclues a column of sequences and a column of their types

*Optional: For a little extra challenge make your function work with both upper
and lower case letters, or even strings with mixed capitalization*
