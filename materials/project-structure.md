---
layout: page
element: notes
title: Project Structure
language: R
--- 

### Simple
* Main/Root directory (`./`)
    * Code file (`.R`)
        * single top level script
        * linked data manipulation and analysis scripts
    * Project File (`.Rproj`)
    * `README`
        * description of what you're doing and how to run w/top level script
        * `.txt` or `.md`        
    * Data (`./data/`) 
        * Sub directories may be useful
    * Results (`./results/`)
        * Sub directories may be useful

```
./README
./myproject.Rproj
./mydatascript.R
./myanalysisscript.R
./data/datafile1.txt
./data/datafile2.txt
./results/graph1.png
./results/graph2.png
```

### Advanced

* Code directory (`./code/` or `./src/`)
* Documentation file (`./docs/`)
* Manuscript files (`./paper/` or `./doc/paper/`)
