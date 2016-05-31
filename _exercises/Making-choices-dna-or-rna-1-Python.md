---
layout: exercise
topic: Making Choices
title: DNA or RNA 1
language: Python
---

Write a function, `dna_or_rna(sequence)`, that determines if a sequence
of base pairs is DNA, RNA, or if it is not possible to tell given the
sequence provided. Since all the function will know about the material is the
sequence the only way to tell the difference between DNA and RNA is that
RNA has the base Uracil (`'u'`) instead of the base Thymine (`'t'`). Have the
function return one of three outputs: `'DNA'`, `'RNA'`, or `'UNKNOWN'`. Use
the function and a `for` loop to print the type of the sequences in the
following list.

```
sequences = ['ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg', 'gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau', 'gaaagcaagaaaaggcaggcgaggaagggaagaagggggggaaacc', 'guuuccuacaguauuugaugagaaugagaguuuacuccuggaagauaauauuagaauguuuacaacugcaccugaucagguggauaaggaagaugaagacu', 'gauaaggaagaugaagacuuucaggaaucuaauaaaaugcacuccaugaauggauucauguaugggaaucagccggguc']
```

*Optional: For a little extra challenge make your function work with both upper
and lower case letters, or even strings with mixed capitalization*
