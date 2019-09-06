---
layout: page
element: notes
title: Basic Reproducibility
language: R
---

> Make sure that `Tools` -> `Global Options` -> `General` ->
> `Save workspace to ~/.RData on exit` is set to the default `Ask`

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

> * Start new project
> * Create data subdirectory
> * Use `Right Click` -> `Save Link As` to download Portal surveys & species data

```r
data_mammals <- read.csv('data/surveys.csv')
avg_mass <- mean(data_mammals$weight, rm.na = TRUE)
```

* You then go to add the species data and realize that `data` probably isn't
  descriptive enough

```r
data_surveys <- read.csv('data/surveys.csv')
avg_mass <- mean(data_mammals$weight, rm.na = TRUE)
data_species <- read.csv('data/species.csv')
```

* And you rerun all of your code and everything works
* But will it work after I restart R?
  * No, because the code doesn't create `data` anymore
  * Read through code

* Clear R environment using the broom icon on the `Environment` tab.
  * Doesn't unload packages
  * Useful when developing code
* Restart R to get a clean environment: `Session` -> `Restart R`
  * Does unload packages
  * Useful for making sure everything works
* Run entire file using `Source` button or `Ctrl-Shift-S`
* Makes sure that the code runs fully and produces desired result

* Stop R from storing the state of the environment
* When you close RStudio it will often ask if you want to save your workspace
* *Start to close RStudio*
* *Show Save dialog*
* If you do this is will get reloaded when you start R, even when you restart it
  as described above
* Stop this by `Tools` -> `Global Options` -> `General` ->
  `Save workspace to ~/.RData on exit` -> `Never`
* Unclick `Restore .RData into workspace at startup` 

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

### Clean up extra code

* Remove experiments from your code
* Remove `install.packages()` lines from your code
  * Avoid reinstalling packages on other peoples computers
  * If you really want to keep it comment it out

### Checklist

* There is an Assignment Turn In Checklist to help
* Show link on main page
