---
layout: page
element: notes
title: Version Control
language: R
--- 

> Before class
>
> * Setup class organization at Github
>     * Check the `Allow members to create repositories for this organization ` permission
>     * Set the `Default permissions` for the organization to `None` if you want
>       to avoid students accessing each others repositories
> * Have students create a GitHub account and email their username to the instructor.
> * Add students' username to organization.

> For class
> 
> * Download [Gaeta_etal_CLC_data.csv](https://lter.limnology.wisc.edu/sites/default/files/Gaeta_etal_CLC_data.csv).
> * Either arrange to have a teaching partner to attend class or be logged into GitHub as another user in the browser for collaboration demos.
>
> * Open the following links in a browser and zoom in to make the images fill
>   the screen.
>
> > * [http://www.phdcomics.com/comics/archive.php?comicid=1531](http://www.phdcomics.com/comics/archive.php?comicid=1531)
> > * [http://www.phdcomics.com/comics/archive.php?comicid=1323](http://www.phdcomics.com/comics/archive.php?comicid=1323)

> 
> **Live coding demo and assignment are intertwined and designed to work in order.**

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

### Introduce yourself to Git

1. Git tab -> `More` -> `Shell`
2. `git config --global user.name "[name]"`
3. `git config --global user.email "[email]"` (same as GitHub account email).

> That was [Exercise 1 - Set-up Git]({{ site.baseurl }}/exercises/Version-control-basic-set-up-git-R/).
> Have students confirm that this all worked and fix any issues.


### First commits

#### Commit data

* Download the data file [Gaeta_etal_CLC_data.csv](https://lter.limnology.wisc.edu/sites/default/files/Gaeta_etal_CLC_data.csv) to your project directory.
* Add the data file to version control
* Two step process:

1. Add the data file (checkbox)
2. Commit it

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


> Do [Exercise 2 - First Solo Commit]({{ site.baseurl }}/exercises/Version-control-basic-first-solo-commit-R/) and
> [Exercise 3 - Second Solo Commit]({{ site.baseurl }}/exercises/Version-control-basic-second-solo-commit-R/)

> **Instructor also do exercises**


### Committing multiple files

* Commits can include multiple files at once
* Let's move our data file into a `data` subdirectory
* `New Folder` -> `data`
* Checkbox `Gaeta_etal_CLC_data.csv` -> `More` -> `Move`
* Change code to read from new subdirectory

```r
fish_data = read.csv("data/Gaeta_etal_CLC_data.csv")
```

* Changes to R script indicated by M
* Original datafile has a red D next to it which indicates "deleted"
* New, untracked, data directory
* git initially thinks we've deleted `Gaeta_etal_CLC_data.csv` and created a new `Gaeta_etal_CLC_data.csv` file in a new directory.
* Click on both the old and new files to stage them
* git then recognizes that we have moved (or renamed) the file by making the two files into one and marking this with an `R` for "rename".

* Commit: `Move data file into subdirectory`

> Do [Exercise 4 - Commit Multiple Files]({{ site.baseurl }}/exercises/Version-control-basic-commit-multiple-files-R/).

> **Instructor also do exercise**

### Git as a time machine

#### Experiment with impunity

<pre>
fish_data_cat = fish_data %>% 
  mutate(length_cat = ifelse(length > 300, <b>"large"</b>, "small"))
</pre>

* `Save` and show changes are staged
* <i class="fa fa-gear"></i> `More` -> `Revert` -> `Yes`

* Get previous state of a file
    * `History` -> select commit -> `View file @ ...`
    * Save file over current file
    * Copy and paste relevant piece into current file

#### Delete with impunity

* Both of these also work for deleted files
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
> with the commit message: `Plot histogram of scale length by categorical size`

```
ggplot(fish_data_cat, aes(x = scalelength, fill = length_cat)) +
  geom_histogram()
```

> Either you (logged in as another user) or your teaching partner should make
> the same change to your respository

### Pulling

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


### Merges

> Demo merges either with a partner or by logging into GitHub as another user in
> the browser.

* What happens if two people make changes at the same time?
    * If they edit different parts of the code git will combine them automatically
    * If they edit the same areas of the code this requires human intervention
* Merges

* You decide to change the number of histogram bins to 10

<pre>
geom_histogram(<b>bins = 10</b>)
</pre>

* Your collaborator reassesses the measurement device and decides it is accurate
  down to 0.5 mm and pushes the change to the remote repository [make this
  change in the remote]

<pre>
filter(scalelength >= <b>0.5</b>)
</pre>

* You try to push your change
* Get an error that shows someone else has made a change & you need to
  incorporate it to push
* Pull
* Merge happens automatically
* You have both sets of changes
* Remote still only has collaborators changes
* Push to add the merged version to the remote

### Merge conflicts

* If both you and your collaborator edit the same location in the code git
  doesn't know how to combine the changes.
* A human has to make this kind of decision.

* You decide to change `"big"` to `"large"`

<pre>
mutate(length_cat = ifelse(length > 300, <b>"large"</b>, "small"))
</pre>

* Your collaborator changes the size threshold and pushes to the remote

<pre>
mutate(length_cat = ifelse(length > 250, <b>"big"</b>, "small"))
</pre>

* You attempt to push your changes
* Merge conflict when pulling collaborators changes
* This shows as `U` for "unmerged" in RStudio
* First block of code is your version
* Second block is the version on the remote
* Combine into a single block that includes everything

```
mutate(length_cat = ifelse(length > 250, "large", "small"))
```

* Click check box next to file
* Commit indicating that it is a merge
* Still not on remote yet
* Push

### Full GitHub flow

* Collaborating on Github can get more complex with "forks" and "branches.

> *Optional*: Redraw diagram with local, `origin`, and `upstream`. Arrows from
> `origin` to/from `upstream` are pull requests and merges.

> Show an [example of a working repository]({{ site.github.repo }}) with
> branches and forks. Navigate to pull requests.


