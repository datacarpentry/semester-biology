---
layout: exercise
topic: Version Control Basic
title: Set-up Git
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

Install `git` for your operating system following the
[setup instructions](http://www.datacarpentry.org/semester-biology/computer-setup/). Then
create a new project for this assignment in RStudio with the following steps:

1. File -> New Project -> New Directory -> Empty Project
2. Choose where to put your project
3. Select `Create a git repository`
4. If everything worked in the upper right corner of RStudio you should see a `Git` tab
