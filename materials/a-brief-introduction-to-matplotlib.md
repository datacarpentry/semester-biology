--- 
layout: page 
element: notes
title: A brief introduction to matplotlib 
language: Python
---

#### Import

import matplotlib.pyplot as p

#### Basic plots of two variables

p.plot(x, y, color_symbol_info)

color_symbol_info looks like 'bo-' for blue circles connected by a solid line

p.loglog(x, y)

p.semilogx(x, y)

####  

#### Histograms

p.hist(x, numberofbins)

 

#### Labeling the axes

p.xlabel('My x-axis name')

p.ylabel('My y-axis name')

####  

#### Changing the axis limits

p.axis([xmin, xmax, ymin, ymax])

####  

#### Plotting multiple sets of data together

p.hold(True)

p.hold(False)

####  

#### Subplots

p.subplot(number_of_rows_of_plots, number_of_cols_of_plots, position)

#### Multiple Figures

To start a new figure:

p.figure()
