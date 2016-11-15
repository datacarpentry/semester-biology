---
layout: page
element: notes
title: Version Control
language: R
--- 

> Remind students to setup a GitHub account and email the instructor their
> username.

> Arrange to have a teaching partner attend class and `push` the following code 
> for the 'Collaborating' demo.

> **Students need 2 projects to follow along with live coding.**
> **Must switch projects when shifting from live coding to exercises**

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
  # Plot time-series data by size class
  # Input: data frame with year, size_class, and counts columns
  ggplot(df, aes(x = year, y = counts, color = size_class)) +
    geom_line()
}
```

> Open the following links in a browser and zoom in to make the images fill the screen.
>
> > * [Like this?](http://www.phdcomics.com/comics/archive.php?comicid=1531)
> > * [Or like this?](http://www.phdcomics.com/comics/archive.php?comicid=1323)

## Introduction

### Motivation

* Who has a directory on their computer with a bunch of filenames
    * [Like this?](http://www.phdcomics.com/comics/archive.php?comicid=1531)
    * [Or like this?](http://www.phdcomics.com/comics/archive.php?comicid=1323)
* Get rid of messy folders and track changes to things like
data files and code in a more manageable way.


### Benefits of version control

* Track changes (*but better*)
    * Tracks every change ever made in groups called commits
        * Every commit stores the full state of all of your files at that time
    * Never lose anything
        * Revert or restore to any commit
        * Easily unbreak your code/data/manuscript
        * No more file name changes
* Collaboration
    * Work on things simultaneously
        * See what changes others have made
        * Everyone has the most recent version of everything

## Version control using RStudio & Git

### Getting started

1. File -> New Project -> New Directory -> Empty Project
2. Choose where to put your project.
3. Select `Create a git repository`.
4. Check to make sure you have a you have a `Git` tab in the upper right window.

#### Tell git who you are

* Click on gear icon
* Select `Shell`

```
git config --global user.name 'Ethan White'
git config --global user.email 'ethan@weecology.org'
git config --global --list
```

> Do [Exercise 1 - Set-up Git]({{ site.baseurl }}/exercises/Version-control-basic-set-up-git-R/).

### First commit

*The following example uses the code from the problem decomposition lecture.*

* Create a new file. 
    * `large-small-ts-analysis.R`
* Add some code to the file.
    * `get_data()`

```
get_data <- function() {
  data <- read.csv("surveys.csv")
  return(data)
}

data <- get_data()
```

* Git -> Select `large-small-ts-analysis.R`. 
    * Changes in staged files will be included in next commit.
    * Can also see changes by selecting `Diff`
* Commit with message. 
    * `"Start project comparing dynamics of different sized rodents"`
* History: 
    * One commit
    * See what changes where made

### Building a history

* `large-small-ts-analysis.R` doesn't currently show on the `Git` tab
    * No saved changes since last commit
* Add some more code to `large-small-ts-analysis.R`.
    * `get_size_class()`

```
get_size_class <- function(weight) {
  if (weight > 50){
    size_class = "large"
  } else {
    size_class = "small"
  }
  return(size_class)
}
```

* Save `large-small-ts-analysis.R`.
* Now we see the file on the `Git` tab.
    * `M` indicates that it's been modified.
* To commit these changes, we need to stage the file.
    * Check the box next to `large-small-ts-analysis.R`.
* Commit with message.
    * `"Add function for determining size class"`
* History: 
    * Two commits 
    * Each commit shows the additions we made in that commit.

* Modify the code in `large-small-ts-analysis.R` 
    * Add `threshold` to `if()` in `get_size_class()`. 

```
get_size_class <- function(weight, threshold){
  if (weight > threshold){
    size_class = "large"
  } else {
    size_class = "small"
  }
  return(size_class)
}
```

* Stage -> Commit
    * Now we see both red and green sections. 
        * Green for lines that have been added 
        * Red for lines that have been deleted 
    * Git works line by line.
        * The previous version of the line is shown as deleted.
        * The new version of the line is shown as added.


> Do [Exercise 2 - First Commit]({{ site.baseurl }}/exercises/Version-control-basic-first-commit-R/).

### Git as a time machine

* Experiment with impunity

```
get_size_class <- function(weight, threshold){
  if (weight > threshold){
    size_class = 1
  } else {
    size_class = 2
  }
  return(size_class)
}
```

* `Save` and show changes are staged
* `More` -> `Revert`

* Get previous state of a file
    * `History` -> select commit -> `View file @ ...`

## GitHub Remotes

> Draw diagram to link local machine with GitHub `origin`.

* So far we've worked with a local `Git` repository.
* One of the big benefits of version control is easy collaboration.
* To do this, we synchronize our local changes with a `remote` repository.
* We'll use GitHub. 
    * By far the most popular hosted version control site
    * Public and private hosted repositories
    * Private free for students and academics
        * For the assignment, we'll use private repositories that I'll make for you.

### Add a remote

* Make a new `Git` repository ( *Students should have been assigned one.* )
* Copy remote adding code from GitHub.
    * `git remote add origin https://github.com/user/repo.git`
* <i class="fa fa-gear"></i> -> Shell
* Paste lines from GitHub -> Enter
* See files on GitHub
* Show browsing repo in past

> Do [Exercise 5 - Adding a Remote]({{ site.baseurl }}/exercises/Version-control-basic-adding-a-remote-R/).

### Push to a remote

* Add `add_size_classes()`.

```
add_size_classes <- function(df) {
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
    * Show on local, not remote
* Push
    * Show on remote

> Do [Exercise 6 - Pushing Changes]({{ site.baseurl }}/exercises/Version-control-basic-pushing-changes-R/).

### Collaborating

* Big advantage to remotes is easy collaboration
* Avoids emailing files and shared folders where you are never sure if you actually have the most recent version
* Makes it easy to see what collaborators have done
* While I've been talking, one of my collaborators has finished adding the other
functions we need.

* Pull
* Show history
* Run code

> Do [Exercise 7 - Pulling and Pushing]({{ site.baseurl }}/exercises/Version-control-basic-pulling-and-pushing-R/).
