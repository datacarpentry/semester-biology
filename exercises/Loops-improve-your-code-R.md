---
layout: exercise
topic: Loops
title: Improve Your Code
language: R
---

This is a follow up to [String Data]({{ site.baseurl }}/exercises/Functions-string-data-R/).

A colleague has produced a file with one DNA sequence on each line. So far
you've been manually extracting each DNA sequence and calculating it's GC
content, which as worked OK with five sequences, but isn't going to work very
well when the sequencer really gets going and you have to handle 100s-1000s of
sequences.

Use a `for` loop and your function from [String Data]({{ site.baseurl }}/exercises/Functions-string-data-R/) to
calculate the GC content of each sequence and print them out. The function
should work on a single sequence at a time and the `for` loop should repeatedly
call the function and print out the result.
