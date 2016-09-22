---
layout: page
element: notes
title: Conditionals
language: R
---

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

> Do [Exercise 1 - Choice Operators]({{ site.baseurl }}/exercises/Making-choices-choice-operators-R).

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
* `if (`the conditional statement is `TRUE ) {` do something `}`
    * 'Who is the best superhero?'

```
superhero <- "Batman"
if (superhero == "Batman") {
  print("That is correct")
  }
print("Done")
```

```
superhero <- "Black Widow"
```

* `} else {` do a different something `}`

```
if (superhero == "Batman") {
  print("That is correct")
} else {
  print("Please try again")
}
print("Done")
```

* `} else if (` a different conditional statement is `TRUE ) {` 
    * do another different something

```
if (superhero == "Batman") {
  print("That is correct")
} else if (superhero == "Black Widow") {
  print("OK, you may have a point")
} else {
  print("Please try again")
}
print("Done")
```

```
superhero <- "Flash"
```

## Convert to function

```
is_best_superhero <- function(superhero) {
  if (superhero == "Batman") {
	print("That is correct")
  } else if (superhero == "Black Widow") {
	print("OK, you may have a point")
  } else {
	print("Please try again")
  }
}

is_best_superhero("Hulk")
```

* OK. The Hulk is awesome!

```
is_best_superhero <- function(superhero) {
  if (superhero == "Batman") {
	print("That is correct")
  } else if (superhero == "Black Widow" | superhero == "Hulk") {
	print("OK, you may have a point")
  } else {
	print("Please try again")
  }
}

is_best_superhero("Hulk")
```

> Do [Exercise 2 - Complete the Code]({{ site.baseurl }}/exercises/Making-choices-complete-the-code-R).
