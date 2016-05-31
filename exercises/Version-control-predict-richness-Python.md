---
layout: exercise
topic: Version Control
title: Predict Richness
language: Python
---

This is a follow up question to
[Pull and Move]({{ site.baseurl }}/exercises/Version-control-pull-and-move-Python).

Your job is to take all of these files, run them through the python code and
produce a single list of the areas and associated richness predictions from all
of the sites combined. This list should be sorted from the smallest area to the
largest area, should only include unique values, and should be stored to a file
called `predicted_diversities.txt`. You could cut and paste the files together,
run them through the Python code, and then do some post processing to get the
list looking right, but new files are going to be showing up constantly, and
besides, this can be readily accomplished in one line using the shell. You could
use a loop, but since you just need a single list of areas and predictions it's
probably easier to just use `cat` to concatenate all of the files at the
beginning. Once you've figured out the necessary shell commands put them in a
text file and save it as `predict_richness.sh`. Test to make sure everything is
working by running it using the command bash `predict_richness.sh`. Commit the
new shell program and the resulting data file to the repository.
