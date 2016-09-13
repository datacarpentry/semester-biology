---
layout: page
element: notes
title: Debugging
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
    * Can't see variables inside the function

### Run line by line

* Run the code line by line checking each step.
* More difficult once functions are involved
    * Use `print()` to verify input and output.
    * Run function with simplified input.
    * Write test script that separates function from other code chunks.

### `print()` statements
* Shows us things that we can't see after error
    * Dynamic changes in code (e.g., `for` loop objects)
    * Things inside functions

```
print(head(df))
``` 

> Fix error by passing `data_size_class` instead of `data`.
> Run `debugging-example-unfixed.R`.  

* Something seems weird about these results.
    * Difficult to tell with manual strategy	

## Debugger

* Like a `print()` statement, but better
    * Contains a complete snapshot of the status of the program
    * Let's you walk through the code dynamically
    * Doesn't accidentally get left in the code

### Break points

1. Insert breakpoint.
2. Source the code.
3. Program runs until breakpoint and stops (*before executing the line of code*).
4. Environment gives the current values for all variables. 
    * Local and global 
    * Can switch scopes with dropdown

### Stepping

* `Next` 
    * Runs next line of code 
    * Does not enter functions
* `Step Into` 
    * Goes line by line through the code including entering functions
* `Step Out` 
    * Leaves the current function or loop 
    * Returns to whatever called it
* `Continue` 
    * Continues to the next breakpoint

### Bugs to fix

* Passes `data` instead of `data_size_class`
* Not using `threshold`
* Not passing `threshold`
