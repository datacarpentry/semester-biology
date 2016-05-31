---
layout: exercise
topic: Loops
title: Improve Your Code
language: Python
---

This is a follow up to [GC Content 2]({{ site.baseurl }}/exercises/Functions-gc-content-2-Python/).

A colleague has produced a file with one DNA sequence on each line. So far
you've been manually extracting each DNA sequence and calculating it's GC
content, which as worked OK with five sequences, but isn't going to work very
well when the sequencer really gets going and you have to handle 100s-1000s of
sequences.

Use a `for` loop and your function from [GC Content 2]({{ site.baseurl }}/exercises/Functions-gc-content-2-Python/) to calculate the 
GC content of each sequence and print them out. The function should work on a 
single sequence at a time and the `for` loop should repeatedly call the function 
and print out the result.
