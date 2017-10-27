---
layout: page
element: notes
title: Conditionals
language: R
---

> INSTRUCTOR NOTE: Code examples should generally build up by modifying the
> existing code example rather than by retyping the full example.

### Conditionals

* Usage: 
    * Generate `"logical"`:
        * `TRUE` if the condition is satisfied 
        * `FALSE` if the condition is not satisfied
* Operators:
    * `==`, `!=`
    * `<`, `>`
    * `<=`, `>=`

```
10 > 5
"aang" == "aang"
3 != 3
```

* Combine:
    * `and`, `&` 
    * `or`, `|`

```
5 > 2 & 6 >=10
5 > 2 | 6 >=10
```

* Appearances:
    * `subset()`
    * `dplyr::filter()`
    * `if()`, `else`, `while()`

> Do [Choice Operators]({{ site.baseurl }}/exercises/Making-choices-choice-operators-R).

> Discuss floating point with students.
>
> * Did you notice anything weird while you were doing the exercise?
> * Take a closer look at item 4.

### Floating point

```
> x <- 1.3
> y <- 2.8
>  x * 2 + 0.2 == y
[1] FALSE
> 1.3 * 2 + 0.2
[1] 2.8
```

* What's going on?
    * Unexpected result from computer arithmetic
    * Numbers combine to include very small trailing digit  
        * See this more easily in Python

```
>>> 1.3 * 2 + 0.2 == 2.8
False
>>> 1.3 * 2 + 0.2
2.8000000000000003
```

* Avoid floating point problems.
    * `round(x * 2 + 0.2, 1) == y`
    * `all.equal(x * 2 + 0.2, y)`

### `if` statements

* Conditional statements generate `"logical"` to filter inputs.
* `if` statements use conditional statements to control flow of program processing.
* `if (the conditional statement is TRUE ) { do something }`

* Different mass calculations for different vegetation types

```
veg_type <- "tree"
volume <- 16.08
if (veg_type == "tree") {
  mass <- 2.65 * volume^0.9
  }
print(mass)
```

```
veg_type <- "shrub"
```

* `} else { do something else }`

```
if (veg_type == "tree") {
  mass <- 2.65 * volume^0.9
} else {
  print("I don't know how to convert volume to mass for that vegetation type")
  mass <- NA
}
print(mass)
```

* `} else if ( a different conditional statement is TRUE ) {` 
    * do something else

```
if (veg_type == "tree") {
  mass <- 2.65 * volume^0.9
} else if (veg_type == "grass") {
  mass <- 0.65 * volume^1.2
} else {
  print("I don't know how to convert volume to mass for that vegetation type")
  mass <- NA
}
print(mass)
```

```
veg_type = "liana"
```

> Do [Simple If Statement]({{ site.baseurl }}/exercises/Making-choices-simple-if-statement-R).

## Convert to function

```
est_mass <- function(volume, veg_type){
  if (veg_type == "tree") {
	mass <- 2.65 * volume^0.9
  } else if (veg_type == "grass") {
	mass <- 0.65 * volume^1.2
  } else {
	print("I don't know how to convert volume to mass for that vegetation type")
	mass <- NA
  }
  return(mass)
}

est_mass(1.6, "tree")
est_mass(1.6, "grass")
est_mass(1.6, "shrub")
```

> Do [Complete the Code]({{ site.baseurl }}/exercises/Making-choices-complete-the-code-R).


* Can use more complex conditions

```
est_mass <- function(volume, veg_type, age){
  if (veg_type == "tree") {
    if (age < 5) {
	  mass <- 1.6 * volume^0.8
	} else {
	  mass <- 2.65 * volume^0.9
	}
  } else if (veg_type == "grass" | veg_type == "shrub") {
	mass <- 0.65 * volume^1.2
  } else {
	print("I don't know how to convert volume to mass for that vegetation type")
	mass <- NA
  }
  return(mass)
}

est_mass(1.6, "tree", age = 2)
est_mass(1.6, "shrub", age = 5)
```

* First checks if the vegetation type is "tree"
* If it is checks to see if it is < 5 years old
* If so does one calculation, if not does another
* But nesting can be difficult to follow so try to minimize it

> Do [Choices with Functions]({{ site.baseurl }}/exercises/Making-choices-choices-with-functions-R).
