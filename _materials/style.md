---
layout: page
title: Programming Style (in Python)
---

Basics
------
* Readability is important

* E.g.,

    My name is Ethan. I am 36 years old.

    MYnameIS          ETHAN................... I_AM_36 years
                 OLD

* Using the same style as others is important ([PEP 8](http://www.python.org/dev/peps/pep-0008/))
* ``import this``

Whitespace
----------
* Indentation what the brain reconizes, use it regardless of language (and braces)
* 4 space indents
* Spaces after commas and around operators (almost always)

Naming
------
* joined_lower for functions
* StudlyCaps for classes

Long lines
----------
* Lines < 80 characters long
* Use implied line continuation

Flow
----
* No compound statements

Docstrings and Comments
-----------------------
* Docstrings = How to use code ([PEP 257](http://www.python.org/dev/peps/pep-0257/)
* Comments = Why & how code works

General approaches
------------------
Style also includes the general approaches for addressing regularly
encountered problems. E.g.:

* Multi-value assignment
* List comprehensions
    * e.g., [a ** 2 for a in range(10)]
    * e.g., [a * b for a in range(1, 5) for b in range(1, 5) if a == b]
    * e.g., [a * b for a in range(1, 5) for b in range(a, 5)]
    * and Generator expressions - ``sum(a ** 2 for a in range(100))
* get() method for dictionaries
* ``if x:`` not ``if x == True:`` or ``if len(x) > 0:``
* ``enumerate()``
* EAFP (easier to ask forgiveness) no LBYL
    * assume that types are right and fail gracefully if not instead of checking types first
