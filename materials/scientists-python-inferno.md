---
layout: page
title: The (Scientist's) Python Inferno
---

This is a brief description of some of the common stumbling points in Python
for scientific programmers, named in deference to The R Iferno (which is much
more expansive).

Table of Contents
-----------------
1. Indexing starts at 0, not 1
2. Dividing one integer by another yeilds an integer (Python 2 only)
3. Some methods change an object in place and return None
4. Data type conversion issues

Indexing starts at 0 not 1
--------------------------

If you want the first item in a list, string, tuple, etc. then the index for
this value is 0. For example,

```
>>> my_list = [1, 2, 3, 4]
>>> my_list[1]
2
```

This is standard for most programming languages, but not for scripting
languages like R and Matlab.

Integer Division (Python 2.x)
-----------------------------

Dividing an integer by another integer returns an integer, even when the
two numbers are not evenly divisible. For example,

```
>>> 2 / 3
0

>>> -3 / 2
-2
```

The resulting values are rounded down to the nearest integer.
This happens because computers pay attention to the type of data they are
working with and often like to maintain types when combining two things of
the same type. However, since this result is clearly wrong to most humans
(and to all scientists). Python 3 now does this division as expected.
There are three approaches to fix this integer division problem:

1. Import the expected functionality by typing ``from __future__ import division``
at the beginning of an interactive session or at the beginning of your script.
2. Convert one or more of the integers to floats prior to doing the calculation:
`float(2) / 3`
3. Add a decimal place to one of the integers so that it's type is already float:
`2 / 3.0`.

Note that this does not work very well programmatically so approaches (1)
and (2) are preferred.

Methods return None
-------------------

Methods are functions that are attached to objects of a particular type.
Some of these methods return modified versions of the object and do not change the
object itself, but some modify the object and return ``None``. For example,
all lists have a method called sort that sorts the values in the list.
When you call sort it sorts the list in question and returns None. So,

```
>>> my_list = ['A', 'F', 'D', 'B', 'E', 'C']
>>> my_new_list = my_list.sort()
>>> my_new_list
None
>>> my_list
['A', 'B', 'C', 'D', 'E']
```

Misunderstanding this behavior can lead to a common bug when attempting to sort a
list where the values in the list are accidentally delected:

```
>>> my_list = ['A', 'F', 'D', 'B', 'E', 'C']
>>> my_list = my_list.sort()
>>> my_list
None
```

Data type conversion issues
---------------------------

Most data type conversion in Python is seamless (unlike a certain capital letter language),
but there are still tricky conversions in places.

### Converting a list to a Numpy Structured Array

Lists of lists will not convert to Structured Arrays properly, but lists of Tuples will.

```
>>> import numpy as np
>>> my_list = [['A', 1], ['B', 2], ['C', 3]]
>>> np.array(my_list, dtype={'names': ['ID', 'Value'], 'formats': ['a2', 'i2']})
Traceback (most recent call last):
  File "<string>", line 1, in <fragment>
TypeError: expected a readable buffer object

>>> my_list = [('A', 1), ('B', 2), ('C', 3)]
>>> np.array(my_list, dtype={'names': ['ID', 'Value'], 'formats': ['a2', 'i2']})
array([('A', 1), ('B', 2), ('C', 3)], 
      dtype=[('ID', '|S1'), ('Value', '<i2')])
```

This can be easily addressed using a list comprehension:

```
>>> my_list = [['A', 1], ['B', 2], ['C', 3]]
>>> my_list = [tuple(row) for row in my_list]
>>> my_list
[('A', 1), ('B', 2), ('C', 3)][('A', 1), ('B', 2), ('C', 3)]
```
