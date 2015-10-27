---
layout: exercise
title: Version Control Basic 1
subtitle: Set-up Git
language: R
---

This is a follow up to [Basic 2]({{ site.baseurl }}/exercises/Basic-2-R).

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

Install git for your operating system following the
[setup instructions](http://www.datacarpentry.org/semester-biology/computer-setup/). Then
create a new project for this assignment in RStudio with the following steps:

a. File -> New Project -> New Directory -> Empty Project
b. Choose where to put your project
c. Select `Create a git repository`
d. If everything worked in the upper right corner of RStudio you should see a `Git` tab
