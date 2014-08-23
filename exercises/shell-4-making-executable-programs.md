---
layout: exercise
title: Shell 4 - Making Executable Programs
---

This is a follow up on the [Shell 3 - Finding Things problem](/exercises/shell-3-finding-things).

Instead of having to call our Python program and our Bash script by
using the commands python and bash, it would be nice if we could just
execute them directly. So, let's do the following:

1.  Add shebangs to the beginning of both rich_pred.py and the bash
    script that you created in the previous problem. Do this using a
    shell text editor just to get a little practice. If you don't have a
    preference you can use nano by typing nano and then the name of the
    file.
2.  Commit these changes to your repository with a descriptive commit
    message. You can do this directly from the shell using `svn commit
    rich_pred.py my_file.sh -m "My totally useful and informative
    commit message"`. Don't forget to add your shell script first using
    svn add my_file.sh if you haven't already.
3.  Make both of these files executable
4.  Modify your shell script so that it executes `rich_pred.py` without
    using the python command. Commit the change (yes... with an
    informative commit message... *always with an informative commit
    message*).

