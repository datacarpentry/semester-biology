---
layout: page
title: Introduction to Methods
---

Methods are groups of functions that objects of a certain type carry around with
them.

Let's start by looking at a function for working with strings using the `string`
module.

```
import string
dna = 'attggc'
print(string.upper(dna))
```

We can do the same thing using a string method.

```
dna = 'attggc'
print(dna.upper())
```

The idea is that because `dna` is a string we will often want to use string
based functions on it, so instead of needing a module the string itself has
access to these functions.

We don't need to pass the function any input in this case, because it is by
definition working on the string itself, but if the method needs additional
information then it goes inside the parentheses just like a function.

```
weekdays = 'monday, tuesday, wednesday, thursday, friday'
weekdays.replace(',', ';')
```
