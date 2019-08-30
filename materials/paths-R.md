---
layout: page
element: notes
title: Paths
language: R
---

### Introduction to Paths

* To use data stored on a computer we need to tell R where it is
* This is done using paths
* *Go to data page and download shrub dimensions data to a datacarp directory*
* Paths can be absolute

```
'/home/ethan/datacarp/shrub-dimensions-labeled.csv' # OSX/Linux
'/Users/ethan/datacarp/shrub-dimensions-labeled.csv' # Windows
```

* Folders/Directories are separate by `/` with the file name at the end
* Include the file extension (the part after the `.`)

* Paths can also be relative

```
'datacarp/shrub-dimensions-labeled.csv'
```

* "From where I am the shrub-dimensions file is in the Desktop subdirectory"
* Absolute & relative paths are the same if R thinks it's in `/home/ethan/`

### Find out where you are

* To find out where R is use `getwd()`

```
getwd()
```

* "get working directory"
* The "working directory" is where the program starts from

### Loading data

* For data in the working directory just use the file name

```
shrub_data <- read.csv('shrub-dimensions-labeled.csv')
```

* Download a file into working directory using `download.file()`

* For data not in the working directory - two options
    * tell R where it is
    * change the working directory to where it is
* Changing the working directory is common
    * Who here uses `setwd` regularly?
    * Does that ever cause any issues?
        * Working on a different computer?
        * Working with someone else's files?
* Have working directory automatically set to a common place and use relative paths

### Projects

* Think of each project as a self-contained unit in a single folder/directory
* Treat all locations as relative to that single directory
* To do this in RStudio we use projects
* `File` -> `New Project` -> `New Directory` -> `New Project` -> datacarp
* Or use `Existing Directory` to choose an existing directory
* Creates .Rproj file
    * Isn’t project itself
    * Contains project info
    * Don’t change manually
* Can switch between projects using `File` -> `Recent Projects` or `Open Project`
* Keeps track the state of RStudio when you last worked with that project

> * Create a project for this assignment
> * Do [Exercise 9 - Shrub Volume Data Frame]({{ site.baseurl }}/exercises/Data-frames-shrub-volume-data-frame-R).

### Assignments

* This idea of projects as folders is also important for how we share code
* To turn in assignments you will submit a compressed version of the folder for that assignment
* Demo compressing a folder
* Version control also treats projects as folders

> Assign remaining exercises. Submit as compressed main folder, see [Assignment Submission & Checklist]({{ site.baseurl }}/materials/turn-in-checklist)