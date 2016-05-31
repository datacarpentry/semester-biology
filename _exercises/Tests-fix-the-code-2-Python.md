---
layout: exercise
topic: Tests
title: Fix the Code 2
language: Python
---

This is a follow up to [Fix the Code 1]({{ site.baseurl }}/exercises/Debugging-fix-the-code-1-Python).

Write tests for your `Fix the Code 1` code for the following cases and
save it in a file called `test_granger_analysis_code.py` (*remember that
the file has to start with `test_` for nose to find it*). Make any
corrections/improvements that need to be made to the code so that all of
your tests pass.

**gc_content()**

1.  Sequence represented by upper case string
2.  Sequence represented by lower case string
3.  Sequence represented by mixed case string
4.  Sequence represented by multiline string

**get_size_class()**

In an email accompanying your "updated" code, Dr. Granger indicated that
the specifications for the earlength size classes were:

1.  extralarge: earlength >= 15
2.  large: 10 <= earlength < 15
3.  medium: 8 <= earlength < 10
4.  small: earlength < 8

Write tests to check:

1.  That each case is working when the numbers are in the range
2.  The edge cases of 8, 10, and 15
3.  What happens if non-numerical values are passed to the function
    (e.g., a string from a header row that didn't get removed)
