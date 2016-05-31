---
layout: exercise
topic: Tests
title: Refactor
language: Python
---

This is a follow up to the [Fix the Code 2 problem]({{ site.baseurl }}/exercises/Tests-fix-the-code-2-Python).

Now that you've got the code working it's time to deal with the fact that it's
not really well structured (I mean, has this guy not heard of NumPy or Pandas or
what), but before messing with working code let's write a regression test. This
test will make sure that the code still does the same thing it did before we
started.

The problem is that all of the important code that needs refactoring is
outside of functions at the bottom of the script. So,

1.  Move the bulk of this code into one of more functions
2.  Write a test that executes the main function using StringIO to make
    example data
3.  Make sure it is doing what you expect
4.  Refactor the portion of the code that gets the average values of gc
    content for each size class to use Numpy or Pandas.
5.  Rerun your tests to make sure that both the regression test and the
    unit tests still pass
