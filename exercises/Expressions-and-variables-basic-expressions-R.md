---
layout: exercise
topic: Expressions and Variables
title: Basic Expressions
language: R
---

Think about what value each of the following expressions will return?
Check your answers using the R Console by typing each expression into
the console on the line marked `>` and pressing enter.

1. 2 - 10
2. 3 \* 5
3. 9 / 2
4. 5 - 3 \* 2
5. (5 - 3) \* 2
6. 4 \*\* 2
7. 8 / 2 \*\* 2

Did any of the results surprise you? If so, then might have run in to some order of operations confusion. The order of operators in R are listed [HERE](http://stat.ethz.ch/R-manual/R-patched/library/base/html/Syntax.html).

Now turn this set of expressions into a program that you can save by
using an R script. For each expression add one line to the script as part
of a print statement. Copy and paste the script into the console to display the answer to the screen. If you are using RStudio, you can use Ctrl+Enter (Windows & Linux) or Command+Enter (Mac) to run the line or selection of code directly from your script. 

To tell someone reading the code what this section of the code is about,
add a comment line that says 'Problem 1' before the code that answers
the problem. Comments in R are added by adding the `#` sign.
Anything after a `#` sign on the same line is ignored when the program is
run. So, the start of your program should look something like:

    # Problem 1
    print(2-10)
