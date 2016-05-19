---
layout: exercise
topic: Data Analysis
title: Code Shuffle
language: Python
---

We are interested in understanding the monthly variation in precipitation in
Gainesville, FL. We'll use some data from the
[NOAA National Climatic Data Center](http://www.ncdc.noaa.gov/).

Start by downloading [the data]({{ site.baseurl }}/data/gainesville_precip.csv) and saving it in
the same directory as your homework script. Each row of this data file is a year
(from 1961-2013) and each column is a month (January-December).

Rearrange the following program so that it:

- Imports the necessary modules
- Imports the data
- Calculates the average precipitation in each month across years
- Plots the monthly averages as simply line plot

```
plt.plot(monthly_mean_ppt)
import numpy as np
monthly_mean_ppt = ppt_data.mean(axis=0)
ppt_data = np.loadtxt("gainesville_precip.csv", delimiter=',')
plt.show()
import matplotlib.pyplot as plt
```
