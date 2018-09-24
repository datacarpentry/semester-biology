---
layout: page
element: notes
title: Computational Project Structure
language: R
--- 

### Introduction

* Learn how to organize a computational project
* Many benefits to good organization & documentation
    * Understand all project components
    * Work more efficiently
    * Easier for collaboration
    * Including with your future self
* Save a lot of time & frustration in long run, even if it’s time-consuming and frustrating to do it right initially

### Example project walk-through
Download [example project]({{ site.baseurl }}/data/example_project.zip). 

* Good file structure
    * All project files in one main folder
    * Subfolders (data, R, etc.)
* Main folder is R project
    * Self-contained project
    * Use relative instead of absolute paths
* Good folder & file names
    * Descriptive but not too long
    * No spaces
    * Consistent format
* README
    * Everything someone needs to know to understand project
* Raw data
    * In separate folder from cleaned data
    * Never change!
    * Each file should have metadata
* Scripts with code
    * Relative file paths to read in and create files
    * Lots of comments
    * Order: libraries, data, user-created functions, everything else
    * Good variable & column names
* Two methods to deal with different versions of same file
    * Good = consistent naming scheme
        * Each copy has date or version number
        * Don’t call anything final, cause no file ever is! 
    * Better = version control, only have one copy of each file
* Running all scripts
    * Good = description of order to run each script in README
    * Better = script to run all scripts
    * Best = Make
* Combine code output and text in single document, e.g., knitr

### Goal of good project structure

* Reproducibility = ability to get same results from set of data & code
* Give entire project folder to someone else (or your future self!), they can understand all parts and recreate your results, figures, documents, etc. 
* Improving reproducibility makes YOUR life easier! 
