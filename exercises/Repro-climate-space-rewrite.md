---
layout: exercise
topic: Reproduction
title: Climate Space Rewrite
language: R
---

This is a follow up to [Climate Space]({{ site.baseurl }}/exercises/Repro-climate-space).

Producing a plot of occurrences on the available climate space for each of the three species required a lot of repetition of very similar code. Whenever this happens, it is usually an indication that a function could be used instead. Such functions reduce the repetition in producing the three species plots, which enables you to save time and prevent errors by not having to rewrite the same code multiple times. 

1. Create a function to download occurrence data and extract the corresponding climate data, which should return a dataset of all the bioclim variables for each species. Because the latitude and longitude columns for each occurrence dataset will be different, generalize them using the column index, instead of the column name, to get only those columns (e.g., `select(longitude = 2, latitude = 3`). 

2. Create a second function for plotting species occurrences onto the available climate space, then use this function to generate a plot for each of the three tree species. 
