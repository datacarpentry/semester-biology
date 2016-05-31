---
layout: page
element: notes
title: Project Structure
language: R
--- 

## Simple

* Code: / (single top level script)
* Project File: /
* README: / (description of what you're doing and how to run w/top level script)
* Data: /data (sub dirs if useful)
* Results: /results (sub dirs if useful)

```
/README
/myproject.Rproj
/mydatascript.R
/myanalysisscript.R
/data/datafile1.txt
/data/datafile2.txt
/results/graph1.png
/results/graph2.png
/paper/mypaper.Rmd
/paper/mypaper.pdf
```

## Advanced

* Project file & README: /
* Docs: /doc
* Paper: /paper or /doc/paper
* Code: /src
* Data: /data
* Results: /results
