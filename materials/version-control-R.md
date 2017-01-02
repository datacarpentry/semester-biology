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
> * Setup class organization at Github. 
> * Add students' username to organization with "create repo" permissions and
>   respond with link to organization in email.

> For class
> 
> * Download [`houseelf-earlength-dna-data.csv`]({{ site.baseurl }}/data/houseelf-earlength-dna-data.csv).
> * Arrange to have a teaching partner attend class and `push` the following
>   code for the 'Collaborating' demo.

```
library(dplyr)

data_size_class <-
  data %>% 
  rowwise() %>% 
  transmute(id = id, earlengthcat = get_size_class(earlength, 10))
```

> * Open the following links in a browser and zoom in to make the images fill
>   the screen.
>
> > * [Like this?](http://www.phdcomics.com/comics/archive.php?comicid=1531)
> > * [Or like this?](http://www.phdcomics.com/comics/archive.php?comicid=1323)

> 
> **Live coding demo parallels assignment.**

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

## Version control using Git & RStudio

### Create a Git repo

1. Navigate to Github in a web browser and login.
2. Click the `+` at the upper right corner of the page that shows the words
   `Create  new...` when you hover over it and choose `New repository`.
3. Choose the class organization (e.g., `dcsemester`) as the `Owner` of the
   repo.
4. Fill in a `Repository name` that follows the form `FirstnameLastname`.
5. Select `Private`.
6. Select `Initialize this repository with a README`.
7. Click `Create Repository`.

### Connect to the Git repo in RStudio

1. File -> New Project -> New Directory -> Version Control -> Git
2. Navigate to your new Git repo -> Click the `Clone or download` button ->
   Click the `Copy to clipboard` button.
3. Paste the `Repository URL:` *A suggested `Project directory name:` should be
   automatically generated*.
4. Choose where to `Create project as subdirectory of:`.
5. Click `Create Project`.
6. Check to make sure you have a `Git` tab in the upper right window.

> Do [Exercise 1 - Set-up Git]({{ site.baseurl }}/exercises/Version-control-basic-set-up-git-R/).


### First commits

*The following example uses the code from the [Data Management Review]({{ site.baseurl }}/exercises/Basic-data-management-review-R) exercise.*

#### Commit data

* Download the data file [`houseelf-earlength-dna-data.csv`]({{ site.baseurl }}/data/houseelf-earlength-dna-data.csv) to your project directory.
* Git -> Select `houseelf-earlength-dna-data.csv`.
* Commit with message. 
    * `"Add earlength data of houseelves"`
* History: 
    * One commit
    * Changes too large to see

#### Commit R script

* Create a new file. 
    * `houseelf-analysis.R`
* Add some code to the file.
    * `get_data()`

```
get_data <- function() {
  data <- read.csv("houseelf-earlength-dna-data.csv")
  return(data)
}

data <- get_data()
```

* Git -> Select `houseelf-analysis.R`. 
    * Changes in staged files will be included in next commit.
    * Can also see changes by selecting `Diff`
* Commit with message. 
    * `"Start script comparing earlength and DNA of houseelves"`
* History: 
    * Two commits
    * See what changes where made to `houseelf-analysis.R`

### Building a history

* `houseelf-analysis.R` doesn't currently show on the `Git` tab
    * No saved changes since last commit
* Add some more code to `houseelf-analysis.R`.
    * `get_size_class()`

```
get_size_class <- function(earlength){
  if (earlength > 10){
    size_class = "large"
  } else {
    size_class = "small"
  }
  return(size_class)
}
```

* Save `houseelf-analysis.R`.
* Now we see the file on the `Git` tab.
    * `M` indicates that it's been modified.
* To commit these changes, we need to stage the file.
    * Check the box next to `houseelf-analysis.R`.
* Commit with message.
    * `"Add function for determining size class"`
* History: 
    * Three commits 
    * Each `houseelf-analysis.R` commit shows the additions we made in
      that commit.

* Modify the code in `houseelf-analysis.R` 
    * Add `threshold` to `if()` in `get_size_class()`. 

```
get_size_class <- function(earlength, threshold){
  if (earlength > threshold){
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
get_size_class <- function(earlength, threshold){
  if (earlength > threshold){
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

* Close the upper left window with the `houseelf-analysis.R`.
* Choose the `File` tab in the lower right window.
* Select `houseelf-analysis.R` -> `Delete` -> `Yes`
* <i class="fa fa-gear"></i> `More` -> `Revert` -> `Yes`

## GitHub Remotes

> Draw diagram to link local machine with GitHub `origin`.

* So far we've worked with a local `Git` repository.
* One of the big benefits of version control is easy collaboration.
* To do this, we synchronize our local changes with a remote repository called
  `origin`.
* Our remote repository is on GitHub. 
    * By far the most popular hosted version control site
    * Public and private hosted repositories
    * Private free for students and academics
	* https://education.github.com/
        * For the assignment, we're using private repositories that we made at
          the beginning.

### Push to a remote

* `Push` sends your recent commits to the `origin` remote.

> Draw push arrow on diagram on board from local to `origin`.

* Before a `Push` your commits show in your local history but not on the remote.

> Show local commit history and lack of history in remote.

* To `Push` to your remote, select the `Push` button at the top of the `Git`
  tab.
* Now your changes and commit history are also stored on the remote.

> Show local commits now on `origin`.


> Do [Exercise 6 - Pushing Changes]({{ site.baseurl }}/exercises/Version-control-basic-pushing-changes-R/).

> Have students email a link to their repo to their instructor once they have
> finished Pushing Changes
>
> The instructor should then commit the following code to their repo
> with the commit message: "Generate data frame with id and earlength class"

```
library(dplyr)

data_size_class <-
  data %>% 
  rowwise() %>% 
  transmute(id = id, earlengthcat = get_size_class(earlength, 10))
```

### Collaborating

* Big advantage to remotes is easy collaboration
* Avoids emailing files and shared folders where you are never sure if you
  actually have the most recent version
* Makes it easy to see what collaborators have done
* Automatically combines non-overlapping changes
* While I've been talking, Dr. Granger has finished adding some code that we
  need to put our results into a data frame.

> Show `origin` with collaborator commit.

> Add collaborator local repo to diagram and `pull` arrow from `origin` to
> locals.
 
* `Pull` the changes from the remote repo with the `Pull` button on the Git tab

> Show updates to history following `Pull` and run code

> Do [Exercise 7 - Pulling and Pushing]({{ site.baseurl }}/exercises/Version-control-basic-pulling-and-pushing-R/).

* Collaborating on Github can get more complex with "forks" and "branches.

> *Optional*: Redraw diagram with local, `origin`, and `upstream`. Arrows from
> `origin` to/from `upstream` are pull requests and merges.

> Show an [example of a working repository]({{ site.github.repo }}) with
> branches and forks. Navigate to pull requests.


