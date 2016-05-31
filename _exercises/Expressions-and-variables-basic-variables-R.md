---
layout: exercise
topic: Expressions and Variables
title: Basic Variables
language: R
---

Here is a small program that converts a mass in kilograms to a mass in grams and
then prints out the resulting value.

```
mass_kg <- 2.62
mass_g <- mass_kg * 1000
print(mass_g)
```

Modify this code to create a variable that stores a body mass in pounds and
assign it a value of 3.5 (about the right size for a
[Desert Cottontail Rabbit – *Sylvilagus audubonii*](https://en.wikipedia.org/wiki/Desert_Cottontail)). Convert
this value to kilograms (we are serious scientists after all). There are
approximately 2.2046 lbs in a kilogram, so divide the variable storing the
weight in pounds by 2.2046 and store this value in a new variable for storing
mass in kilograms. Print the value of the new variable to the screen.
