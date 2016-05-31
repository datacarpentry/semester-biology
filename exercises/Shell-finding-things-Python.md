---
layout: exercise
topic: Shell
title: Finding Things
language: Python
---

This is a follow-up question to [Pipes and Filters]({{ site.baseurl }}/exercises/Shell-pipes-and-filters-Python).

Your team quickly realizes that since it's going to have lots of data
files it will be better to store them in their own directories to keep
things more organized.

1.  Do an update from the repository using svn update. You should see
    two new folders appear in your main repository folder. Move them
    into the folder you are using for this assignment.
2.  Add a new directory to the directory where you are keeping this code
    called modeldata and then move the current areas.txt files into that
    folder using the subversion command line. Commit the changes.
3.  Modify your shell script so that when it is executed from the main
    project folder (which now has no areas.txt files in it) it finds all
    of the files in the subfolders and returns the full list of areas
    and predicted richnesses for all of the files.

