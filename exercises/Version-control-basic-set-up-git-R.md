---
layout: exercise
topic: Version Control Basic
title: Set Up Git
language: R
---

This exercise and [Version Control Basics]({{ site.baseurl }}/assignments/r-git) 
assignment references the [Data Management Review]({{ site.baseurl }}/exercises/Basic-data-management-review-R) problem. 
*It will not be necessary to complete the [Data Management Review]({{ site.baseurl }}/exercises/Basic-data-management-review-R) exercise for this 
assignment, though we encourage the review and self-evaluation of your problem 
solving wizardry.*

You're continuing your analyses of house-elves with Dr. Granger. Unfortunately
you weren't using version control and one day your cat jumped all over your
keyboard and managed to replace your analysis code with:

```
asd;fljkzbvc;iobv;iojre,nmnmbveaq389320pr9c9cd

ds8
a
d8of8pp
```

before somehow hitting `Ctrl-s` and overwriting all of your hard word. 

Determined to not let this happen again you've committed to using `git` for
version control.

Install `Git` for your operating system following the
[setup instructions](http://www.datacarpentry.org/semester-biology/computer-setup/). Then
create a new repo at the Github organization for the class:

1. Navigate to Github in a web browser and login.
2. Click the `+` at the upper right corner of the page that shows the words
   `Create  new...` when you hover over it and choose `New repository`.
3. Choose the class organization (e.g., `dcsemester`) as the `Owner` of the
   repo.
4. Fill in a `Repository name` that follows the form `FirstnameLastname`.
5. Select `Private`.
6. Select `Initialize this repository with a README`.
7. Click `Create Repository`.

Next, set up a project for this assignment in RStudio with the following steps:

1. File -> New Project -> New Directory -> Version Control -> Git
2. Navigate to your new Git repo -> Click the `Clone or download` button ->
   Click the `Copy to clipboard` button.
3. Paste the `Repository URL:`. *A suggested `Project directory name:` should be
   automatically generated*.
4. Choose where to `Create project as subdirectory of:`.
5. Click `Create Project`.
6. Check to make sure you have a `Git` tab in the upper right window.
