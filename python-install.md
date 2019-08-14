
## Installing Python

* Go to https://www.python.org/downloads
* Click the yellow `Download Python` button
* Start the installer
* Click "Add Python 3.7 to PATH" then "Install Now"

* Go to https://conda.io/miniconda.html
* Download the installer for your operating system
* Run the installer
* Keep all defaults
* 
* Open RStudio

```
install.packages('reticulate')
library('reticulate')
py_install('retriever')

install.packages('rdataretriever')
```

```
use_condaenv('r-reticulate')
library(rdataretriever)
```