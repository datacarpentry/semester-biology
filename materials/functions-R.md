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
add <- function(a, b) {
  total <- a + b
  return(total)
}
```

* Creating a function doesn't run it.
* Call the function with some arguments.

```
add(2, 3)
summed <- add(2, 3)
```

> * Do [Exercise 1 - Use and Modify]({{ site.baseurl }}/exercises/Functions-use-and-modify-R), Tasks 1-2.

* Treat functions like a black box.
    * Can't access a variable that was created in a function
        * `> a`
        * `Error: object 'a' not found`
    * 'Global' variables can influence function, but should not.
        * Very confusing and error prone to use a variable that isn't passed in
          as an argument
    * Defaults can be set for common inputs.

```
add <- function(a=1, b=2) {
  total <- a + b
  return(total)
}

add()
add(b=3)
add(4, 5)
```

* NOT

```
a <- 1
b <- 2

add <- function() {
  total <- a + b
  return(total)
}
```

> Do [Exercise 1 - Use and Modify, Task 3]({{ site.baseurl }}/exercises/Functions-use-and-modify-R)
> and [Exercise 2 - Writing Functions]({{ site.baseurl }}/exercises/Functions-writing-functions-R).
>
> *Discuss what passing `a` and `b` in is much more useful than having them
> fixed*

### Nesting Functions

* Functions can be used to organize, manipulate, or group other functions.
    * The `do_something()` in our basic function can be anything.
        * math
        * built-in function
        * self-written function 

```
make_pie_filling <- function(stuff) {
  filling <- pi * stuff
  return(filling)
}
```

```
make_pie <- function(stuff, crust) {
  pie <- crust + make_pie_filling(stuff)
  return(pie)
}
```

> Do [Exercise 3 - Nested Functions]({{ site.baseurl }}/exercises/Functions-nested-functions-R).
