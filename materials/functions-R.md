---
layout: page
element: notes
title: Functions
language: R
---

### Understandable and reusable code

* Write code in understandable chunks.
* Write reusable code.

### Understandable chunks

* Human brain can only hold ~7 things in memory.
    * Write programs that don't require remembering more than ~7 things at once.
* What do you know about how `sum(1:5)` works internally?
    * Nothing.
    * Ignore the details and reduce `sum()` to a single conceptual chunk.
* All functions should work as a single conceptual chunk.

### Reuse

* Want to do the same thing repeatedly?
    * Inefficient & error prone to copy code
    * If it occurs in more than one place, it will eventually be wrong somewhere.
* Functions are written to be reusable.

### Function basics

```
function_name <- function(inputs) {
  output_value <- do_something(inputs)
  return(output_value)
}
```

* The braces indicate that the lines of code are a group that gets run together

```r
{a = 2
b = 3
a + b}
```

* Pressing run anywhere in this group runs all the lines in that group
* A function runs all of the lines of code in the braces
* Using the arguments provided
* And then returns the output

```
calc_shrub_vol <- function(length, width, height) {
  volume <- length * width * height
  return(volume)
}
```

* Creating a function doesn't run it.
* Call the function with some arguments.

```r
calc_shrub_vol(0.8, 1.6, 2.0)
```

* Store the output to use it later in the program

```r
shrub_vol <- calc_shrub_vol(0.8, 1.6, 2.0)
```

> Do [Writing Functions]({{ site.baseurl }}/exercises/Functions-writing-functions-R)

* Treat functions like a black box
  * *Draw a box on board showing inputs->function->outputs*
  * The only things the function knows about are the inputs we pass it
  * The only thing the program knows about the function is the output it
    produces

* Walk through function execution (using debugger)
    * Call function
	* Assign 0.8 to length, 1.6 to width, and 2.0 to height inside function
	* Calculate volume
	* Send the volume back as output
	* Store it in `shrub_vol`

* Treat functions like a black box.
    * Can't access a variable that was created in a function
        * `> volume`
        * `Error: object 'width' not found`
    * Or an argument by name
        * `> width`
        * `Error: object 'width' not found`
    * 'Global' variables can influence function, but should not.
        * Very confusing and error prone to use a variable that isn't passed in
          as an argument

> Do [Use and Modify]({{ site.baseurl }}/exercises/Functions-use-and-modify-R).
> End of 1 hour class

### Default arguments

* Defaults can be set for common inputs.

```
calc_shrub_vol <- function(length = 1, width = 1, height = 1) {
  volume <- length * width * height
  return(volume)
}

calc_shrub_vol()
calc_shrub_vol(width = 2)
calc_shrub_vol(0.8, 1.6, 2.0)
calc_shrub_vol(height = 2.0, length = 0.8, width = 1.6)
```

> Do [Default Arguments]({{ site.baseurl }}/exercises/Functions-default-arguments-R).

> *Discuss why passing `a` and `b` in is more useful than having them fixed*

### Named vs unnamed arguments

* When to use or not use argument names

```
calc_shrub_vol(length = 2.0, width = 0.8, height = 1.6)
```

Or

```
calc_shrub_vol(2.0, 0.8, 1.6)
```

* You can always use names
    * Value gets assigned to variable of that name
* If not using names then order determines naming
    * First value is `length`, second value is `width`, third value is `height`
    * If order is hard to remember use names
* In many cases there are *a lot* of optional arguments
    * Convention to always name optional argument

### Combining Functions

* Each function should be single conceptual chunk of code
* Functions can be combined to do larger tasks in two ways

* Calling multiple functions in a row

```r
est_shrub_mass <- function(volume){
  mass <- 2.65 * volume^0.9
}

shrub_volume <- calc_shrub_vol(0.8, 1.6, 2.0)
shrub_mass <- est_shrub_mass(shrub_volume)
```

* We can also use pipes with our own functions
* The output from the first function becomes the first argument for the second function

```r
library(dplyr)
shrub_mass <- calc_shrub_vol(0.8, 1.6, 2.0) %>%
  est_shrub_mass()
```

> Do [Combining Functions]({{ site.baseurl }}/exercises/Functions-combining-functions-R).

* We can nest functions

```r
shrub_mass <- est_shrub_mass(calc_shrub_vol(0.8, 1.6, 2.0))
```

* But we careful with this because it can make code difficult to read
* Don't nest more than two functions

* Can also call functions from inside other functions
* Allows organizing function calls into logical groups

```
est_shrub_mass_dim <- function(length, width, height){
  volume = calc_shrub_vol(length, width, height)
  mass <- est_shrub_mass(volume)
  return(mass)
}

est_shrub_mass_dim(0.8, 1.6, 2.0)
```

* We ***don't*** need to pass the function name into the function
* That's the one violation of the black box rule

### Documentation & Comments

* Documentation
    * How to use code
    * Use Roxygen comments for functions
* Comments
    * Why & how code works
    * Only if it code is confusing to read

### Working with functions in RStudio

* It is possible to find and jump between functions
* Click on list of functions at bottom of editor and select

* Can be helpful to clearly see what is a function
* Can have RStudio highlight them
*  Global Options -> Code -> Display -> Highlight R function calls
