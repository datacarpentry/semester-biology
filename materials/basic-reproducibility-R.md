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

> * Start new project
> * Create data subdirectory
> * Use `Right Click` -> `Save Link As` to download Portal surveys & species data

```r
data_mammals <- read.csv('data/surveys.csv')
avg_mass <- mean(data_mammals$weight, rm.na = TRUE)
```

* You then go to add the species data and realize that `data_mammals` probably isn't
  descriptive enough

```r
data_surveys <- read.csv('data/surveys.csv')
avg_mass <- mean(data_mammals$weight, rm.na = TRUE)
data_species <- read.csv('data/species.csv')
```

* And you rerun all of your code and everything works
* But will it work after I restart R?
  * No, because the code doesn't create `data_mammals` anymore
  * Read through code

* Clear R environment using the broom icon on the `Environment` tab.
  * Doesn't unload packages
  * Useful when developing code
* Restart R to get a clean environment: `Session` -> `Restart R`
  * Does unload packages
  * Useful for making sure everything works
  * As long is it doesn't secretly reload things
* Run entire file using `Source` button or `Ctrl-Shift-S`
* Makes sure that the code runs fully and produces desired result

* Stop R from storing the state of the environment
* When you close RStudio it will often ask if you want to save your workspace
* *Start to close RStudio*
* *Show Save dialog*
* Or on RStudio Cloud it will just do this automatically
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
	  * Filenames in code should match actual names exactly, including capitalization
	  * Use `/` instead of `\` or `\\` in paths

### Clean up extra code

* Remove experiments from your code
* Remove `install.packages()` lines from your code
* Avoid reinstalling packages repeatedly

### Checklist

* There is an Assignment Turn In Checklist to help
* Show link on main page
