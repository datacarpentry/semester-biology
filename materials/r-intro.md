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


### Basic expressions

* Write code directly in the interpreter

```
2 + 5
4 * 2 / 3
```

* Write code in text editor and the run either by line or all code

```
2 + 5
4 * 2 / 3
```

* `Source` vs `Source with Echo`


### Types

* All values have types

```
str(2)
str('hello world')
```

### Variables

* A variable is a name that has a value associated with it
    * Assign using `<-` or `=`

```
weight <- 26
```

* It works just like the value itself

```
double_weight <- weight * 2
```

* It won't change unless you assign a new value to it directly

```
weight
weight * 2
weight
weight <- 22
weight
```

### Assignments format

* Output:
    * `cat("1: ", answer)`
    * `cat("1.1: ", answer)`
* Comment before each problem:
    * `# Problem 1`
