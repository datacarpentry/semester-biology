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
6. 4 ^ 2
7. 8 / 2 ^ 2

Did any of the results surprise you? If so, then might have run in to some order
of operations confusion. The order of operators for math in R are the same as
for mathematics more generally.

Now turn this set of expressions into a program that you can save by using an R
script. For each expression add one line to the script. Run the script in the
console to display the answer to the screen. If you are using RStudio, you can
click the `Run` button in the top-right corner of the editor or use Ctrl+Enter
(Windows & Linux) or Command+Enter (Mac) to run the line or selection of code
directly from your script. You can run the entire script by clicking the arrow
next to `Source` and selecting `Source with Echo` or by using Ctrl+Shift+Enter
(Windows & Linux) or Command+Shift+Enter (Mac).

To tell someone reading the code what this section of the code is about,
add a comment line that says 'Exercise 1' before the code that answers
the exercise. Comments in R are added by adding the `#` sign.
Anything after a `#` sign on the same line is ignored when the program is
run. So, the start of your program should look something like:

    # Exercise 1
    2-10
