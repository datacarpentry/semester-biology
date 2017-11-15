---
layout: page
element: notes
title: Problem Decomposition
language: R
---

### Approaches to solving problems

* Real computational tasks are complicated. 
* To accomplish them effectively you need to **think before you code**.

* Decompose a coding problem:

1. Understand the problem.
    * Identify inputs and outputs.
        * Input = Portal surveys csv
        * Output = plot of yearly abundance for large and small rodents

	```
	# Overall goal: visualize how many large (>50g) and 
	# small (<50g) mammals are collected each year
	```

2. Break the problem down into a few pieces.
    * Bullet list on paper or comments in script. 

	```
	# Subtasks
	    # Import data
	    # Get column of small and large categories
	    # Count number of each per year
	    # Plot this
	```

3. Break those pieces into codeable chunks.

	```
	# TODO: function that returns size class from weight
	```

4. Code one chunk at a time.

### Coding one chunk

* Write function to return size classes

```
get_size_class()
```

* Start with if statement
* Pseudocode
    * Write code in English
    * “If weight value is bigger than 50, return large; otherwise return small”

```
if(weight > 50){
  size_class <- "large"
} else {
  size_class <- "small"
}
```

* Test code using values with known output

```
weight <- 10
```

* Turn into function

```
get_size_class <- function(weight){
  if(weight > 50){
    size_class <- "large"
  } else {
    size_class <- "small"
  }
}
get_size_class(100)
```

* Why doesn’t this work? 

```
get_size_class <- function(weight){
  if(weight > 50){
    size_class <- "large"
  } else {
    size_class <- "small"
  }
  return(size_class)
}
```

* Generalize function
* Easier to change values later
* Always test after changing

```
get_size_class <- function(weight, threshold){
  if(weight > threshold){
    size_class <- "large"
  } else {
    size_class <- "small"
  }
  return(size_class)
}
get_size_class(100, 50)
get_size_class(100, 150)
```

* Make one change at a time

* Decompose a code chunk:
    1. Think about it.
    2. Write it.
    3. Test it ( *on it's own* ).
    4. Fix any problems.

> Rest of code in [decomposition-example.R]({{ site.baseurl }}/materials/decomposition-example.R).
