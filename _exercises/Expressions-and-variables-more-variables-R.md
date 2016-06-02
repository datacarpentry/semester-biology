---
layout: exercise
topic: Expressions and Variables
title: More Variables
language: R
---

Calculate a total biomass in grams for 3 white-throated woodrats
([*Neotoma albigula*](https://en.wikipedia.org/wiki/White-throated_woodrat)) and then convert it to kilograms. The total biomass
is simply the sum of the biomass of all individuals, but in this case we
only know that the average size of a single individual is 250 grams.

1. Add a new section to your R script starting with a comment.
2. Create a variable `grams` and assign it the mass of a single
*Neotoma albigula*.
3. Create a variable `number` and assign it the number of individuals.
4. Create a variable `biomass` and assign it a value by multiplying
the two variables together.
5. Convert the value of `biomass` into kilograms (there are 1000
grams in a kilogram so divide by 1000) and assign this value to a new
variable.
6. Print the final answer to the screen.

*Are the variable names `grams`, `number`, and `biomass` the best
choice? If we came back to the code for this assignment in two weeks
(without the assignment itself in hand) would we be able to remember
what these variables were referring to and therefore what was going on
in the code? The variable name `biomass` is also kind of long. If we
had to type it many times it would be faster just to type `b`. We
could also use really descriptive alternatives like
`individual_mass_in_grams`. Or we would compromise and abbreviate
this or leave out some of the words to make it shorter (e.g.,
`indiv_mass_g`).* 

Have a think about appropriate variable names and then rename the variables in your program to what you find most useful.
