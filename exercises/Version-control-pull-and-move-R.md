---
layout: exercise
topic: Version Control
title: Pull and Move
language: R
---

*Version control exercises 6-9 assume that you have an instructor adding and
 modifying files in your repository. If not, the files are available in the
 [`data`](https://github.com/datacarpentry/semester-biology/tree/gh-pages/data) and
 [`code`](https://github.com/datacarpentry/semester-biology/tree/gh-pages/code) directories of
 the course repository.*

You're working on a large project trying to predict diversity hotspots. Another
member of your collaborative team has produced a series of files that contain
lists of areas that resulted from a series of modeling exercises. Each filename
begins with the word area.

Your programmer has whipped up a small R script called `rich_pred.R` that
takes a single file containing a list of areas, one per line, and returns the
area and the predicted richness.

Your team is using version control and all of the relevant files are
in the repository. Navigate to the main working directory for your repository
and update it from the command line using `git pull`. This will place the
necessary files in your main directory. Move the files into the directory you
created for this assignment by using `git mv filename new_location`, `commit`
this change with an appropriate commit message, and `push` them back to the
central repository.
