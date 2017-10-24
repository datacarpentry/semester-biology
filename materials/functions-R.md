---
layout: page
element: notes
title: Functions
language: R
---

### Understandable and reusable code

* Write code in understandable chunks.
    * Clear variable names
    * Consistent indentation and line spacing
    * Good commenting
    * Functions
* Write reusable code.
    * Concise and modular script
    * Functions with general structure 

### Understandable chunks

* Human brain can only hold ~7 things in memory.
    * Write programs that don't require remembering more than ~7 things at once.
* What do you know about how `sum(1:5)` works internally?
    * Nothing.
    * Ignore the details and reduce `sum()` to a single conceptual chunk.
* All functions should work as a single conceptual chunk.

### Reuse

* Want to do the same thing repeatedly?
    * Inefficient to copy code
    * If it occurs in more than one place, it will eventually be wrong somewhere.
* Functions are written to be reusable.

### Function basics

```
function_name <- function(inputs) {
  output_value <- do_something(inputs)
  return(output_value)
}
```

```
calc_shrub_vol <- function(length, width, height) {
  volume <- length * width * height
  return(volume)
}
```

* Creating a function doesn't run it.
* Call the function with some arguments.

```
calc_shrub_vol(0.8, 1.6, 2.0)
shrub_vol <- calc_shrub_vol(0.8, 1.6, 2.0)
```

* Walk through function execution
    * Call function
	* Assign 0.8 to length, 1.6 to width, and 2.0 to height inside function
	* Calculate volume
	* Send the volume back as output
	* Store it in `shrub_vol`

> Do [Writing Functions]({{ site.baseurl }}/exercises/Functions-writing-functions-R).

* Treat functions like a black box.
    * Can't access a variable that was created in a function
        * `> a`
        * `Error: object 'a' not found`
    * 'Global' variables can influence function, but should not.
        * Very confusing and error prone to use a variable that isn't passed in
          as an argument
    * Don't do this

```
length <- 1
width <- 2
height <- 3

calc_shrub_vol <- function() {
  volume <- length * width * height
  return(volume)
}
```

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

> Do [Use and Modify]({{ site.baseurl }}/exercises/Functions-use-and-modify-R).
>
> * Discuss why passing `a` and `b` in is more useful than having them fixed*


### Combining Functions

* Each function should be single conceptual chunk of code
* Functions can be combined to do larger tasks in two ways

* Calling multiple functions in a row

```
est_shrub_mass <- function(volume){
  mass <- 2.65 * volume^0.9
}

shrub_mass <- est_shrub_mass(calc_shrub_vol(0.8, 1.6, 2.0))

library(dplyr)
shrub_mass <- calc_shrub_vol(0.8, 1.6, 2.0) %>%
  est_shrub_mass()
```

* Calling functions from inside other functions
* Allows organizing function calls into logical groups

```
est_shrub_mass_dim <- function(length, width, height){
  volume = calc_shrub_vol(length, width, height)
  mass <- est_shrub_mass(volume)
  return(mass)
}

est_shrub_mass_dim(0.8, 1.6, 2.0)
```

> Do [Nested Functions]({{ site.baseurl }}/exercises/Functions-nested-functions-R).
