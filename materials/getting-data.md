---
layout: page
element: notes
title: Getting Data
language: R
--- 

> Have students install Python (if using Data Retriever)

## Types of data access

* Variety of ways in which data is made publicly available
* We've seen many of these and will talk about more today

### Direct Downloads

* Website that lets you download data
    * Dataset specific
    * General data archive
    * Aggregator for specific kinds of data
* Ideally an unchanging url
* Sometimes requires point and click interface to get data
* Examples
    * Data paper: https://www.nature.com/articles/sdata2018165
    * NEON website: http://data.neonscience.org/static/browse.html 

### APIs

* Programmatically access data over the web
* Typically allows choosing subsets of data
* Specially structured urls
* Mostly used through packages that "wrap" the APIs
* E.g., used `spocc` which include multiple API wrappers for occurrence data
* One of those sources is the GBIF with the `rgbif` API wrapper

```
install.packages('rgbif')
library('rgbif')
rgbif::occ_search(scientificName = "Ursus americanus", limit = 50)
rgbif::occ_search(scientificName = "Ursus americanus", limit = 50,
                  fields=c('name','decimalLatitude','decimalLongitude'))
```

### Data Packages

* An R package that contains data

```
install.packages('gapminder')
library('gapminder')
gapminder
```

* Also some non-R specific versions
    * `datapackage-r`

### Data Retrievers

* Software that acquires data from other sources
* Sometimes cleans and restructures that data as well
* `retriever`

* Go to https://www.python.org/downloads
* Click the yellow `Download Python` button
* Start the installer
* Click "Add Python 3.7 to PATH" then "Install Now"

* In RStudio
    * Terminal: `pip install retriever`
    * Console: `install.packages('rdataretriever')`

```
library(rdataretriever)
get_updates()
install('breed-bird-survey', 'csv')
counts <- read.csv("breed_bird_survey_counts")
mammal_masses <- fetch("mammal-masses")
mammal_masses$
```

## Licenses

* What can you do with the data
* Creative Commons
    * CC0:  Anything at all
    * CC-BY: Anything you want, but you must cite the source
    * CC-BY-SA: If you build on it you must redistribute with the same license
    * CC-BY-NC: Only available for non-commercial use (but this is tricky)
* Roll your own licenses
* Data may not even be copyrightable
* Important express of how folks would like their public data used


## Citing data

* Many datasets specificy how to cite them
* If published as data papers cite the paper
* If published on an archiving site there will be a link for how to cite
* Often request acknowledgements as well
