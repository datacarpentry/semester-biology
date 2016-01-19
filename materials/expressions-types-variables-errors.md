---
layout: page
title: Expressions, Types, Variables, and Errors
---

# Expressions

A command that returns a value:

```
>>> 2 + 2
4
>>> abs(-2)
2
```

## Python follows standard order of operations

```
>>> 3 + 5 * 2
13
```

# Types

All values have types

```
>>> type(1)
int

>>> type(26.2)
float

>>> type('hello world')
str
```

Types are important because they tell the program how to act

```
>>> 'Brad' + 'Pitt'
BradPitt

>>> 75 + 2
77
```

But they can also be confusing

```
>>> 15.0 / 2
7.5

>>> 15 / 2
7
```

* Old school (Python 2): Any combination of two integers is an integer
* New school (Python 3): `>>> from __future__ import division`

# Variables

A variable is a name that has a value associated with it

```
>>> x = 27
>>> x
27
```

It works just like the value itself

```
>>> 10 + x * 2
64
```

It won't change unless you assign a new value to it directly

# Errors

Errors tell you that your program isn't working, and they also tell you where it
isn't working and what went wrong. It's very important to read error messages
carefully.

`>>> print("The high temperature today is going to be: " + 71)`
