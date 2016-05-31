---
layout: exercise
topic: Shell
title: Pipes and Filters
language: Python
---

You're working on a large project trying to predict [diversity
hotspots](http://en.wikipedia.org/wiki/Biodiversity_hotspot). Another
member of your collaborative team has produced a series of files that
contain lists of areas that resulted from a series of modeling
exercises. Each filename begins with the word `area`.

Your programmer has whipped up a small python script called
`rich_pred.py` that takes a single file containing a list of areas,
one per line, and returns the area and the predicted richness based on
the functions and approach given in the [Species Area Relationship]({{ site.baseurl }}/exercises/Higher-order-functions-species-area-relationship-1-Python) problem.

Your team is, [of
course](https://web.archive.org/web/20100722082534/http://stackoverflow.com/questions/132520/good-excuses-not-to-use-version-control),
using version control and all of the relevant files are in the
repository. Navigate to the main working directory for your repository
and update it from the command line using svn update. This will place
the necessary files in your main directory. Move the files into the
directory you created for this assignment by either using `svn move
filename new_location`or by right clicking on the file in SmartSVN and
selecting Move.

Your job is to take all of these files, run them through the python code
and produce a single list of the areas and associated richness
predictions from all of the sites combined. This list should be sorted
from the smallest area to the largest area, should only include unique
values, and should be stored to a file called
`predicted_diversities.txt`. You could cut and paste the files
together, run them through the Python code, and then do some post
processing to get the list looking right, but new files are going to be
showing up constantly, and besides, this can be readily accomplished in
one line using the shell. Once you've figured out the necessary shell
commands put them in a text file and save it as
`predict_richness.sh`. Test to make sure everything is working by
running it using the command `bash predict_richness.sh`. Commit the
new shell program and the resulting data file to the repository.

**Email me when you are done with this problem so that I can update your
repository for Problem 3.**

*Optional*: Modify your own code from the [Species Area Relationship]({{ site.baseurl }}/exercises/Higher-order-functions-species-area-relationship-1-Python) problem.
to create your own version of `rich_pred.py` instead of using the one
in the repository. One easy way to deal with stdin is to use
[fileinput.input()](http://docs.python.org/library/fileinput.html). Move
the equations back into the body of the code so that it's just a single
self-contained unit. Overwrite the version of `rich_pred.py` from the
repository and commit the new version.
