---
layout: exercise
topic: Regular Expressions
title: List the Rodents 2
language: Python
---

This is a follow up to the [List the Rodents 1 problem]({{ site.baseurl }}/exercises/Regular-expressions-list-the-rodents-1-Python).

Once you figured out how to extract the latin binomials from a Wikipedia
page that, to be generous, wasn't exactly the most consistently formated
thing you'd ever seen before, you realize that your Python Kung Fu has
gotten pretty strong over the last few months*. So, you decide to push
yourself a little harder and see how far you can get with this Wikipedia
rodent list in another hour or two. Instead of getting just the latin
binomial for each species you decide to also get the family so that each
line of the results is family, genus, species (we don't care about sub
families, sub genera, etc.). And, because transfering things between
databases and programming languages using text files is for rookies,
novices, and newbs, you decide to skip the whole `csv` thing and move all
of the resulting information straight into an SQLite database.

When you're done with this assignment, commit the raw data file and the
Python code to your repository. There's no need to commit the database
because your code will create it when executed.

*Note: It is not uncommon for this type of programming euphoria driven
confidence and excitement to be brutally shattered by the very next
thing you try... so...*
