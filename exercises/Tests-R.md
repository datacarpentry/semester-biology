---
layout: exercise
title: Tests
language: R
---

This is a follow up to the [Debugging problem]({{ site.baseurl }}/exercises/Debugging-R).

Write tests for your 'Debugging' code for the following cases and save it in a 
file called `Tests-R.R`. Make corrections/improvements to the 'Debugging' code 
so that all of your tests pass.

#### gc_content()

1.  Sequence represented by upper case string
2.  Sequence represented by lower case string
3.  Sequence represented by mixed case string
4.  Sequence represented by multiline string

#### get_size_class()

In an email accompanying your "updated" code, Dr. Granger indicated that
the specifications for the earlength size classes were:

1.  extralarge: earlength >= 15
2.  large: 10 <= earlength < 15
3.  medium: 8 <= earlength < 10
4.  small: earlength < 8

Write tests to check:

1.  That each case is working when the numbers are in the range
2.  The edgecases of 8, 10, and 15
3.  The function fails if non-numerical values are input as an argument
    (e.g., a string from a header row that didn't get removed)
