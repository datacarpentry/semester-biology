The Shell
=========

Introduction
------------

We're here to teach you about computers and computers really do four things:

* run programs
* store data
* communicate with each other
* and interact with us

They can do the last of these in many different ways.
The most common way of doing this is using a graphical interface.
Another way to do this is using a command line text interface called the shell.

The shell is very useful for three main reasons:

1. Automating data analysis
2. Combining existing tools in powerful ways with only a few keystrokes
3. Interacting with remote machines

###Why you should care
* Demo a workflow pipeline (use old Adv HW3)
* Need to understand all of this to do equivalent things in other languages

### Shortcuts
* Up and down arrows
* Tab
* history

Wednesday
---------
### Shebangs
A shebang is a special code at the beginning of a script to tell
the shell to run it as a scripot for a particular language.

Comes from Sharp(#) + Bang(!)

#### Syntax
* `#!/path/to/interpreter`
* `#!/bin/bash`
* `#!/usr/bin/python`

#### Portability
Above commands work on Linux and Mac. To allow use on Windows:

* `#!/usr/bin/env bash`
* `#!/usr/bin/env python`

This looks for the interpreter in the PATH
