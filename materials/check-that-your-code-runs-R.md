---
layout: page
element: notes
title: Check That Your Code Runs
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
  * But won't clear environment by default (at least on Posit Cloud)
* Safest thing is to both clear the environment and restart R
* Then run the entire file using `Source with Echo` button or `Ctrl-Shift-S`
* Ensures that the code runs fully and produces desired result
* Last required exercise of every assignment will walk you through this process

### Force R to clear environment when restarting

* `Tools` -> `Global Options` -> `General` ->
  `Save workspace to ~/.RData on exit` -> `Never`
* Unclick `Restore .RData into workspace at startup`

### Check every assignment

* To reinforce this important step in coding the last required exercise each week is the check that your code runs
* *Show last exercise of first assignment*
* This will remind you to check that everything is running and fix any issues
* It will also make grading much easier because when we run your code it will run
* At the start of the semester if the code doesn't run when we go grade we'll send message you on Canvas and give you a chance to fix it before grading
