---
layout: page
element: notes
title: Basic Reproducibility
language: R
---

### Introduction to Reproducibility

* Goal - rerun full analysis with a single click (or command)
* First step - Make sure your code runs anywhere
* Important for class - your code has to run the on graders computer
* Important for science
    * next day (who has gotten code working & had it not work the next day?)
	* desktop vs. laptop
	* collaborators
	* advisor

### Make sure things you did before don't matter

* Computers store the results of each command run in sequence
* Change something
* Looks like it still works
* Only works because of something you did earlier in the same session

* Good: Clear R environment using the broom icon on the `Environment` tab.
* Better: Restart R to get a clean environment: `Session` -> `Restart R`
* Run entire file using `Source` button or `Ctrl-Shift-S`
* Makes sure that the code runs fully and produces desired result

### Make sure code works on other computers

* Don't use `setwd()`
    * Use projects and relative paths
    * `data/mydata.csv` not `C:\Users\Batman\DataCarp\data\mydata.csv`
* Write code that works on all operating systems
    * Assume case specificity
	    * Filenames in code should match actual names exactly, including capitalization
	* Use `/` instead of `\` or `\\` in paths

### Use print to show things you want the program to show

* Depending on how your code is run it may show different things
* `Source` without echo will hide most things
* Use the `print` function to print out text you want the person running your
  code to see
* Print out the answers to each homework exercise

### Checklist

* There is an Assignment Turn In Checklist to help
* Show link on main page
