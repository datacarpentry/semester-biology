---
layout: page
element: notes
title: Version Control
language: R
--- 

## Introduction

In a browser:

* http://www.phdcomics.com/comics/archive.php?comicid=1531
* http://www.phdcomics.com/comics/archive.php?comicid=1323

* Who has a directory on their computer with a bunch of filenames like this or
  like this
* Learn how to get rid of folders like this and to track changes to things like
data files and code in a more manageable way.


## Benefits of version control

* Track changes but better
    * Tracks every change ever made in groups called commits
	* Every commit stores the full state of all of your files at that time
    * Never lose anything
	* Easily unbreak your code/data/manuscript
	* No more file name changes
* Collaboration
    * Work on things simultaneously
	* See what changes others have made
	* Everyone has the most recent version of everything

# Version control using RStudio/Git/Github

## Getting started

1. File -> New Project -> New Directory -> Empty Project
2. Choose where to put your project
3. Select `Create a git repository`
4. In the upper right window you'll see a `Git` tab

**Exercise 1**

## First commit

*The following example uses the code from the problem decomposition lecture*

* Create a new file `large-small-ts-analysis.R`
* Add a data import function

```
get_data <- function(){
  data <- read.csv("surveys.csv")
  return(data)
}

data <- get_data()
```

* Git -> Select file *changes in staged files will be included in next commit*
* Commit -> "Start project comparing dynamics of different sized Rodents"
* History: one commit, and see what changes where made

## Building a history

* File doesn't currently show on Git tab; hasn't been changed since last commit
* Add size class function

```
get_size_class <- function(weight){
  if (weight > 50){
    size_class = "large"
  }
  else{
    size_class = "small"
  }
  return(size_class)
}
```

* Save
* Now we see the file and the `M` indicates that it's been modified
* To commit these changes we need to stage the file (check the box)
* Commit -> "Add function for determining size class"
* History: two commits each showing the additions we made in that commit

* Add threshold

```
get_size_class <- function(weight, threshold){
  if (weight > threshold){
    size_class = "large"
  }
  else{
    size_class = "small"
  }
  return(size_class)
}
```

* Stage -> Commit
    * Now we see both red and green sections. Green for lines that have been
      added, red for lines that have been deleted. Git works line by line so if
      you change a line the previous version is shown as deleted and the new
      version as added.


**Exercise 2**

**Setup a Github account and email me your username**

## Remotes

**Draw origin-local figure throughout this section**

* So far we've worked with a local git repository
* One of the big benefits of version control is easy collaboration
* To do this we synchronize our local changes with a remote repository
* We'll use Github, by far the most popular hosted version control site
    * Public and private hosted repositories
    * Private free for students and academics
	* For the assignment we'll use private repositories that I'll make for you

### Add a remote

* Make a new git repository (students have been assigned one)
* Copy remote adding code from Github
* Gear icon -> Shell
* Paste lines from Github -> Enter
* See files on Github
* Show browsing repo in past

**Exercise 5**

### Push to a remote

* Add size classes function

```
add_size_classes <- function(df){
  # Add size class data to a data frame
  # Input: data frame with weight column containing size information
  data_size_class <-
    df %>% 
    na.omit() %>% 
    rowwise() %>% 
    mutate(size_class = get_size_class(weight, 50))
  return(data_size_class)
}
```

* Commit
* Show on local not remote
* Push
* Show on remote

**Exercise 6**

**Partner quietly pushes the following code**

```
get_size_class_ts_data <- function(df){
  # Convert individual data to time-series data for each of a set of size classes
  # Input: data frame with a year column for time
  #        and a size_class column
  ts_data <-
    df %>% 
    group_by(year, size_class) %>% 
    summarize(counts = n())
  return(ts_data)
}

plot_ts_data <- function(df){
  #Plot time-series data by size class
  # Input: data frame with year, size_class, and counts columns
  ggplot(df, aes(x = year, y = counts, color = size_class)) +
    geom_line()
}
```

### Collaborating

* Big advantage to remotes is easy collaboration
* Avoids emailing/dropboxing files and never being sure of most recent version
* Makes it easy to see what collaborators have done
* While I've been talking one of my collaborators has finished adding the other
functions we need

* Pull
* Show history
* Run code


**Exercise 7**
