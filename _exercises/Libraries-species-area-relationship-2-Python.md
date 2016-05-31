---
layout: exercise
topic: Libraries
title: Species Area Relationship 2
language: Python
---

This is a follow up to the [Species Area Relationship]({{ site.baseurl }}/exercises/Higher-order-functions-species-area-relationship-1-Python) problem.

After writing a program to estimate the number of species at a site of a
given area based on the average predictions of a suite of different
species-area relationship equations, you realize that as you add more
and more equations (remember, we might eventually want at least 20) it's
going to increasingly clutter your code. In addition, many of the
equations aren't really specific to the species-area relationship itself
and so you'd like to be able to use them in some of your projects
related to population growth.

Create a new module called *yourname*\_equations.py (where *yourname*
is, creatively enough, replaced with your name). Move all of the
equations into that module. Add a docstring to the module itself and for
each individual function (these can be quite short). Modify your main
program to use these functions by importing your new module.

*Optional*: If you're feeling bold, add some commands to the module so
that if someone tries to execute it directly it just prints out the
sentence: “This is just a bunch of equations for use by other programs.
It doesn't do anything on its own. TTFN.” (but make sure it doesn't do
this if it's imported as a library). Then modify your main program to
check for command line arguments. If arguments are present have your
code treat each of them as an area and print an estimate of species
richness for each area to the screen. If no arguments are present have
your code print the answers to all of the home work problems.
