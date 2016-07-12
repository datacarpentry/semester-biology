---
layout: exercise
topic: Higher Order Functions
title: Species Area Relationship 1
language: Python
---

The species-area relationship characterizes the relationship between the
the number of species observed at a site and the area being sampled.
This relationship is used widely in ecology and conservation biology for
tasks such as estimating the location of biodiversity hotspots to
prioritize for conservation.

Unfortunately there is no consensus on the form of the equation that
best describes the species-area relationship. This means that any
estimate of species richness depends on the choice of model. Most of the
models have roughly equivalent statistical support and we are going to
be making predictions for regions where there is no data so we can't
determine the best model statistically. Instead we are going to take a
consensus approach where we estimate the species richness using all
possible models and then use the average prediction as our best
estimate.

We are going to deal with 5 models today (*which is already kind of a
lot*), but according to some authors there are as many as 20 reasonable
models for the species-area relationship, so we'll want to make our code
easily extensible. The five models we will work with are those defined
by Dengler and Oldeland (2010).

- Power: S = b<sub>0</sub> * A<sup>b<sub>1</sub></sup>
- Power-quadratic: S = 10<sup>(b<sub>0</sub> + b<sub>1</sub> * log(A) + b<sub>2</sub> * log(A)<sup>2</sup>)</sup>
- Logarithmic: S = b<sub>0</sub> + b<sub>1</sub> * log(A)
- Michaelis-Menten: S = b<sub>0</sub> * A / (b<sub>1</sub> + A)
- Lomolino: S = b<sub>0</sub> / (1 + b<sub>1</sub><sup>log(b<sub>2</sub>/A)</sup>)

All logarithms are base 10. The parameters for each model are available
below, along with the areas at which we wish to predict species
richness. Each sublist contains the parameters for one model in the
order given above. All models 
contain b<sub>0</sub> and b<sub>1</sub>, but only the Power-quadratic and Lomolino models contain the 
third parameter b<sub>2</sub>.


```
sar_parameters = [[20.81, 0.1896], [1.35, 0.1524, 0.0081],
                  [14.36, 21.16], [85.91, 42.57],
				  [1082.45, 1.59, 390000000]]

areas = [1, 5.2, 10.95, 152.3, 597.6, 820, 989.8, 1232.5, 15061]
```

These can be cut and paste into your code. Alternatively, if you're looking for
a more realistic challenge you can import the related `csv` files for
[the parameters]({{ site.baseurl }}/data/sar_model_data.csv) and [the areas]({{ site.baseurl }}/data/sar_areas.csv)
directly from the web. Dealing with extracting the data you need from a standard
`csv` import will be a little challenging, but you'll learn a lot (and you can
always solve the main problem first and then go back and solve the import step
later; which might well be what an experienced programmer would do in this
situtation).

Write a script that calculates the richness predicted by each model for each
area, and exports the results to a `csv` file with the first column containing 
the area for the prediction and the second column containing the mean predicted
richness for that area. To make this easily extensible you will want to write a
function that defines each of the different species-area models (5 functions
total) and then use higher order functions to call those functions. Depending on
how you solve the problem you may find
[zip](http://docs.python.org/library/functions.html#zip) and
[Python's use of asterisks](http://www.technovelty.org/code/python/asterisk.html)
handy.

