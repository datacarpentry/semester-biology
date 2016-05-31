---
layout: page
element: notes
title: Conditionals
language: R
---

## Conditions

* Seen conditions before when filtering data

```
10 > 5
"aang" == "aang"
3 != 3
```

* Conditions return `TRUE` if the condition is satisfied, `FALSE` if not

* Can combine conditions using `and` and `or

```
5 > 2 & 6 >=10
5 > 2 | 6 >=10
```

**Exercise 1**

**Did you notice anything weird?**

## Floating point

```
> x <- 1.3
> y <- 2.8
>  x * 2 + 0.2 == y
[1] FALSE
> 1.3 * 2 + 0.2
[1] 2.8
```

* What's going on?
* See this more easily in Python

```
>>> 1.3 * 2 + 0.2 == 2.8
False
>>> 1.3 * 2 + 0.2
2.8000000000000003
```

`all.equal(x * 2 + 0.2, y)`

## Conditionals

* In addition to using conditions with other functions to filter data we can use
  them directly using `if` statements

```
superhero <- "Black Widow"
if (superhero == "Batman"){
  print("That is correct")
  }
print("Done")
```

```
superhero <- "Black Widow"
if (superhero == "Batman"){
  print("That is correct")
} else {
  print("Please try again")
}
print("Done)
```

```
superhero <- "Black Widow"
if (superhero == "Batman"){
  print("That is correct")
} else if (superhero == "Black Widow") {
  print("OK, you may have a point")
} else {
  print("Please try again")
}
print("Done")
```

* Then switch to `Flash`

## Convert to function

```
is_best_superhero <- function(superhero){
  if (superhero == "Batman"){
	print("That is correct")
  } else if (superhero == "Black Widow") {
	print("OK, you may have a point")
  } else {
	print("Please try again")
  }
}

is_best_superhero("Hulk")
```

* Realize hulk is awesome and add to Black Widow line


**Exercise 2**
