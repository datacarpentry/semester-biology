---
layout: page
title: Computer Setup
---

### Python

Download and install the
[Anaconda Scientific Python Distribution](http://continuum.io/downloads).
I recommend you use a special editor like the [Wing Intelligent Development Environment - 101](http://wingware.com/downloads/wingide-101).


### R

Download and install the [R base system](http://cran.rstudio.com/). I recommend you use the [R studio](http://www.rstudio.com/products/rstudio/download/) to work with the base system.


### SQL

Download and install [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/). Add the [SQLite Manager](https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/).


### Git

#### Windows

1.  Download the Git for Windows
    [installer](https://git-for-windows.github.io/).
2.  Run the installer and follow the steps bellow:
    1.  Click on "Next".
    2.  Click on "Next".
    3.  Click on "Next".
    4.  Click on "Next".
    5.  Click on "Next".
    6.  **Select "Use Git from the Windows Command Prompt" and click on
        "Next".** If you forgot to do this programs that you need for
        the workshop will not work properly. If this happens rerun the
        installer and select the appropriate option.
    7.  Click on "Next". **Keep "Checkout Windows-style, commit
        Unix-style line endings" selected.**
    8.  **Select "Use Windows' default console window" and click on
        "Next".**
    9.  Click on "Next".
    10. Click on "Finish".


#### Mac OS X

1. Open up the Terminal, type in "git" and press enter.
2. This should cause a pop-up window to appear. It will have several options;
   click on "Install" (not "Get Xcode", see "Installing Xcode" for that).
3. Click "Agree".
4. When the install is finished, click "Done".
5. To make sure this worked, type in "git" in the Terminal and press enter. Some
   information will come up, including a list of common commands.

If this doesn't work you can try the following:

For **OS X 10.9 and higher**, install Git for Mac by downloading and running the
most recent "mavericks" installer from
[this list](http://sourceforge.net/projects/git-osx-installer/files/).  After
installing Git, there will not be anything in your `/Applications` folder, as
Git is a command line program. For older versions of **OS X (10.5-10.8)**
use the most recent available installer labelled "snow-leopard" [available
here](http://sourceforge.net/projects/git-osx-installer/files/.)

#### Linux

Git is probably already installed. If it is not already available on your
machine you can try to install it via your distro's package manager. For
Debian/Ubuntu run `sudo apt-get install git` and for Fedora run `sudo yum
install git`.
