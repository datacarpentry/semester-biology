The Shell
=========

Monday
------

###Why you should care
* Demo a workflow pipeline
* Commit all data files for Problem 2 using:

        python multi_svn.py add areas*
        python multi_svn.py commit "Adding data files for hotspot analysis."
    

### Shortcuts
* Up and down arrows
* Tab

### Version Control
* `svn checkout`
* `svn update`
* `svn add`
* `svn commit`

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

### Shell from inside Python
Everything you can do in the shell you can do using Python.
The two key modules for doing so are:

* [`os`](http://docs.python.org/library/os.html), which is easy
        import os
        os.system("ls -l -a")
* [`subprocess`](http://docs.python.org/library/subprocess.html), which is "best"

        import subprocess
        subprocess.call(["ls"])
        subprocess.call(["ls", "-l"])
        directory_list = subprocess.check_output(["ls", "-l"])
        directory_list = subprocess.os.listdir('.')


Friday
------

### SSH

### Background Jobs
