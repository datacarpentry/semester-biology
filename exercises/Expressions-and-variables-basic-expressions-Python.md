---
layout: exercise
topic: Expressions and Variables
title: Basic Expressions
language: Python
---

Think about what value each of the following expressions will return?
Check your answers using the Python interpreter by typing each expression into
the interpreter and pressing enter.

1. 2 - 10
2. 3 \* 5
3. 8 / 2
4. 9 / 2
5. 9.0 / 2
6. 5 - 3 \* 2
7. (5 - 3) \* 2
8. 4 \*\* 2
9. 8 / 2 \*\* 2

Did any of the results surprise you? If so, then you've probably run
into a common point of confusion in Python 2 - [Integer
Division](http://nbviewer.ipython.org/urls/github.com/ethanwhite/progbio/raw/master/ipynbs/integer-division.ipynb).

Now turn this set of expressions into a program that you can save by
using the editor. For each expression add one line to the editor as part
of a print statement to display the answer to the screen.

To tell someone reading the code what this section of the code is about,
add a comment line that says 'Problem 1' before the code that answers
the problem. Comments in Python are added by adding the `#` sign.
Anything after a `#` sign on the same line is ignored when the program is
run. So, the start of your program should look something like:

    # Problem 1
    print(2-10)
