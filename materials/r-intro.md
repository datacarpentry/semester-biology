---

layout: page
element: notes
title: Introduction to R
language: R
---

> Remind students to install R and RStudio or setup access to RStudio Cloud/Server

> Have students open RStudio and check to see if console "sees" R.

### Logging into RStudio Cloud

* Open a browser
* Go to https://rstudio.cloud/
* ...


### R

* Programming language
* Started as a statistics and data analysis environment
* But can also build websites, run simulations, and lots of other things
* R is what runs all of the code we will write this semester
* Separate from RStudio

### RStudio

* IDE - Integrated Development Environment
* Makes developing code in R easier
* It includes a number of different aspects of code development in one place
* Interpreter/Console is where R is actually running
    * Can work in here "interactively"
    * Run a single command and see the result
    * `2 + 2`
    * This is also where RStudio will run code written in the text dditor
* Text editor
    * Where we write code we want to keep and potentially reuse later
    * Creates a plain text file that stores the code we've written
    * Does a number of things to make writing clean code easier including
        * Object highlighting to makes it easier to see different things in the code
        * Automatically pairing `""` and `{}`
        * Automatically indenting code
        * Flagging issues with code
        * Autocompleting function and variable names
    * `tab` key autocompletes
        * Let the computer do repetitious work. 
        * It's easier and with fewer mistakes.
* It provides information on the variables that currently exist and their values under Environment
* And a history of the commands you've run under `History` in case you forgot to write something down
* Project management
    * Create, delete, and rename files & folders
    * Projects to help code know where other files like data files are located

> Create new folder for scripts

### RStudio Cloud

* An online version of RStudio that runs in your browser
* We are going to try using this this year for four reasons
  1. Everything should work for everyone, there shouldn't be installation issues or other complexities that come from differences between computers
  2. Code is automatically shared with instructors so we can help you figure out why things aren't working. This is the closest approximation to working side by side with you in the classroom that I've been able to find.
  3. We can leave some of the complexities of working with R until after we've learned the basics
  4. Works on tablets as well as computers
* Folks with limited internet access, please checkout the video on working with RStudio installed on your own computer

#### RStudio Cloud in Class

* All work for this class will be done in a class workspace
* To join this space follow the link provided via Canvas and sign in using your UF email address
* When you open RStudio Cloud click on the three lines in the top corner and select `Data Carpentry` from `Spaces`
* Click on the appropriate week, which should say `Start` by it the first time you open it
* This is your own copy of the assignment, which should include everything you need to both follow along with the lessons and complete the assignment
* This is also where we can come look at your code to help if you get stuck
* If you want to start a separate project, not for class, just click on `New Project` instead

### Basic expressions

* Write code directly in the text editor

```
2 + 2
```

* This is called an expression
* A set of commands that returns a value

* Kangaroo rat weight (g -> lb)

```
50
50 / 1000
50 / 1000 * 2.2
```

* Run line
* Run selection
* `Source` & `Source with Echo`

* Save as `krat_weight_analysis.R`


### Variables

* To save the values we calculate for later use we use variables 
* A variable is a name that has a value associated with it
    * Assign using `<-` or `=`

```
weight_g <- 50
weight_g = 50
```

* It works just like the value itself

```
weight_g / 1000
weight_g / 1000 * 2.2
weight_lb <- weight_g / 1000 * 2.2
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

* Now we're going to work on some exercises to get a feel for this
* In class we will often only do part of an exercise and save the rest for later
* I use an in-class feedback system to get a feel for when most folks are done
  and how well folks understand the material
* When you are done with the part of the exersise we are doing for class, click
  on the `In class feedback` link and fill out the poll
* Two sections
  * 1-5 rating for how well you understand what we just covered
  * A text box to describe anything confusing you if you can describe it
  * 4 and 5's indicate that you're following things and we can move on
  * 3's and below suggest we need to chat more 

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

* Another function that we'll use a lot is `str()`
* All values and therefore all variables have types
* `str`, short for "structure", lets us look at them

```
str(weight_lb)
str(10)
str('hello world')
```

* Functions can take multiple arguments.
    * Round `weight_lb` to one decimal place
    * Typing `round()` shows there are two arguments
    * Number to be rounded and number of digits

```
round(0.11, 1)
round(weight_lb, 1)
```

* Arguments return values, so as with other values, if we don't save the output of a function then there is no way to access it later
* It is common to forget this when dealing with functions and expect the
  function to have changed the value of the variable
* But looking at `mass_lb` we see that it hasn't been rounded

```
mass_lb
```

* To save the output of a function we assign it to a variable.

```
weight_rounded <- round(weight_lb, 1)
weight_rounded
```


> Do [Exercise 4.1-4.3 - Built-in Functions]({{ site.baseurl }}/exercises/Functions-built-in-functions-R/)