---
layout: page
title: Walkthrough R
language: R
---

### Basic Workflow

The R environment is broken up into two main windows, the console and the script. The console window is the place where R is waiting for you to tell it what to do, and where it will show the results of a command. `>` mark that R is ready to take a command. `+` means the command is not complete, like you are missing a `)` or `}`. You can type commands directly into the console, but they will be forgotten when you close the session.The script is a simple text (.R) file that stores your code. The point of a well constructed script is not just to "do stuff" but to do it in a way that maintains a complete record of your work so anyone can easily and exactly replicate your workflow and results.

### Basic Operation

- `# this is a comment in R`
- Use `x <- 3` to assign a value, `3`,  to a variable, `x`
   - `=` can also be used, but should be avoided EXCEPT in functions
- R counts from 1, unlike many other programming languages (e.g., Python)
- `length(thing)` returns the number of elements contained in the variable
  `thing`. `dim(thing)` returns length in multiple dimensions.
- `c(value1, value2, value3)` creates a vector
- `container[i]` selects the i'th element from the vector `container`
- `container[[i]]` selects the i'th object from the object `container`
- You'll have to get familiar with the different `class()` of objects:
  - `character` is text
  - `numeric` is numbers
  - `factor` is categories
  - `logical` is TRUE / FALSE
- Objects can be grouped in many ways:
  - `list()`
  - `vector()` or `c()`
  - `matrix()`
  - `data.frame()`


### Control Flow

- Create a conditional using `if`, `else if`, and `else`

		if(x > 0){
			print("value is positive")
		} else if (x < 0){
			print("value is negative")
		} else{
			print("value is neither positive nor negative")
		}

- Create a `for` loop to process elements in a collection one at a time

		for (i in 1:5) {
			print(i)
		}

This will print:

		1
		2
		3
		4
		5


- Use `==` to test for equality
  - `3 == 3`, will return `TRUE`,
  - `'apple' == 'orange'` will return `FALSE`
- `X & Y` is `TRUE` is both X and Y are true
- `X | Y` is `TRUE` if either X or Y, or both are true

### Functions

- Defining a function:

		is_positive <- function(integer_value){
			if(integer_value > 0){
			   TRUE
			else{
			   FALSE
			{
		}

In R, the last executed line of a function is automatically returned, otherwise use `return()` to be sure you know what the function is giving back to you.

- Specifying a default value for a function argument

		increment_me <- function(value_to_increment, value_to_increment_by = 1){
			value_to_increment + value_to_increment_by
		}

`increment_me(4)`, will return 5

`increment_me(4, 6)`, will return 10

- Call a function by using `function_name(function_arguments)`

- apply family of functions: `apply()`,	`sapply()`, `lapply()`,	`mapply()`
   `apply(dat, MARGIN = 2, mean)` will return the average (`mean`) 
   of each column in `dat`


### Packages

- Install package by using `install.packages("package-name")`
- Update packages by using `update.packages("package-name")`
- Load packages by using `library("package-name")`


### Math

Do math by simply typing or pasting in the console.

```
x+y
x*y
x**y
sum(vector)
mean(vector)
round(vector, decimal_places)
```

### Scientific Commands

- Import data using `read.csv(file, header = TRUE, sep = ",", …)`
- Check out what you imported with `names()`, `head()`, and `str()`
- Export results using `write.csv(x, file, …)` 
- Many statistical functions are available (`t.test()`, `lm(y~x)`)

### Finding Help

Don’t be defeated by a coding problem, semantics confusion, or error messages. 
Find help:

`help(function)` or `?function` - Input any function into the parentheses for useful syntax and function information. `args()` gives you the arguments of a function.
 
You can also check out the resources below or run a general engine search (i.e., [r split character string](https://duckduckgo.com/?q=r+split+character+string&t=ffsb&ia=qa)).
The hardest part here is finding the right keywords to use.

### General Resources

#### Manual Directories

- [R-project Intro](http://cran.r-project.org/doc/manuals/R-intro.html)
- [R-project Manual](http://stat.ethz.ch/R-manual/R-devel/library/)
- [base functions](http://stat.ethz.ch/R-manual/R-devel/library/base/html/) 
- [graphics functions](http://stat.ethz.ch/R-manual/R-devel/library/graphics/html/) 
- [statistics functions](http://stat.ethz.ch/R-manual/R-devel/library/statistics/html)

#### R Community Forums

- [R-project.org](http://www.r-project.org/)
- [statmethods.net](http://www.statmethods.net/)
- [R-tutor.com](http://www.r-tutor.com/)
- [R-bloggers.com](http://www.r-bloggers.com/)
- [Programiz](http://www.programiz.com/r-programming)
- [Stackoverflow.com](http://stackoverflow.com/)

#### *[How to ask for help](http://blog.revolutionanalytics.com/2014/01/how-to-ask-for-r-help.html)*


###Style Guides
- [Hadley Wickham](http://r-pkgs.had.co.nz/style.html)
- [Google](https://google-styleguide.googlecode.com/svn/trunk/Rguide.xml)

#### *This document benefited greatly by the inclusion of Data Carpentry materials ([Before we start](http://www.datacarpentry.org/R-ecology-lesson/00-before-we-start.html), [Introduction to R](http://www.datacarpentry.org/R-ecology-lesson/01-intro-to-R.html)) and Software Carpentry's ([Programming with R Reference](http://swcarpentry.github.io/r-novice-inflammation/reference.html))*