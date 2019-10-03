---
layout: page
element: notes
title: Basic Debugging
language: R
---

> Remember to
>
> * download [`debugging-example-unfixed.R`]({{ site.baseurl }}/code/debugging-example-unfixed.R) and [`debugging-example-fixed.R`]({{ site.baseurl }}/code/debugging-example-fixed.R).
> * send `debugging-example-unfixed.R` to students so they can follow along.
> * set up a new `Git` project that includes `debugging-example-unfixed.R`.

## Basic Manual Debugging Strategy

* How do we figure out what's wrong with a program?
    * Be a scientist.
        * Hypothesize about what is wrong.
        * Make one change that is expected to fix error.
        * Check if change worked/fixed error.
    * Read the error message.
    * Talk through the code.
        * Observe what the code is doing.
        * [Rubber duck programming](https://en.wikipedia.org/wiki/Rubber_duck_debugging)
    * **Do not change something without a reason.**

### Observe

> Run `debugging-example-unfixed.R`.

* Read the error message and try to fix it.
* Where did code fail? 
    * Traceback
    * `options(error = tamper::tamper)` helps with pipes (`%>%`)
* Read the code.
* Look at the current state of the environment.
    * This gives us a snapshot of what's going on in the code.
* Run the code line by line checking each step.
