# Data Carpentry for Biologists (semester long course)

Teaching materials for courses teaching biologists how to work with data through
programming, database management and computing more generally.

This repository contains the complete teaching materials (excluding exams and
answers to assignments) and website for a series of a university course teaching
computational data skills to biologists.


## Where is everything

Core teaching materials are stored in the relevant folders including `lectures`,
`ipynbs` (a series of Project Jupyter notebooks), and `exercises`.

Class specific materials are stored in `syllabus` and `assignments`.

Most of the other folders and files support creating the course website using
[Jekyll](http://jekyllrb.com/).


## Using Jekyll to build the course website

### Simple setup

The website is setup to be easy to run automatically through GitHub:

1. Fork the repository
   * In a few minutes you should be able to see the site at:
     `https://yourusername.github.io/datacarp-semester-biology/`
2. Edit any of the markdown (.md) files
3. Commit and push the changes
   * The changes should now be reflected on the website
4. If you want to use a custom domain name instead of `github.io`, follow
   [GitHub's instructions for setting up a custom domain](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/).

### Previewing changes locally

If you want to view your changes locally, before pushing them to the live
website, you'll need to setup Jekyll locally. GitHub provides a [good
introduction on how to do this](https://help.github.com/articles/using-jekyll-with-pages/).

If you have Jekyll properly installed, you can then run

`jekyll serve`

from the command line and navigate to http://localhost:4000/ in your browser to
preview the current state of the website.


## Creating new pages

If you want to add new lectures, exercises, etc. you do this by creating a
markdown file in the appropriate directory. Each markdown file needs to start
with some information that tells Jekyll what the page is. This is done using
something called YAML, and the standard YAML for a new exercise would look like
this:

```
---
layout: exercise
title: Name of Your Exercise
---
```

This is placed at the very beginning of the markdown file and provides
information on what kind of content it is (e.g., exercise, lecture, etc.) and
what the title of the page is.

The page should then be available at a url based on where the file is located
and what the file name is. So if you created a new exercise in the `exercises`
folder called `my_awesome_exercise.md` it would be located at:

Locally: `http://localhost:4000/exercises/my_awesome_exercise`
After pushing to GitHub: `https://yourusername.github.io/datacarp-semester-biology/exercises/my_awesome_exercise`
