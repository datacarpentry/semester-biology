Programming Style (in Python)
=============================

Basics
------
* Readability is important
* Using the same style as others is important ([PEP 8](http://www.python.org/dev/peps/pep-0008/))

Whitespace
----------
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
* No compond statements

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
    * and Generator expressions
* get() method for dictionaries
* ``if x:`` not ``if x == True:`` or ``if len(x) > 0:``
* ``enumerate()``
* EAFP (easier to ask forgiveness) no LBYL- assume that types are right and fail gracefully if not