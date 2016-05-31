---
layout: exercise
topic: Strings
title: Strings and Math
language: R
---

The length of an organism is typically strongly correlated with its body
mass. This is useful because it allows us to estimate the mass of an
organism even if we only know its length. This relationship generally
takes the form
 
Mass (kg) = a * Length(m)<sup>b</sup>
 
where the parameters `a` and `b` vary among groups. Write a script that prompts the user for the following pieces of information:

1. Genus name
2. species name
3. the length of the species

and then estimates the mass of the organism using the equation above.
The script should paste the result as:

*Genus* *species* is *length* meters long and weighs approximately *mass* kg.

where the words in ***italics*** are replaced with the appropriate
values. As is standard practice the first letter (and only the first
letter) of the Genus name should be capitalized, and the species name
should appear in all lower case letters when input.

An allometric approach is regularly used to estimate the mass of
dinosaurs since we cannot typically weigh something that is only
preserved as bones. I'll be testing your script using the length of a
[Spinosaurus](http://en.wikipedia.org/wiki/Spinosaurus) (*Spinosaurus
aegyptiacus*), which is 16 m long based on it's reassembled skeleton.
So, use the values of `a` and `b` for Theropoda (*the appropriate dinosaur
clade*): `a` has been estimated as 0.73 and `b` has been estimated as 3.63
([Seebacher 2001](http://www.jstor.org/stable/4524171)). Spinosaurus is
a predator that is bigger, and therefore, by definition, cooler, than
that stupid Tyrannosaurus that everyone likes so much.
