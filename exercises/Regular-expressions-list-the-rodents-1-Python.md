---
layout: exercise
topic: Regular Expressions
title: List the Rodents 1
language: Python
---

There are many diverse sources of biological data in the modern world,
but not all of them are nicely cultivated into well structured data. For
a project you're working on you need a list of all of the rodent species
in the world. You find a great list of rodents by following [the first
link](http://en.wikipedia.org/wiki/List_of_rodents) on a Google search
for *List of Rodents*.

Unfortunately it's in HTML and scraping HTML is generally considered to
be a bit of a nightmare. Fortunately it's a Wikipedia article and
Wikipedia has a nice feature to let us see the source code (or wiki
markup) that is used to build the HTML. This is same as what we would
see if we clicked on the Edit tab of the article, but accessible in a
simple text file. This can be done using the general url:

`http://en.wikipedia.org/w/index.php?title=PAGETITLE&action=raw`

where `PAGETITLE` is replaced with the actual title of the page.

Download the wiki markup and write a short script using regular
expressions that extracts the list of all latin binomials from the page.
Export this list as a text file, one species per line, with genus and
species separated by a comma.
