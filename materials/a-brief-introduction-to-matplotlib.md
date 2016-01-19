--- layout: post title: A brief introduction to matplotlib created:
1289851333 categories: [] ---

#### Import

import matplotlib.pyplot as p

\

#### Basic plots of two variables

p.plot(x, y, color\_symbol\_info) \#color\_symbol\_info looks like 'bo-'
for blue circles connected by a solid line\

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

p.subplot(number\_of\_rows\_of\_plots, number\_of\_cols\_of\_plots,
position)

#### Multiple Figures

To start a new figure:

p.figure()
