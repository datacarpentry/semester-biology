---
layout: page
title: Problem decomposition
---

Real computational tasks are complicated. 
To accomplish them you need to **think before you code**.

## Problem decomposition steps

1.  Understand the problem
    1. Restate the problem in your own words.
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
    2. Write the code.
    3. Test it... on it's own.
    4. Fix any problems.
5. One way to do this is to identify functions.

### Example

> Build this example up piece by piece. First do then top level, then breakdown
> one bullet, etc.

Make a graph of the relationship between diameter and height in trees and
highlight the relationship for a single species.

1. Prepare data on diameter and height
    1. Download data
    2. Import data
    3. Clean data
        1. Filter nulls
2. Make plot
    1. Plot diameter vs height for all species
        1. Basic plot
        2. Good labels
        3. Transformation?
        4. Colors?
    2. Add points for highlighted species
    3. Clean up plot
3. Reproducibility check

## Make a simpler version first

If you aren't sure how to do something, make a simpler version that you do know
how to do first. 

1. Experiment
2. Write a simpler version
3. Make sure it works
4. Make sure you understand it
5. Modify it to make it more complicated
6. Repeat until finished
