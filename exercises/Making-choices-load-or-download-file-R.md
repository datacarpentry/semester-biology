---
layout: exercise
topic: Making Choices
title: Load or Download File
language: R
---

With large data files it can be useful to only download the file if it hasn't
already been downloaded. One way to do this is to check if the file name exists
in your working directory. If it does then load it, if not then download it. You
can use the `list.files()` function to get a lit of files and directories in the
working directory and the `download.file(url, filename)` function to download
the file at a `url` to a specific `filename`.

1. Write a conditional statement that checks if `surveys.csv` exists in the
   working directory, downloads it from
   <https://ndownloader.figshare.com/files/2292172> using if it is not, loads the file
   into a data frame and displays the first few rows using the `head()`
   function.

2. Make a version of this conditional statement that is a function, where the
   name of the file is the first argument and the link for downloading the file
   is the second argument. The function should return the resulting data frame.
   Add some documentation to the top of the function describing what it does.
   Call this function using "species.csv" as the file name and
   <https://ndownloader.figshare.com/files/3299483> as the link. Print the first
   few rows of the resulting data frame using `head()`.
