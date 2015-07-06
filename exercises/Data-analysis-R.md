---
layout: exercise
title: Data Analysis
subtitle: Code Shuffle
language: R
---

We are interested in understanding the monthly variation in precipitation in
Gainesville, FL. We'll use some data from the
[NOAA National Climatic Data Center](http://www.ncdc.noaa.gov/).

Start by downloading [the data]({{ site.baseurl }}/data/gainesville_precip.csv)
and saving it in the same directory as your homework script. Each row of this
data file is a year (from 1961-2013) and each column is a month (January-
December).

Rearrange the following program so that it:

- Imports the data
- Calculates the average precipitation in each month across years
- Plots the monthly averages as a simple line plot


```
monthly_mean_ppt[i] = mean(ppt_data[,i])
}
plot(monthly_mean_ppt, type='l', xlab = 'month') 
monthly_mean_ppt <- vector(length=12)
ppt_data <- read.csv('gainesville_precip.csv', header = FALSE, sep = ',') 
for (i in 1:12){
```
