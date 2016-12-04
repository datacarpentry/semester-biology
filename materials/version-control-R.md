---
layout: page
element: notes
title: Version Control
language: R
--- 

> Before class
>
> * Remind students to setup a GitHub account and email the instructor their
>   username. 
> * Setup repo with students' username and respond with link to repo in email.

> For class
> 
> * Download [`surveys.csv`](https://ndownloader.figshare.com/files/2292172).
> * Arrange to have a teaching partner attend class and `push` the following
>   code for the 'Collaborating' demo.

```
get_size_class_ts_data <- function(df){
  # Convert individual data to time-series data for each of a set 
  # of size classes
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

> * Open the following links in a browser and zoom in to make the images fill
>   the screen.
>
> > * [Like this?](http://www.phdcomics.com/comics/archive.php?comicid=1531)
> > * [Or like this?](http://www.phdcomics.com/comics/archive.php?comicid=1323)

> **Students need 2 projects to follow along with live coding.**
> **Must switch projects when shifting from live coding to exercises**

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
4. Check to make sure you have a `Git` tab in the upper right window.

> Do [Exercise 1 - Set-up Git]({{ site.baseurl }}/exercises/Version-control-basic-set-up-git-R/).

#### Tell git who you are

* Click on <i class="fa fa-gear"></i> `More`
* Select `Shell`

```
git config --global user.name 'Ethan White'
git config --global user.email 'ethan@weecology.org'
git config --global --list
```

### First commits

*The following example uses the code from the problem decomposition lecture.*

#### Commit data

* Download the data file [`surveys.csv`](https://ndownloader.figshare.com/files/2292172) to your project directory.
* Git -> Select `surveys.csv`.
* Commit with message. 
    * `"Add survey data of different sized rodents"`
* History: 
    * One commit
    * Changes too large to see

#### Commit R script

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
    * `"Start script comparing dynamics of different sized rodents"`
* History: 
    * Two commits
    * See what changes where made to `large-small-ts-analysis.R`

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
    * Three commits 
    * Each `large-small-ts-analysis.R` commit shows the additions we made in
      that commit.

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


> Do [Exercise 2 - First Commit]({{ site.baseurl }}/exercises/Version-control-basic-first-commit-R/),
> [Exercise 3 - Importing Data]({{ site.baseurl }}/exercises/Version-control-basic-importing-data-R/),
> and [Exercise 4 - Commit Multiple Files]({{ site.baseurl }}/exercises/Version-control-basic-commit-multiple-files-R/).

### Git as a time machine

#### Experiment with impunity

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
* <i class="fa fa-gear"></i> `More` -> `Revert` -> `Yes`

* Get previous state of a file
    * `History` -> select commit -> `View file @ ...`

#### Delete with impunity

* Close the upper left window with the `large-small-ts-analysis.R`.
* Choose the `File` tab in the lower right window.
* Select `large-small-ts-analysis.R` -> `Delete` -> `Yes`
* <i class="fa fa-gear"></i> `More` -> `Revert` -> `Yes`

## GitHub Remotes

> Draw diagram to link local machine with GitHub `origin`.

* So far we've worked with a local `Git` repository.
* One of the big benefits of version control is easy collaboration.
* To do this, we synchronize our local changes with a `remote` repository.
* We'll use GitHub. 
    * By far the most popular hosted version control site
    * Public and private hosted repositories
    * Private free for students and academics
	    * https://education.github.com/
        * For the assignment, we'll use private repositories that I'll make for you.

### Add a remote

* Make a new `Git` repository ( *Students should have been assigned one.* )
* **Add helper as collaborator**
* Copy remote adding code from GitHub.
    * `git remote add origin https://github.com/user/repo.git`
* <i class="fa fa-gear"></i> `More` -> Shell
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

> Draw push/pull on diagram on board

> Do [Exercise 6 - Pushing Changes]({{ site.baseurl }}/exercises/Version-control-basic-pushing-changes-R/).

> Have students email a link to their repo to their instructor once they have
> finished Pushing Changes
>
> The instructor should then commit the following code to their repo
>
> get_size_class <- function(ear_length){
>   # Calculate the size class for one or more ear lengths
>   ear_lengths <- ifelse(ear_length > 10, "large", "small")
>   return(ear_lengths)
> }
>
> With the commit message:
> Add function for determining ear length class

### Collaborating

* Big advantage to remotes is easy collaboration
* Avoids emailing files and shared folders where you are never sure if you
  actually have the most recent version
* Makes it easy to see what collaborators have done
* Automatically combines non-overlapping changes
* While I've been talking, one of my collaborators has finished adding the other
  functions we need.

* Pull
* Show history
* Run code

> Show an example of a working repository
> Show examples of pull requests

> Do [Exercise 7 - Pulling and Pushing]({{ site.baseurl }}/exercises/Version-control-basic-pulling-and-pushing-R/).
