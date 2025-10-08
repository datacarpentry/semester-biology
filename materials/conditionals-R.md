---
layout: page
element: notes
title: Conditionals
language: R
---

> Environment Setup:
> Just Base R


> INSTRUCTOR NOTE: Code examples should generally build up by modifying the
> existing code example rather than by retyping the full example.

### Conditionals

* Conditional statements are when we check to see if some condition is true or not
* We used these for filtering data in `dplyr`

```r
weight > 50
species == "DM"
```

* These statements generate a value of type `"logical"`
* The value is `TRUE` if the condition is satisfied
* The value is `FALSE` if the condition is not satisfied
* These aren't the strings "TRUE" and "FALSE"
* They are a special type of value known as "boolean"

* Conditional statements are made with a range of operators
* We've seen
  * `==` for equals
  * `!=` for not equals
  * `<`, `>` for less than and greater than
  * `<=`, `>=` for less than or equal to and greater than or equal to

```r
10 >= 5
```
* There are others, including `%in%`, which checks to see if a value is present in a vector of possible values

```r
"DM" %in% c("DM", "DO", "DS")
"PP" %in% c("DM", "DO", "DS")
```

* There are also functions that return these boolean values
* `is.na()` checks to see if a value is an `NA` (in which case it returns `TRUE` or not (in which case it returns `FALSE`)

```r
is.na(NA)
is.na(5)
```

### Reversing conditions

* Sometimes we want to the opposite of a condition
* We do this using `!` which stands for "not"
* For normal conditional statements we also need `()`

```r
!(10 >= 5)
```

* This reverses the returned boolean value
* So it changes `TRUE` to `FALSE` and `FALSE` to `TRUE`
* If we want to ask if "PP" is not in a given species list

```r
!("PP" %in% c("DM", "DO", "DS"))
```

* So it is true that "PP" is not in the list
* Because it is not in the list, the part inside `()` returns `FALSE`
* And the `!` reverses that `FALSE` to `TRUE`

### Combining conditional statements

* We can combine conditions using "and" and "or"
* We use the `&` for "and"
* Which means if both conditions are `TRUE` return `TRUE`
* If either or both of the conditions is `FALSE` then return `FALSE`

```r
5 > 2 & 6 >=10
```

* We always need to use `&` unless we are using `dplyr::filter()` where we have used separate arguments

* We use the `|` for "or"
* Which means if either or both of the conditions are `TRUE` return `TRUE`

```r
5 > 2 | 6 >=10
```

> *QUICK* (2 mins): Do Tasks 1 & 2 in [Choice Operators]({{ site.baseurl }}/exercises/Making-choices-choice-operators-R).

### Conditional statements work on vectors

* Vectors of values compared to a single value return one logical per value

```r
c(1, 1, 2, 3, 1) == 1
```

* Checks each value to see if equal to 1
* Returns a vector of the results
* This is what `[]` and filtering approaches use to subset
* They keep the values where the value in this condition vector is equal to `TRUE`
* Let's look at an example where we have a vector of counts and a vector the the states they occur in

```r
states <- c('FL', 'FL', 'GA', 'SC')
counts <- c(9, 16, NA, 10)
```

* A conditional statement checking if the state is `'FL'` returns a vector of `TRUE`'s and `FALSE`s

```r
states == 'FL'
```

* So when we filter the `counts` vector to only return values where the `states` is equal to `'FL'`

```r
counts[states == 'FL']
```

* It is the same as passing a vector of `TRUE` and `FALSE` values inside the square brackets

```r
counts[c(TRUE, TRUE, FALSE, FALSE)]
```

* This keeps the first and second values in `counts` because the values in the vector are `TRUE`
* This is also how `dplyr::filter()` works

* Can also compare element wise to see which values in two vectors are the same

```r
recounts <- c(9, 16, NA, 12)
counts == recounts
```

* Cannot compare none equal length vectors (or at least you shouldn't)
* Will error in cases where the lengths of the vectors aren't even multiples

```r
states == c("SC", "GA", "FL")
```

* Or will repeat the shorter vector

```r
states == c("GA", "SC")
```

* Looks like it works, but this is actually doing an element wise comparison

```r
states == c("GA", "SC", "GA", "SC")
```

* If we change the order we can a different answer

```r
states == c("SC", "GA")
```

* This is why we have `%in%`

> Do Tasks 3-10 [Choice Operators]({{ site.baseurl }}/exercises/Making-choices-choice-operators-R).

### `if` statements

* Conditional statements generate logical values
* `if` statements use conditional statements to control flow of the program

```r
if (the conditional statement is TRUE ) {
  do something
}
```

* Example

```r
x = 6
if (x > 5){
  x = x * 2
}
x
```

* `x > 5` is `TRUE`, so the code in the `if` runs
* `x` is now 6 * 2 or 12
* Change `x` to 4

```r
x = 4
if (x > 5){
  x = x * 2
}
x
```

* `x > 5` is `FALSE`, so the code in the `if` doesn't run
* `x` is still 4
* This is *not* a function
* Everything that happens in the if statement influences the global environment (unless the if statement is in a function)
* No `return()`
* Repeat after me: *return, is only, for functions*

* Different mass calculations for different vegetation types

```r
veg_type <- "shrub"
volume <- 16.08
if (veg_type == "shrub") {
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
if (veg_type == "shrub") {
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
veg_type <- "tree"
volume <- 16.08
if (veg_type == "shrub") {
  mass <- 2.65 * volume^0.9
} else if (veg_type == "grass") {
  mass <- 0.65 * volume^1.2
} else {
  mass <- NA
}
mass
```

> Do Tasks 2-3 in [Basic If Statements]({{ site.baseurl }}/exercises/Making-choices-basic-if-statements-R).

#### `if` statements need a single logical value

* While conditional statements can handle vectors, `if` statements typically can't
* The if condition needs to return a single logical value
* So if we try to pass a vector we'll get an error

```r
veg_type <- c("tree", "shrub")
volume <- c(16.08, 2.26)
if (veg_type == "shrub") {
  mass <- 2.65 * volume^0.9
} else if (veg_type == "grass") {
  mass <- 0.65 * volume^1.2
} else {
  mass <- NA
}
mass
```

### Using Conditionals Inside Functions

* We've used a conditional to estimate mass differently for different types of vegetation
* This is the kind of code we are going to want to reuse, so let's move it into a function
* We do this by placing the same code inside of a function
* And making sure that the function takes all required variables as input

```r
est_mass <- function(volume, veg_type){
  if (veg_type == "shrub") {
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
est_mass(1.6, "shrub")
est_mass(1.6, "grass")
est_mass(24, "tree")
```

* Let's walk through how this code executes using the debugger
* When we call the function the first thing that happens is that 1.6 gets assigned to `volume` and `"tree"` gets assigned to `veg_type`
* The code then checks to see if `veg_type` is equal to `"shrub"`
* It isn't so the code then checks to see if `veg_type` is equal to `"grass"`
* It isn't so the code then hits the `else` statement and executes the code in the `else` block
* It assigns `NA` to mass
* It then finishes the if/else if/else statement and returns the value for `mass`, which is `NA` to the global environment

> Do Task 4 in [Basic If Statements]({{ site.baseurl }}/exercises/Making-choices-basic-if-statements-R).
> Do Tasks 1 & 2 in [If Statements In Functions]({{ site.baseurl }}/exercises/Making-choices-if-statements-in-functions-R).

### Automatically extracting functions (optional)

* Can pull code out into functions
* Highlight the code
* Code -> Extract Function
* Provide a name for the function

### If statements with functions that return booleans

* We can also use if statements with functions that return `TRUE` or `FALSE`
* Assume our values for `veg_type` are messier and include values like `"grass A"` and `"grass B"`
* We want our function to work the same way but if veg_type is `"grass A"` then it doesn't match our condition

```r
est_mass(1.6, "grass A")
"grass A" == "grass"
```

* Instead of checking if `veg_type` is equal to `"grass"` we check to see if `veg_type` contains the word "grass"
* We do this using the `str_detect` function from `stringr`

```r
install.packages('stringr')
```

```r
library(stringr)

str_detect("grass A", "grass")
```

* Since this function produces `TRUE` or `FALSE` we can replace the conditional statements in our functions

```r
est_mass <- function(volume, veg_type){
  if (str_detect(veg_type, "shrub")) {
    mass <- 2.65 * volume^0.9
  } else if (str_detect(veg_type, "grass")) {
    mass <- 0.65 * volume^1.2
  } else {
    mass <- NA
  }
  return(mass)
}
```


### Multiple ifs vs else if (optional)

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
x
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
x
```

### Nested conditionals (optional)

* Sometimes decisions are more complicated
* For example we might have different equations for some vegetation types based on the age of the plant
* Can "nest" conditionals inside of one another

```r
est_mass <- function(volume, veg_type, age){
  if (veg_type == "shrub") {
    if (age < 5) {
      mass <- 1.6 * volume^0.8
    } else {
      mass <- 2.65 * volume^0.9
    }
  } else if (veg_type == "grass" | veg_type == "sedge") {
    mass <- 0.65 * volume^1.2
  } else {
    mass <- NA
  }
  return(mass)
}

est_mass(1.6, "shrub", age = 2)
est_mass(1.6, "shrub", age = 6)
```

* First checks if the vegetation type is "shrub"
* If it is checks to see if it is < 5 years old
* If so does one calculation, if not does another
* But nesting can be difficult to follow so try to minimize it

> Assign the rest of the exercises.
