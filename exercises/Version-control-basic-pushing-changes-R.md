---
layout: exercise
topic: Version Control Basic
title: Pushing Changes
language: R
---

This is a follow up to
[Adding a Remote]({{ site.baseurl }}/exercises/Version-control-basic-adding-a-remote-R).

Now that you've set up your remote repository for collaborating with Dr. Granger
you'd better get to work since she can see everything you're doing.

1. Write a function to calculate the GC-content of a sequence, regardless of the
   capitalization of that sequence. (*Hint: using the function `str_to_lower` or
   `str_to_upper` in the `stringr` package might be useful*). This function
   should also be able to take a vector of sequences and return a vector of
   GC-contents (*it probably does this without any extra work so give it a try*). 
2. Commit this change.
3. Once you've committed the change click the `Push` button in the upper right
   corner of the window and then click `OK` when `git` is done pushing.
4. You should be able to see the changes you made on Github.
5. Email your teacher to let them know that you've finished this exercise.
