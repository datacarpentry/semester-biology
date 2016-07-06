---
layout: page
element: notes
title: Debugging
language: R
---

> Remember to
>
> * send `debugging-example-unfixed.R` to students so they can follow along.
> * set up a new `Git` project that includes `debugging-example-unfixed.R`.

## Basic Manual Debugging Strategy

* How do we figure out what's wrong with a program?
    * Be a scientist.
        * Hypothesize about what is wrong.
        * Make one change that is expected to fix error.
        * Check if change worked/fixed error.
    * Read the error message.
    * Talk through the code
        * Observe what the code is doing
        * [Rubber duck programming](https://en.wikipedia.org/wiki/Rubber_duck_debugging)
    * **Do not change something without a reason.**

### Observe

> Run `debugging-example-unfixed.R`.

* Read the error message and try to fix it.
* Where did code fail? 
    * Traceback
* Read the code.
* Look at the current state of the environment.
    * This gives us a snapshot of what's going on in the code
    * Can't see variables inside the function

### Run line by line

* Run the code line by line checking each step.
* More difficult once functions are involved.
    * Isolate functions.
    * Use `print()`.

### `print()` statements
* Show us things that we can't see after error
    * Dynamic changes in code
    * Things inside functions

```
print(head(df))
``` 

> Fix error by passing `data_size_class` instead of `data`.
> Run `debugging-example-unfixed.R`.  

* Something seems weird about these results
    * difficult to tell with manual strategy	

## Debugger

* Advanced error visualization (`print()`) technique
* Doesn't accidentally get left in the code
* Contains a complete snapshot of the status of the program
* Let's you walk through the code dynamically


### Break points

1. Insert breakpoint
2. Source the code
3. Program runs until breakpoint and stops ( *before executing the line of code* )
4. Environment gives the current values for all variables 
    * Local and global 
    * Can switch scopes with dropdown

### Stepping

* `Next` 
    * runs next line of code 
    * does not enter functions
* `Step Into` 
    * goes line by line through the code including entering functions
* `Step Out` 
    * leaves the current function or loop 
    * returns to whatever called it
* `Continue` 
    * continues to the next breakpoint

### Bugs to fix

* passes `data` instead of `data_size_class`
* not using `threshold`
* not passing `threshold`
