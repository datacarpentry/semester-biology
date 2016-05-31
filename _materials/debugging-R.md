---
layout: page
element: notes
title: Debugging
language: R
---

## Setup

**Send `debugging-example-unfixed.R` to students so they can follow along.**

* Start with a new project including `debugging-example-unfixed.R`

## Basic Strategy

* How do we figure out what's wrong with a program
    * Be a scientist
	    * Hypothesis about what is wrong
	    * Make one change that is expected to fix it
		* Check if it worked
		* **Do not change something without a reason**
    * Read the error message
    * Talk through the code (rubber duck programming)
	* Observe what the code is doing


## Observe

*Run*

* Read the error message and try to fix it
* Where did code fail? Show traceback
* Read the code
* Look at the current state of the environment
* This gives us a snapshot of what's going on in the code
* Can't see inside the function


## Run line by line

* Run the code line by line checking each step
* Trick once functions are involved


## Print statements
* Show us things that we can't see after error
    * Dynamic changes in code
	* Things inside functions

*`print(head(df))`, fix by passing `data_size_class`*  
*Run*  
*Something seems weird about these results*
	

## Debugger

* Like a print statement but better
* Doesn't accidentally get left in the code
* Contains a complete snapshot of the status of the program
* Let's you walk through the code dynamically


### Break points

1. Insert breakpoint
2. Source the code
3. Program runs until breakpoint and stops (before executing the line of code)
4. Environment gives the current values for all variables (Local
   vs. Global). Can switch scopes with dropdown.


### Stepping

* Next: runs next line of code. does not enter functions
* Step Into: goes line by line through the code including entering functions
* Step Out: leaves the current function or loop return to whatever called it
* Continue: continues to the next breakpoint


## Bugs

* passes `data` instead of `data_size_class`
* not using `threshold`
* not passing `threshold`
