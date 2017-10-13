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
> * Download [Gaeta_etal_CLC_data.csv](https://lter.limnology.wisc.edu/sites/default/files/Gaeta_etal_CLC_data.csv).
> * Arrange to have a teaching partner attend class and `push` the following
>   code for the 'Collaborating' demo.

```
ggplot(fish_data_cat, aes(x = scalelength, fill = length_cat)) +
  geom_histogram()
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
2. Click the `+` at the upper right corner of the page and choose `New repository`.
3. Choose the class organization (e.g., `dcsemester`) as the `Owner` of the
   repo.
4. Fill in a `Repository name` that follows the form `FirstnameLastname`.
5. Select `Private`.
6. Select `Initialize this repository with a README`.
7. Click `Create Repository`.

### Connect to the Git repo in RStudio

1. From new GitHub repository, click green `Clone or download` button ->
   Click the `Copy to clipboard` button.
2. In RStudio, File -> New Project -> Version Control -> Git
3. Paste copied URL in `Repository URL:`. 
4. Leave `Project directory name:` blank; automatically given repo name. 
5. Choose where to `Create project as subdirectory of:`.
6. Click `Create Project`.
7. Check to make sure you have a `Git` tab in the upper right window.

> Do [Exercise 1 - Set-up Git]({{ site.baseurl }}/exercises/Version-control-basic-set-up-git-R/).


### First commits

#### Commit data

* Download the data file [Gaeta_etal_CLC_data.csv](https://lter.limnology.wisc.edu/sites/default/files/Gaeta_etal_CLC_data.csv) to your project directory.
* Git -> Select `Gaeta_etal_CLC_data.csv`.
* Commit with message. 
    * `Add fish size and growth rate data`
* History: 
    * One commit
    * Changes too large to see

#### Commit R script

* Read in data to new R script.

```
fish_data = read.csv("Gaeta_etal_CLC_data.csv")
```

* Save as `fish-analysis.R`. 
* Git -> Select `fish-analysis.R`. 
    * Changes in staged files will be included in next commit.
    * Can also see changes by selecting `Diff`
* Commit with message. 
    * `Start script comparing fish length and scale size`
* History: 
    * Two commits
    * See what changes were made to `fish-analysis.R`

### Building a history

* `fish-analysis.R` doesn't currently show on the `Git` tab
    * No saved changes since last commit
* Add some more code to `fish-analysis.R`
    * Create new categorical size column

```
library(dplyr)
fish_data_cat = fish_data %>% 
  mutate(length_cat = ifelse(length > 200, "big", "small"))
```

* Save `fish-analysis.R`.
* Now we see the file on the `Git` tab.
    * `M` indicates that it's been modified.
* To commit these changes, we need to stage the file.
    * Check the box next to `fish-analysis.R`.
* Commit with message.
    * `Add categorical fish length column`
* History: 
    * Three commits 
    * Each `fish-analysis.R` commit shows the additions we made in
      that commit.

* Modify this code in `fish-analysis.R` 
    * Change category cut-off size

```
fish_data_cat = fish_data %>% 
  mutate(length_cat = ifelse(length > 300, "big", "small"))
```

* Save file -> stage -> commit
    * `Change size cutoff for new column`
    * Green sections for added lines, red for deleted
    * Git works line by line.
        * The previous version of the line is shown as deleted.
        * The new version of the line is shown as added.


> Do [Exercise 2 - First Solo Commit]({{ site.baseurl }}/exercises/Version-control-basic-first-solo-commit-R/),
> [Exercise 3 - Second Solo Commit]({{ site.baseurl }}/exercises/Version-control-basic-second-solo-commit-R/),
> and [Exercise 4 - Commit Multiple Files]({{ site.baseurl }}/exercises/Version-control-basic-commit-multiple-files-R/).

> Instructor also do exercises

### Git as a time machine

#### Experiment with impunity

```
fish_data_cat = fish_data %>% 
  mutate(length_cat = ifelse(length > 300, "large", "small"))
```

* `Save` and show changes are staged
* <i class="fa fa-gear"></i> `More` -> `Revert` -> `Yes`

* Get previous state of a file
    * `History` -> select commit -> `View file @ ...`

#### Delete with impunity

* Close the upper left window with the `fish-analysis.R`.
* Choose the `File` tab in the lower right window.
* Select `fish-analysis.R` -> `Delete` -> `Yes`
* Stage deleted file -> <i class="fa fa-gear"></i> `More` -> `Revert` -> `Yes`

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


> Do [Exercise 5 - Pushing Changes]({{ site.baseurl }}/exercises/Version-control-basic-pushing-changes-R/).

> Have students email a link to their repo to their instructor once they have
> finished Pushing Changes
>
> The instructor should then commit the following code to their repo
> with the commit message: `Plot histogram of scale length by fish categorical size`

```
ggplot(fish_data_cat, aes(x = scalelength, fill = length_cat)) +
  geom_histogram()
```

### Collaborating

* Big advantage to remotes is easy collaboration
* Avoids emailing files and shared folders where you are never sure if you
  actually have the most recent version
* Makes it easy to see what collaborators have done
* Automatically combines non-overlapping changes
* While I've been talking, a collaborator has added a plot of scale size and fish length to the code.

> Show `origin` with collaborator commit.

> Add collaborator local repo to diagram and `pull` arrow from `origin` to
> locals.
 
* `Pull` the changes from the remote repo with the `Pull` button on the Git tab

> Show updates to history following `Pull` and run code

> Do Tasks 3-6 in [Exercise 6 - Pulling and Pushing]({{ site.baseurl }}/exercises/Version-control-basic-pulling-and-pushing-R/).

* Collaborating on Github can get more complex with "forks" and "branches.

> *Optional*: Redraw diagram with local, `origin`, and `upstream`. Arrows from
> `origin` to/from `upstream` are pull requests and merges.

> Show an [example of a working repository]({{ site.github.repo }}) with
> branches and forks. Navigate to pull requests.


