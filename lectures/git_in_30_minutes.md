# A quick introduction to Git and GitHub

## Setup

In a browser:

* http://www.phdcomics.com/comics/archive.php?comicid=1531
* http://www.phdcomics.com/comics/archive.php?comicid=1323
* http://github.com

## Introduction

Who has a directory on their computer with a bunch of filenames that look like
these? (1531)

And how about one that looks like this? (1323)

What we're going to learn about today is how to get rid of folders like this and
keep the same kind of backup and change information in a more useful way.

Version control  gives you a better way to track changes to things like data
files and code in a more manageable way. That's important because when the
reviews come back on your paper and ask you to perform some additional analyses
and you open up this directory, it can be pretty difficult to figure out which
file you should actually use. At the very least you'll spend a bunch of extra
time figuring it out before you get to work, but I've also certainly picked the
wrong file and had to redo all of my work after I finally realized I wasn't
getting the same results as in the submitted version of the manuscript.

## Benefits of version control

* Track changes on steroids
    * Tracks every change ever made in groups called commits
	* Every commit stores the full state of all of your files at that time
    * Never lose anything
	* Easily unbreak your code/data/manuscript
	* No more file name changes
* Collaboration
    * Work on things simultaneously
	* See what changes others have made
	* Everyone has the most recent version of everything

## Git

* Create a new repository
* Add a file (bird_data.txt)

```
date,species,number
2014-04-15,chickadee,3
2014-04-15,bluejay,3
```

* Now commit these changes by providing a clear description of what you did.
* We can see that
    1. We've created the file
    2. Our commit describing what we've done is listed
	3. If we look at the commit the green lines with pluses are telling us that 
      we've added these three lines to our file.
* If I change the file by adding some more data then the commit shows exactly
  what I've changed

```
2014-04-16,sparrow,2
2014-04-16,mallard,2
2014-04-17,robin,999
```

* Fix typo
* Show that you can go back in time

## Advantages

* easily follow what we've done over time
* easy to both know what we've done
* easy to fix things if we break them
* easy to rerun your code from 3 months ago to make sure the code still does the
  same thing
  * who has ever had code that worked one day, you changed a few things that
    shouldn't hurt anything and then a couple of days later the code wouldn't run?
  * demo using White et al.


## Collaboration

* Work on things simultaneously
* See what changes others have made
* Everyone has the most recent version of everything
* Show Retriever repository on GitHub

## Common points of confusion

* Git vs. GitHub
  * Private GitHub repos (https://education.github.com/)
* Everything is a repository
* Stage
