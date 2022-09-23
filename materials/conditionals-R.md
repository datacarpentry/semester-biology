---
layout: page
element: notes
title: Conditionals
language: R
---

> INSTRUCTOR NOTE: Code examples should generally build up by modifying the
> existing code example rather than by retyping the full example.

### Conditionals

* Conditional statements are when we check to see if some condition is true or not
* We used these for filtering data in `dplyr`

```r
weight > 50
species == "DM"
```

* These statements generate a value is of type `"logical"`
* The value is `TRUE` if the condition is satisfied 
* The value is `FALSE` if the condition is not satisfied
* These aren't the strings "TRUE" and "FALSE"
* They are a special type of value
  
* Conditional statements are made with a range of operators
* We've seen
  * `==` for equals
  * `!=` for no equals
  * `<`, `>` for less than and greater than
  * `<=`, `>=` for less than or equal to and greater than or equal to
  * `is.na()` for is this value null
* There are others, including `%in%`, which checks to see if a value is present in a vector of possible values

```r
"aang" == "aang"
"aang" != "kora"
10 < 5
10 >= 5
is.na("toph")
"zuko" %in% c("aang", "toph", "katara")
```

* We can combine conditions using "and" and "or"
* We use the `&` for "and"
* Which means if both conditions are `TRUE` return `TRUE` 
* If one of the contions is `FALSE` then return `FALSE`

```r
5 > 2 & 6 >=10
```

* We use the `|` for "or"
* Which means if either or both of the conditions are `TRUE` return `TRUE`

```r
5 > 2 | 6 >=10
```

* Vectors of values compared to a single value return one logical per value

```r
c(1, 1, 2, 3, 1) == 1
```

* Checks each value to see if equal to 1
* This is what subsetting approaches use to subset
* They keep the values where the value in this condition vector is equal to `TRUE`
* Let's look at an example where we have a vector of sites and a vector the the states they occur in

```r
site = c('a', 'b', 'c', 'd')
state = c('FL', 'FL', 'GA', 'AL')
```

* A conditional statement checking if the state is `'FL'` returns a vector of `TRUE`'s and `FALSE`s

```r
state == 'FL'
```

* So when we filter the `site` vector to only return values where the `state` is equal to `'FL'`

```r
site[state == 'FL']
```

* It is the same as pass a vector of `TRUE` and `FALSE` values inside the square brackets

```r
site[c(TRUE, TRUE, FALSE, FALSE)]
```

* This keeps the first and second values in `site` because the values in the vector are `TRUE`
* This is how `dplyr::filter()` and other methods for subsetting data work

> Do Tasks 1-4 in [Choice Operators]({{ site.baseurl }}/exercises/Making-choices-choice-operators-R).

### `if` statements

* Conditional statements generate logical values to filter inputs.
* `if` statements use conditional statements to control flow of the program.

```r
if (the conditional statement is TRUE ) {
  do something
}
```

* Example

```r
x = 6
if (x > 5){
  x = x^2
}
x
```

* `x > 5` is `TRUE`, so the code in the `if` runs
* `x` is now 6^2 or 36
* Change `x` to 4

```r
x = 4
if (x > 5){
  x = x^2
}
x
```

* `x > 5` is `FALSE`, so the code in the `if` doesn't run
* `x` is still 4
* This is *not* a function, so everything that happens in the if statement
  influences the global environment

* Different mass calculations for different vegetation types

```r
veg_type <- "tree"
volume <- 16.08
if (veg_type == "tree") {
  mass <- 2.65 * volume^0.9
  }
mass
```

> Do Task 1 in [Basic If Statements]({{ site.baseurl }}/exercises/Making-choices-basic-if-statements-R).

* Often want to chose one of several options
* Can add more conditions and associated actions with `else if`
 
```r
veg_type <- "grass"
volume <- 16.08
if (veg_type == "tree") {
  mass <- 2.65 * volume^0.9
} else if (veg_type == "grass") {
  mass <- 0.65 * volume^1.2
}
mass
```

* Checks the first condition
* If `TRUE` runs that condition's code and skips the rest
* If not it checks the next one until it runs out of conditions

* Can specify what to do if none of the conditions is `TRUE` using `else` on its own

```r
veg_type <- "shrub"
volume <- 16.08
if (veg_type == "tree") {
  mass <- 2.65 * volume^0.9
} else if (veg_type == "grass") {
  mass <- 0.65 * volume^1.2
} else {
  mass <- NA
}
mass
```

> Do Tasks 2-3 in [Basic If Statements]({{ site.baseurl }}/exercises/Making-choices-basic-if-statements-R).

### Multiple ifs vs else if

* Multiple ifs check each conditional separately
* Executes code of all conditions that are `TRUE`

```r
x <- 5
if (x > 2){
  x * 2
}
if (x > 4){
  x * 4
}
```

* `else if` checks each condition sequentially
* Executes code for the first condition that is `TRUE`

```r
x <- 5
if (x > 2){
  x * 2
} else if (x > 4){
  x * 4
}
```

### Using Conditionals Inside Functions

* We've used a conditional to estimate mass differently for different types of vegetation
* This is the kind of code we are going to want to reuse, so let's move it into a function
* We do this by placing the same code inside of a function
* And making sure that the function takes all required variables as input

```r
est_mass <- function(volume, veg_type){
  if (veg_type == "tree") {
    mass <- 2.65 * volume^0.9
  } else if (veg_type == "grass") {
    mass <- 0.65 * volume^1.2
  } else {
    mass <- NA
  }
  return(mass)
}
```

* We can then run this function with different vegetation types and get different estimates for mass

```r
est_mass(1.6, "tree")
est_mass(1.6, "grass")
est_mass(1.6, "shrub")
```

* Let's walk through how this code executes using the debugger
* When we call the function the first thing that happens is that 1.6 gets assigned to `volume` and `"shrub"` gets assigned to `veg_type`
* The code then checks to see if `veg_type` is equal to `"tree"`
* It isn't so the code then checks to see if `veg_type` is equal to `"grass"`
* It is so the code then hits the `else` statement and executes the code in the `else` block
* It assigns `NA` to mass
* It then finishes the if/else if/else statement and returns the value for `mass`, which is `NA` to the global environment

> Do [Size Estimates by Name]({{ site.baseurl }}/exercises/Making-choices-size-estimates-by-name-R).

### Automatically extracting functions

* Can pull code out into functions
* Highlight the code
* Code -> Extract Function
* Provide a name for the function

### Nested conditionals

* Sometimes decisions are more complicated
* For example we might have different equations for some vegetation types based on the age of the plant
* Can "nest" conditionals inside of one another

```r
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

> Assign the rest of the exercises.