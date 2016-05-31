Python Packaging
================

Basic Packaging
---------------
Add a file named ``setup.py`` to your project directory.
Users can then install the package using

    python setup.py install

from the command line.

This file contains metadata about the project. The simplest ``setup.py`` file possible is:

    from setuptools import setup, find_packages

    setup(
	      name='mymodule',
          version='0.1',
          py_modules = ['ultimate_answer']
		  )

### Example

Create a simple .py file called ``ultimate_answer.py`` that prints:

*The answer to life the universe and everything is 42*

    print "The answer to life the universe and everything is 42"

* If we try to import this module from anywhere other than it's directory,
  Python can't find it.
* But if we add a ``setup.py`` file and use it to install the package, then it
  can be used from anywhere.

```
from setuptools import setup, find_packages

setup(
      name='ultimate_answer',
      version='0.1',
      py_modules = ['ultimate_answer']
	  )

Now run

    python setup.py install


Setuptools
----------

This works great for simple modules, but real modules have dependencies,
and their modules have dependencies, and we'd have to install them all one at a
time. Instead, we can automate this using our `setup.py` file.

Python keeps an online repository of packages and running ``easy_install`` or
``pip`` will search the repository for the package you want and install it
automatically while handling any dependencies.

**NEEDS EXAMPLE**

Command line programs
---------------------

We can make our Python programs run from anywhere on the command line with some relatively minor modifications to ultimate_answer.py:

    def main():
        print "The answer to life the universe and everyting is 42"

    if __name__ == '__main__':
        main()

And setup.py:

    from setuptools import setup

    setup(name='ultimate_answer',
        version='0.1',
        py_modules = ['ultimate_answer'],
        entry_points={'console_scripts': ['ult_ans = ultimate_answer:main']})


Creating executable programs
----------------------------

We can also create versions of our programs that are self-contained executable programs.

### Windows

1. Install the py2exe module
2. Run ``python setup.py install``
3. Run ``python setup.py py2exe``

This will create a .exe file that can be run on any Windows computer,
no Python or modules required.

### Example

1. Download pythonpy
2. Download setup2.py
3. Install

Package structure
-----------------

    package/
        __init__.py
        module1.py
        subpackage/
            __init__.py
            module2.py

    import package.module1
    from package.subpackage import module2
    from package.subpackage.module2 import name
