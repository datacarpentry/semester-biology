--- layout: post title: Installing Nose on Windows created: 1319034892
categories: [] ---

#### With easy\_install/pip

1.  If pip is installed on your system then simply type **pip install
    nose** into Cywin or the Windows command line
2.  If easy\_install is installed, but pip is not, then install pip
    using **easy\_install pip** and then run **pip install nose**

#### Using setup.py\

1.  Download Nose either from the [main download
    page](http://code.google.com/p/python-nose/downloads/list) (if you
    can extract .tar.gz files) or get the [zipped version I've created
    here](http://www.programmingforbiologists.org/sites/programmingforbiologists.org/files/nose-1.0.0.zip)
2.  Extract the archive
3.  Using either Cygwin or the Windows command line avigate to the
    location where you extracted it and then into the two nose-1.0.0
    directories
4.  Check to make sure that you're in the right place. The direcotry
    should contain a bunch of files and directories including a nose
    directory and a file named setup.py
5.  Run the command **python setup.py install**
6.  This is the standard way to install Python modules that don't come
    with executable installers\

