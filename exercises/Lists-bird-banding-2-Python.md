---
layout: exercise
topic: Lists
title: Bird Banding 2
language: Python
---

This is a follow up to the [Bird Banding 1]({{ site.baseurl }}/exercises/Lists-bird-banding-1-Python) problem.

While conducting the above analyses you realize that a couple of counts
are really high (if you actually noticed this; nice job!), so you go
back to the raw datasheets and discover that the values for site number
27 (count = 900) and site number 59 (count = 600) are typos. Whoever
entered the data actually hit the zero key twice when they should have
only hit it once, so the numbers should actually be 90 and 60. **Use a
Python command to replace the erroneous values with the correct values
(i.e., don't just change them by hand).**

While you are looking through the raw datasheets you also notice that
your field crew has forgotten to enter a whole stack of datasheets.
Sigh, make a mental note to "discuss" your crews data entry habits with
them tomorrow, and then create a new list with the missing data:

unentered\_sites = [27, 24, 16, 9, 23, 39, 102, 0, 14, 3, 9, 93, 64]

Now, combine your new list with the corrected version of
number\_of\_birds (these new sites are entered in order starting at the
end of the previous list) and then (re)answer the following questions.

1.  What is the total number of birds counted across all of the sites?
2.  What is the largest number of birds counted?
3.  What is the smallest number of birds counted?
4.  What is the average number of birds seen at a site?

