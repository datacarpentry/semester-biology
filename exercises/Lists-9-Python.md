---
layout: exercise
title: Lists 6
---

This is a follow up to the
[Making Choices 3 problem]({{ site.baseurl }}/exercises/making-choices-3).

Write a function `dna_or_rna_multivalue(list_of_sequences)` that
takes a list of dna sequences as input, determines whether each sequence
is DNA, RNA, or UNKNOWN, and then returns a list of those values (i.e.,
'DNA', 'RNA', 'UNKNOWN') in the same order as the `list_of_sequences`.

I would recommend:

1.  Starting by copying your function from the [Making Choices 3
    problem]({{ site.baseurl }}/exercises/making-choices-3)
    into your current code [you may end up needing to modify the
    function to handle the unfortunate error that somehow crept into the
    list of sequences below]
2.  Calling this function from inside of your new function (yep, you can
    definitely do that) instead of rewriting or copying all of that
    code.
3.  Starting with an empty list to store the output.
4.  Using the the append method.

Use this new function to return the values for the following list of DNA
sequences and then (outside of the function) print the values in the
resulting list, one value per line.

```
list_of_sequences = ['attgcccaat', 'agcuucua', 'attuuccaga',
'ggcccacacgg', 'atattagcc', 'startcodon', 'uucaaggu', 'tttttttttt',
'aaaaaaaaa']
```
