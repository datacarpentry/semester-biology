---
layout: page
element: notes
title: Introduction to R
language: R
---

> Remind students to install R and RStudio.

> Have students open RStudio and check to see if console "sees" R.

### R

* Programming language
* Statistics and data analysis environment


### RStudio

* IDE - Integrated Development Environment
    * Interpreter/Console
    * Text editor
        * object highlighting 
        * information about problems with code
        * `tab` key autocompletes
            * Let the computer do repetitious work. 
            * It's easier and with fewer mistakes.
    * Environment/History
    * Project management

> Demo
>
> * working directly in interpreter.
> * writing code and running it from the editor.
> * clearing the global environment.
> * Integrated help (start typing, `F1` for more info).


### Projects

* Who here uses `setwd()`?
* Start a new project
* Create a `data` subdirectory
* Add an example `.CSV` file
* Load it

### Project structure

* Two common structures
* code in top-level directory with subdirectories for data, results, etc
  ( *possibly with subdirectories of their own* )
* code in a separate subdirectory

### Assignments format

* Output:
    * `cat("1: ", answer)`
    * `cat("1.1: ", answer)`
* Comment before each problem:
    * `# Problem 1`
