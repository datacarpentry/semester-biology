---
layout: exercise
exercise_type: Version Control Basic
title: Set Up Git
language: R
---

Let’s say that you’re working on analyzing fish scale size data one day. Unfortunately you weren't using version control and your cat jumped 
all over your keyboard and managed to replace your analysis code with:

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
2. Click the `+` at the upper right corner of the page and choose `New repository`.
3. Choose the class organization (e.g., `dcsemester`) as the `Owner` of the
   repo.
4. Fill in a `Repository name` that follows the form `FirstnameLastname`.
5. Select `Private`.
6. Select `Initialize this repository with a README`.
7. Click `Create Repository`.

Next, set up a project for this assignment in RStudio with the following steps:

1. File -> New Project -> Version Control -> Git
2. Navigate to your new Git repo -> Click the `Clone or download` button ->
   Click the `Copy to clipboard` button.
3. Paste this in `Repository URL:`. 
4. Leave `Project directory name:` blank; automatically given repo name. 
5. Choose where to `Create project as subdirectory of:`.
6. Click `Create Project`.
7. Check to make sure you have a `Git` tab in the upper right window.
