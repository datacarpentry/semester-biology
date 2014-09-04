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
