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
* Makes developing code in R easier by including a number of tools in one place
* Interpreter/Console is where R is actually running
    * Can work in here "interactively"
    * Run a single command and see the result
    * `2 + 2`
    * This is also where RStudio will run code written in the text editor
* Text editor
    * Where we write code we want to keep and potentially reuse later
    * Creates a plain text file that stores the code we've written
    * We can open it by clicking the `New File` button or using the `Ctrl-Shift-N` keyboard shortcut (`Cmd-Shift-N`) on Mac

### RStudio Cloud

* An online version of RStudio that runs in your browser
* We're using it because it:
  1. Avoids installation difficulties
  2. Makes sharing code with instructors for debugging easier
  3. Let's us leave some of the complexities of working with R until after we've learned the basics
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

* _Write code directly in the text editor_
* Kangaroo rat weight (g -> lb)

```R
50 / 1000 * 2.2
```

* This is called an expression
* A set of commands that returns a value

* Run line
* Run selection
* `Source` & `Source with Echo`

* Save as `krat_weight_analysis.R`
* Can see in the `Files` tab that we've created this file 
* We can also use this tab to create, delete, and rename files & folders

### Variables

* To save the values we calculate for later use we use variables 
* A variable is a name that has a value associated with it
    * Assign using `<-` or `=`

```
weight_g <- 50
weight_g = 50
```

* We can see that this variable has been created by looking in the Environment tab

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

### RStudio tips

* `tab` key autocompletes
    * _Type `wei` and then tab_
    * Let the computer do repetitious work. 
    * It's easier and with fewer mistakes.
* And a history of the commands you've run under `History` in case you forgot to write something down

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

> Do [Exercise 1.1-1.3 - Basic Expressions]({{ site.baseurl }}/exercises/Expressions-and-variables-basic-expressions-R/)

> Do [Exercise 2 - Basic Variables]({{ site.baseurl }}/exercises/Expressions-and-variables-basic-variables-R/)


### Functions

* A function is a complicated expression.
* Command that returns a value

```
sqrt(49)
```

* A function call is composed of two parts.
    * Name of the function
    * Arguments that the function requires to calculate the value it returns.
    * `sqrt()` is the name of the function, and `49` is the argument.
* We can also pass variables as the argument

```r
weight_lb <- 0.11
sqrt(weight_lb)
```

* Another function that we'll use a lot is `str()`
* All values and therefore all variables have types
* `str`, short for "structure", lets us look at them

```r
str(weight_lb)
```

* Another data type is for text data
* We right text inside of quotation makes

```r
"hello world"
```

* If we look at the structure of some text we see that it is type character

```r
str("hello world")
```

* Functions can take multiple arguments.
    * Round `weight_lb` to one decimal place
    * Typing `round()` shows there are two arguments
    * Number to be rounded and number of digits

```r
round(weight_lb, 1)
```

* Functions return values, so as with other values and expressions, if we don't save the output of a function then there is no way to access it later
* It is common to forget this when dealing with functions and expect the
  function to have changed the value of the variable
* But looking at `weight_lb` we see that it hasn't been rounded

```r
weight_lb
```

* To save the output of a function we assign it to a variable.

```r
weight_rounded <- round(weight_lb, 1)
weight_rounded
```


> Do [Exercise 4.1-4.3 - Built-in Functions]({{ site.baseurl }}/exercises/Functions-built-in-functions-R/)