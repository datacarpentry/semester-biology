---
layout: exercise
topic: Tests
title: Test the Code
language: R
---

This is a follow up to [Debug the Code]({{ site.baseurl }}/exercises/Debugging-debug-the-code-R).

Write tests for your 'Debug the Code' code for the following cases and save it in a 
file called `Tests-R.R`. Make corrections/improvements to the 'Debug the Code' code 
so that all of your tests pass.

`test_that("get_gc_content() works",`

1.  on a sequence represented by upper case string.
2.  on a sequence represented by lower case string.
3.  on a sequence represented by mixed case string.
4.  on a sequence represented by multiline string.

In an email accompanying your "updated" code, Dr. Morales indicated that
the specifications for the earlength size classes were:

1.  extralarge: earlength >= 15
2.  large: 10 <= earlength < 15
3.  medium: 8 <= earlength < 10
4.  small: earlength < 8

`test_that("get_size_class() works",`

1.  for each case when the numbers are in the range,
2.  for the edgecases of 8, 10, and 15,
3.  but the function fails if non-numerical values are input as an argument
    (e.g., a string from a header row that didn't get removed).
