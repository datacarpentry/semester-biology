---
layout: page
element: notes
title: Introduction to R
topic: R
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
* Kangaroo rat weight (g -> lb)

```
50
50 / 1000
50 / 1000 * 2.2
```

* Write code in text editor and run either by line or all code

```
50
50 / 1000
50 / 1000 * 2.2
```

* `Source` vs `Source with Echo`

> Create notes R script, put in new folder


### Variables

* A variable is a name that has a value associated with it
    * Assign using `<-` or `=`

```
weight_g <- 50
```

* It works just like the value itself

```
weight_g / 1000
weight_g / 1000 * 2.2
weight_lb = weight_g / 1000 * 2.2
```

* It won't change unless you assign a new value to it directly

```
weight_g
weight_g * 2
weight_g
weight_g <- 26
weight_g
```

### Comments

* Remember what code is doing
* For humans, not computers
* Use the `#`

```
# Calculate weight of Kangaroo Rat in pounds
```

### Assignments format

* Comment before each problem and each sub-problem
* Make sure result prints out on `Source with echo`

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

> Do [Exercise 1.1-1.3 - Basic Expressions]({{ site.baseurl }}/exercises/Expressions-and-variables-basic-expressions-R/)

> Do [Exercise 2 - Basic Variables]({{ site.baseurl }}/exercises/Expressions-and-variables-basic-variables-R/)


### Functions

* A function is a complicated expression.
* Command that returns a value
* Hides the details of how that value is determined.
* Useful - don't want to know how numbers are rounded

```
sqrt(weight_lb)
sqrt(0.11)
```

* A function call is composed of two parts.
    * Name of the function
    * Arguments that the function requires to calculate the value it returns.
    * `sqrt()` is the name of the function, and `0.11` is the argument.

* Functions can take multiple arguments.
    * Round `weight_lb` to one decimal place
    * Typing `round()` shows arguments
    * Number to be rounded and number of digits

```
round(0.11, 1)
round(weight_lb, 1)
```

* Save the output of a function by assigning it to a variable

```
weight_rounded <- round(weight_lb, 1)
weight_rounded
```

> Do [Exercise 4.1-4.3 - Built-in Functions]({{ site.baseurl }}/exercises/Functions-built-in-functions-R/)

* If you don't save the output of a function then there is no way to access it

```
mass_kg <- 0.5163
round(mass_kg, 2)
```

* It is common to forget this when dealing with variables and expect the
  variable to have changed

```
mass_kg
```

### Types

* All values have types

```
str(weight_lb)
str('hello world')
```