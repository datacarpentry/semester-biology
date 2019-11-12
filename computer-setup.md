---
layout: page
title: Computer Setup
---

***WIS 6934 students will need their own laptops set up with R by week 2, Git by week 10, and SQL by week 13.***

### R

Download and install the [R base system](http://cran.rstudio.com/) and [RStudio](http://www.rstudio.com/products/rstudio/download/). Both are needed. Installing RStudio will not automatically install R.

### GitHub

1. Create an account on GitHub (https://github.com) using the `Sign up for
   GitHub` form on the right side of the page.
2. Send your username to your instructor.
3. Once your instructor adds you to the course GitHub organization you will
   receive an email asking you to accept the invitation. Click on the link to
   accept.
4. Check if this worked
    1. Go to [https://github.com](https://github.com).
    2. Sign in if necessary.
    3. In the upper left corner click on the drop down with your name.
    4. Confirm that the name name of the course GitHub organization is present

### Git

#### Windows

1.  Download the Git for Windows
    [installer](https://git-for-windows.github.io/).
2.  Run the installer and follow the steps bellow:
    1. Click on "Next".
    2. Click on "Next".
    3. Keep "Use Git from the Windows Command Prompt" selected and click on
       "Next". If you forgot to do the integration with R will not work
       properly. If this happens rerun the installer and select the appropriate
       option.
    4. Click on "Next".
    5. Keep "Checkout Windows-style, commit Unix-style line endings" selected and click on "Next".
    6. Keep "Use Windows' default console window" selected and click on "Next".
    7. Click on "Install".
    8. Click on "Finish".
3. Check if the installation is working:
    1. Send your username to your instructor. Once you have received a GitHub invite to the class organization accept it and only then proceed.
    2. Open RStudio
    3. File -> New Project -> Version Control -> Git
    4. On the page called `Clone Git Repository` paste <https://github.com/dcsemester/install-test.git> into the "Repository URL:" box.
    5. Click "Create Project"
    6. Enter your GitHub username and password when prompted
    7. If you see no errors and a file named `SUCCESS.txt` in your Files tab then everything is setup correctly.

If git and RStudio aren't talking to each other (i.e., you don't get the expected
result from when you check the installation), try the following:

1. Open RStudio
2. Select the `Tools` menu -> `Global Options` -> `Git/SVN`
3. Next to `Git executable` click `Browse`
4. Navigate to `C:\Program Files\Git\bin\` and double click on `git` (this should change
   the value in `Git executable` to `C:\Program Files\Git\bin\git`)
5. Click `OK`

**Do not change the git executable to `C:\Program Files\Git\mingwXX\bin\git` as this will fail on some systems with an error message including "rpostback-askpass".**

#### Mac OS X

1. Open up the Terminal, type in "git" and press enter.
2. This should cause a pop-up window to appear. It will have several options;
   click on "Install" (not "Get Xcode").
3. Click "Agree".
4. When the install is finished, click "Done".
5. To make sure this worked, type in "git" in the Terminal and press enter. Some
   information will come up, including a list of common commands. If this
   doesn't work see additional instructions below.
6. Check if git and RStudio are talking to each other:
    1. Send your username to your instructor. Once you have received a GitHub invite to the class organization accept it and only then proceed.
    2. Open RStudio
    3. File -> New Project -> Version Control -> Git
    4. On the page called `Clone Git Repository` paste <https://github.com/dcsemester/install-test.git> into the "Repository URL:" box.
    5. Click "Create Project"
    6. Enter your GitHub username and password when prompted
    7. If you see no errors and a file named `SUCCESS.txt` in your Files tab then everything is setup correctly.

If the git installation didn't work (i.e., you don't get the expect result from
Step 5), try the following:

For **OS X 10.9 and higher**, install Git for Mac by downloading and running the
most recent "mavericks" installer from
[this list](http://sourceforge.net/projects/git-osx-installer/files/).  After
installing Git, there will not be anything in your `/Applications` folder, as
Git is a command line program. For older versions of **OS X (10.5-10.8)**
use the most recent available installer labelled "snow-leopard" [available
here](http://sourceforge.net/projects/git-osx-installer/files/.)

If git and RStudio aren't talking to each other (i.e., you don't get the expect
result from Step 6), try the following:

1. Open RStudio
2. Select the `Tools` menu -> `Global Options` -> `Git/SVN`
3. Next to `Git executable` click `Browse`
4. Navigate to `usr/local/bin/` and double click on `git` (this should change
   the value in `Git executable` from `/usr/bin/git` to `/usr/local/bin/git`)
5. Click `OK`

#### Linux

Git is probably already installed. If it is not already available install it via
your distro's package manager. For Debian/Ubuntu run `sudo apt-get install git`
and for Fedora run `sudo yum install git`.

### SQL

Download and install [DB Browser for SQLite](http://sqlitebrowser.org/)

### Python

*Python installation is not required for WIS 6934. Python materials on this site
are no longer under active development.*

Download and install the
[Anaconda Scientific Python Distribution](http://continuum.io/downloads).
I recommend you use a special editor like the [Wing Intelligent Development Environment - 101](http://wingware.com/downloads/wingide-101).
