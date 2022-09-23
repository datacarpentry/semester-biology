---
layout: page
element: notes
title: Paths
language: R
---

### (optional) If Using RStudio Cloud

* So far in this course we've been using RStudio Cloud and placing data files where R knows to find them for you
* Working with data files on your own computer is a little more complicated
* But in this lesson we'll learn how to do this effectively

### Introduction to Paths

* To use data stored on a computer we need to tell R where it is
* This is done using paths
* This is a description of the directories where our files are stored
* Let's go to the course website and download some data
* https://datacarpentry.org/semester-biology/materials/datasets
* This page contains all of the data we use in class
* Download Shrub Dimensions data
* If we click on this link it will download, but where did it download to
* Click on the arrow to 'Show in Folder'
* The details will look different depending on the operating system
* But, generally, across the top you'll see the folder that things are stored in

* Go back to RStudio
* If we try to load this data just using it's filename it won't work

```r
data = read.csv("shrub-dimensions-labeled.csv")
```

* Returns the error "Cannot open file", "No such file or directory"
* That's because it can't find the file where we've tried to load it from


* Paths can be either relative or absolute
* We'll start with absolute, which always describes exactly where something is on the computer
* Data file is stored in the `Downloads` subdirectory of our `Home` directory
* `Home` directory varies by operating system
* On mac and Linux it is `/home/username`
* Within that is the `Downloads` directory

```r
data = read.csv('/home/ethan/datacarp/shrub-dimensions-labeled.csv') # OSX/Linux
```

* This successfully loads the data because we've told it exactly where the file is
* On Windows change `home` to `Users`

```r
data = read.csv('/Users/ethan/datacarp/shrub-dimensions-labeled.csv') # Windows
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

* This is a relative path, because the file is in the working directory the only remaining piece is the name

* One way to ensure that a file is in the working directory is to download it using `download.file()`

* For data not in the working directory there are two options
    * tell R where it is
    * change the working directory to where it is
* Changing the working directory is common
    * Who here uses `setwd` regularly?
    * Does that ever cause any issues?
        * Working on a different computer?
        * Working with someone else's files?
* In general, using `setwd` means that your code will only work on a single computer
* That's bad, so we want to have the working directory automatically and use relative paths

### Projects

* The simplest way to do this is using RStudio Projects

* (RStudio Cloud) In fact we've already been using them
* (RStudio Cloud) Every time you click on an assignment or click `New Project` this creates a new project

* Each project is a self-contained unit of work in a single folder/directory
* Treat all locations as relative to that single directory
* To do this in regular RStudio we use projects
* `File` -> `New Project` -> `New Directory` -> `New Project` -> datacarp
* Or use `Existing Directory` to choose an existing directory
* Creates .Rproj file
    * Isn’t project itself
    * Contains project info
    * Don’t change manually
* Can switch between projects using `File` -> `Recent Projects` or `Open Project`
* Keeps track the state of RStudio when you last worked with that project

### Sharing code

* This idea of projects as folders is also important for how we share code
* Version control, which we'll have the opportunity to learn about later, works with the projects as folder structure
* We can also zip a the project folder and send it to someone else and they can work with it
