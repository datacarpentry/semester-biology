---
layout: exercise
topic: Scientific
title: Tree Biomass Challenge
language: R
---

Understanding the total amount of biomass (the total mass of all individuals) in 
forests is important for understanding the global carbon budget and how the 
earth will respond to increases in carbon dioxide emissions.

We don't normally measure the mass of a tree, but take a measurement of the
diameter of the trunk and then estimate mass using equations
like mass = 0.124 * diameter<sup>2.53</sup>.

Make a histogram of the estimated tree biomass (using the above equation) for each
species in a 96 hectare area of the Western Ghats in India using the data in
[`ramesh2010-macroplots.csv`]({{ site.baseurl }}/data/ramesh2010-macroplots.csv)
(if isn't already in your workspace then download a copy). Only include species
with at least 100 individuals in your histogram, scale the x axis logarithmically,
and provide good descriptive axis labels.
