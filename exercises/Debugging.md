---
layout: exercise
title: Debugging
---

This is a follow up to the [Basic Python 1
problem](/exercises/Basic-python-2).

While you were out of town doing field work over the summer Dr. Granger hired
another student, Gregory Goyle, to help her modify your code so that it did
something a bit different than the original code. The new code was intended to
include more size classes and to output the average GC content for each size
class to a csv file rather than the individual level data. Unfortunately Greg
hasn't learned an important lesson about programming, that it's
[almost always better to work with existing code than to try to rewrite it from scratch](http://www.joelonsoftware.com/articles/fog0000000069.html),
so he figured it would be easier to just start over than to try to understand
what you'd already done. Sadly Greg isn't quite the programmer you are and so
didn't actually finish the project before having to stop to focus on his course
work now that school is back in session (and boy does he need to focus). So,
he's committed the current version of his code to your repository. It has all of
the parts in place, but isn't exactly... well... working just yet.

You don't want to make the same mistake that Greg did and besides, your computer
crashed over the summer and you weren't using version control yet (it's OK, you
didn't know better, it's not your fault), so you'll need to work with Greg's
code, such as it is.  Find the bugs in the code and fix them. You'll need to
both read the code and use a debugger to understand what's going on and fix the
problems. Get the code cleaned up at least up to the point where the code is
actually executuing. You're welcome to find and fix/improve other issues as
well, but you'll also be writing tests later to help you track the tricky
problems down, so the really important thing at this point is to get the code
running so that you can actually run the tests.

Make a new branch for this problem and commit each fix individually.

The code [can be downloaded](/code/buggy_granger_analysis_code.py), but your
instructor may have already put it in your repository.
