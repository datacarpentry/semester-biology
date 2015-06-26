---
layout: page
title: Problem decomposition
---

Real computational tasks are complicated. 
To accomplish them you need to **think before you code**.

## Problem decomposition steps

1.  Understand the problem
    1 Restate the problem in your own words.
    2. Know what the desired inputs and outputs are.
    3. Ask questions for clarification (in class these questions might be to
       your instructor, but most of the time they will be asking either yourself
       or your collaborators).
2.  Break the problem down into a few large pieces. Write these down, either on
    paper or as comments in a file.
3.  Break complicated pieces down into smaller pieces. Keep doing this until all
    of the pieces are small.
4.  Code one small piece at a time.
    1. Think about how to implement it.
    2. Write the code/query.
    3. Test it... on it's own.
    4. Fix any problems.
5. One way to do this is to identify functions.

### Example

Calculate the volume of a bunch of shrubs.

Data

```
length,width,height
1, 2, 3
2, 4, 3
```

1. Calculate the volume of a shrub
   a. Function
2. Run this calculation on all shrubs
   a. Loop

Write either first.

## Make a simpler version first

If you aren't sure how to do something, make a simpler version that you do know
how to do first. 

1. Experiment
2. Write a simpler version
3. Make sure it works
4. Make sure you understand it
5. Modify it to make it more complicated
6. Repeat until finished

## Converting code into functions

If making a function work is confusing, start without a function and then
convert it into a function.

1. Write a specific example of what the function should do
2. Create variables to hold the specific values you used
3. Replace the specific values in your example with the variables
4. Use the names of those variables in the function definition
5. Indent
6. Remove the initial definition of the variables
7. Return you answer
8. Call the function
