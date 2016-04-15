---
layout: page
element: notes
title: Functions
language: R
---

Package things into understandable chunks & reuse code easily.

### Chunks

* human brain can only hold ~7 things in memory
* want to only have to understand pieces of programs with no more than ~7
things
* what do you know about how `sum(1:5)` works internally? - Nothing
* lets us ignore the details and reduce `sum` to a single conceptual chunk
* want our functions to work this way too.

### Reuse

* Want to do the same thing repeatedly
* Inefficient to copy code
* if it occurs in more than one place it will eventually be wrong somewhere

### Function basics

```
function_name <- function(inputs){
  commands
  return(output_value)
}
```

```
add <- function(a, b){
  total = a + b
  return(total)
}
```

* creating a function doesn't run it
* call the function with some arguments

```
add(2, 3)
summed <- add(2, 3)
```

* treat functions like a black box
* can't access a variable that was created in a function

```
a
b
```

* very confusing and error prone to use a variable that isn't passed in as a
  argument
