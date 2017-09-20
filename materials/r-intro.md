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

> Create new folder for scripts

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

> Create notes R script, put in new folder

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

* Comment before each problem and each sub-problem

```
# Problem 1

# 1.1
2 + 2

# 1.2
2 - 8

# Problem 2

width = 2
height = 3
length = 1.5
volume = width * height * length
volume
```
> Create assignment script, put in new folder

> Do [Exercise 1 - Basic Expressions]({{ site.baseurl }}/exercises/Expressions-and-variables-basic-expressions-R/)

> Do [Exercise 2 - Basic Variables]({{ site.baseurl }}/exercises/Expressions-and-variables-basic-variables-R/)


### Functions

* A function is basically a complicated expression. It is a command that returns
  a value, but hides the details of how that value is determined. This is useful
  because we typically don't want to look at the details of how numbers are
  rounded or lists of numbers are sorted.

```
abs(-2)
```

* A function call is composed of two parts, the name of the function and the
  arguments that the function requires to calculate the value it returns. In the
  example above `abs()` is the name of the function, and `-2` is the argument.

* Functions can take multiple arguments. For example, if we want to round `pi` to
  two decimal places we would use the round function with the arguments `3.14159`
  and `2`, where the first argument is the number to be rounded and the second
  argument is the number of decimal points to round it to.

```
round(3.14159, 2)
```

* Save the output of a function by assigning it to a variable

```
pi_approx <- round(3.14159, 2)
pi_approx
```

> Do [Exercise 4 - Built-in Functions]({{ site.baseurl }}/exercises/Functions-built-in-functions-R/)

