---
layout: page
element: notes
title: Basic Reproducibility
language: R
---

### Setup

> Make sure that `Tools` -> `Global Options` -> `General` ->
> `Save workspace to ~/.RData on exit` is set to the default `Ask`

### Introduction to Reproducibility

* Goal - rerun full analysis with a single click (or command)
* First step - Make sure your code runs anytime and anywhere
  * next day (who has gotten code working & had it not work the next day?)
	* desktop vs. laptop
	* collaborators
	* advisor

### Make sure things you did before don't matter

* Computers store the results of each command run in sequence
* Change something
* Looks like it still works
* Only works because of something you did earlier in the same session

### Clearing environments and restarting R

* Clear R environment using the broom icon on the `Environment` tab.
  * Doesn't unload packages
  * Useful when developing code
* Restart R to get a clean environment
  * Unloads packages
  * But won't clear environment by default (at least not on Posit Cloud)
* Safest thing is to both clear the environment and restart R
* Then run the entire file using `Source with Echo` button or `Ctrl-Shift-S`
* Ensures that the code runs fully and produces desired result
* Last required exercise of every assignment will walk you through this process

### Stop R from storing the state of the environment

* When you close RStudio it will often ask if you want to save your workspace
* *Start to close RStudio*
* *Show Save dialog*
* Or on Posit Cloud it will just do this automatically
* If you do this is will get reloaded when you start R, even when you restart it
  as described above
* Stop this by `Tools` -> `Global Options` -> `General` ->
  `Save workspace to ~/.RData on exit` -> `Never`
* Unclick `Restore .RData into workspace at startup`

* Only reason not to do this is to if you are performing long running calculations as one step in a process
* Better solution is to save the results of those calculations and then reload them when needed

### Make sure code works on other computers

* Don't use `setwd()`
    * Use projects and relative paths
    * `data/mydata.csv` not `C:\Users\Batman\DataCarp\data\mydata.csv`
* Write code that works on all operating systems
    * Filenames in code should match actual names exactly, including capitalization
    * Use `/` instead of `\` or `\\` in paths

### Clean up extra code

* Remove experiments from your code
* Or at least comment them out
* Remove `install.packages()` lines from your code
* Avoid reinstalling packages repeatedly

### Checklist

* There is an Assignment Turn In Checklist to help
* Show link on main page
