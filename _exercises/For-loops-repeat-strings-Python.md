---
layout: exercise
topic: For Loops
title: Repeat Strings
language: Python
---

[Microsatellite's](http://en.wikipedia.org/wiki/Microsatellite_%28genetics%29)
are short sequences of DNA (2-6 bases) that are repeated sequencially in
the genome. For example, a common microsatellite is the pair of bases
(CA)~n~ where n is the number of repeats, so (CA)~10~would be the
sequence CACACACACACACACACACA. These microsatellites are used as genetic
markers in many types of genetic analyses including those associated
with kinship studies and population biology, because they tend to have
high levels of inter- and intra-specific polymorphism.

Write a function that takes two lists as input: one list that contains a
list of the sequences being repeated and another list that contains the
number of times each of those sequences is repeated. Have the function
return a list of the full sequences represent by each pair of values
(sequence and number of repeats). For example, if you passed the
function the following lists:

sequences = ['CA', 'ATTA']

repeats = [10, 2]

it should return:

['CACACACACACACACACACA', 'ATTAATTA']

Use this function to determine the full sequences for the following
lists:

sequences = ['CA', 'ATTA', 'TCTTAG', 'AAGA', 'CG', 'CGAGC']

repeats = [10, 2, 5, 7, 20, 6]

And then (outside of the function) print the values in the returned list
to the screen, one sequence per line.
