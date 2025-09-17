---
layout: page
element: notes
title: Graphing using ggplot
language: R
---

> * Get familiarized with [metadata](https://esapubs.org/archive/ecol/E095/064/metadata.php) - *Acacia drepanolobium* Surveys
> * [UHURU Acacia Experiment Data](https://ndownloader.figshare.com/files/5629542)
> * [UHURU Tree Survey Data](https://ndownloader.figshare.com/files/5629536)

### Introduction to the UHURU dataset

### Data

* For the next set of lessons we'll be working with data on acacia size from an experiment in Kenya
* The experiment is designed to understand the influence of herbivores on vegetation by excluding different sized herbivores
* There are 3 different treatments:
  * The top-left image shows Megaherbivore exclosures, which use wires 2m high to keep elephants
  * The top-right image shows Mesoherbivore exclosures, which use fenses starting 1/3m off the ground to exclude things like impalla
  * The bottom-left image shows full exclosures, which use fenses all the way to the ground to keep out all mammalian herbivores
  * And the bottom-right image shows control plots

![Pictures of 4 experimental treatments. (A) Megaherbivore fences consist of two parallel wires starting 2-m above ground level. (B) Mesoherbivore fences consist of 11 parallel wires starting ~0.3 m above ground level and continuing to 2.4-m above ground level. (C) Total-exclusion fences consist of 14 wires up to 2.4-m above ground level, with a 1-m high chain-link barrier at ground level. (D) Open control plots are unfenced, with boundaries demarcated by short wooden posts at 10-m intervals.](https://esapubs.org/archive/ecol/E095/064/images/Fig2.png)

* So far we've been working with datasets that are separated by commas
* *Click on surveys.csv to show csv format*
* But if we look at this new dataset it looks different
* * *Click on Acacia Dataset to Open in Text Editor*
* This data is tab separated, so we'll need to treat it differently when we import it
* We'll call our data frame `acacia` and assign it the output from `read_tsv()`, where the `t` is for "tab"
* We still give it the name of the file in quotes as the first argument

```r
library(readr)

acacia <- read_tsv("ACACIA_DREPANOLOBIUM_SURVEY.txt")
```

* We can also see that it includes information on whether or not the plant is dead in the HEIGHT column
* Is that good data structure?
* If you said "No", you're right, information on if the tree is dead should be stored in a separate column
* For now, we'll just treat the "dead" entries as null values
* We can do this by using another optional argument `na`
* So let's modify our `read_tsv` statement by adding `na = c("dead")`.
* This will replace the string `"dead"` with `NA`
* It gets passed as a vector because this allows multiple different values to be set as nulls

```r
acacia <- read_tsv("ACACIA_DREPANOLOBIUM_SURVEY.txt", na = c("dead"))
```

* If we open the resulting table we can see that it includes information on:
  * the time and location of the sampling
  * the experimental treatment
  * the size of each Acacia including a height, the canopy diameter measured in the direction (or axis) or the largest diameter and the diameter of the axis perpendicular to that, and the circumference of the shrub
  * information on the number of flowers, buds, and fruits
  * And finally information on the species of ant associated with the shrub because there is a very interesting ant-acacia mutualism where the Acacia special structures that serve as houses for the ants and the ants swarm herbivores that try to eat the acacia


### ggplot

* Very popular plotting package
* Good plots quickly
* Declarative - describe what you want not how to build it
* Contrasts w/Imperative - how to build it step by step
* Install `ggplot2` using `install.packages`

### Basics

* We load the `ggplot2` package just like we loaded `dplyr`

```r
library(ggplot2)
```

* We'll also load the UHURU like we discussed in the video on the dataset

```r
acacia <- read_tsv("ACACIA_DREPANOLOBIUM_SURVEY.txt", na = c("dead"))
```

* To build a plot using `ggplot` we start with the `ggplot()` function

```r
ggplot()
```

* `ggplot()` creates a base ggplot object that we can then add things to
* Like a blank canvas

* We can also add optional arguments for information to be shared across different components of the plot
* The two main arguments we typically use here are
* `data` - which is the name of the data frame we are working with, so `acacia`
* `mapping` - which describes which columns of the data are used for different aspects of the plot
* We create a `mapping` by using the `aes` function, which stands for "aesthetic", and then linking columns to pieces of the plot
* We'll start with telling ggplot what value should be on the x and y axes
* Let's plot the relationship betwen the circumference of an acacia and its height

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT))
```

* This still doesn't create a figure, it's just a blank canvas and some information on
  default values for data and mapping columns to pieces of the plot
* We can add data to the plot using layers
* We do this by adding a `+` after the the `ggplot` function and then adding something called a `geom`, which stands for `geometry`
* To make a scatter plot we use `geom_point`

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point()
```

* It is standard to hit `Enter` after the plus so that each layer shows up on its own line

* To change things about the layer we can pass additional arguments to the `geom`
* We can do things like change
  * the `size` of the points, we'll set it to `3`
  * the `color` of the points, we'll set it to `"blue"`
  * the transparency of the points, which is called `alpha`, we'll set it to 0.5

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, color = "blue", alpha = 0.5)
```

* To add labels (like documentation for your graphs!) we use the `labs` function

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, color = "blue", alpha = 0.5) +
  labs(x = "Circumference [cm]", y = "Height [m]",
       title = "Acacia Survey at UHURU")
```

> Do Task 1 in [Acacia and ants]({{ site.baseurl }}/exercises/Graphing-acacia-ants-R).

### Grouping

#### Color

* Group on a single graph
* Look at influence of experimental treatment

```r
ggplot(acacia, aes(x = CIRC, y = HEIGHT, color = TREATMENT)) +
  geom_point(size = 3, alpha = 0.5)
```

#### Facets

* We can also split data into subplots

```r
ggplot(acacia, aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, alpha = 0.5) +
  facet_wrap(vars(TREATMENT))
```

* Where are all the acacia in the open plots? (eaten?)

> Do Tasks 2-3 in [Acacia and ants]({{ site.baseurl }}/exercises/Graphing-acacia-ants-R).
> This seems short, but for a 50 min class you do have time to stop,
> have them work for 5 min on the basic version,
> and then come back and provide the extra information in the last 5 min of class

* Did you have any subplots with only one or two points?
* Why?
* Can be useful to facet by more than one thing
* To wrap using combinations of variables add variables to `vars()`

```r
ggplot(acacia, aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, alpha = 0.5) +
  facet_wrap(vars(TREATMENT, ANTS))
```

* This is one reason we have the `vars()` function
* We can also layout the grid in two dimensions using `facet_grid()`
* The first argument is the variables to put the on rows and the second argument is the variable to put on the columns

```r
ggplot(acacia, aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, alpha = 0.5) +
  facet_grid(vars(TREATMENT), vars(ANTS))
```

* Using this approach we can see that ant species associated with just a couple of Acacia can occur on a variety of different treatments

### Statistical transformations

* We've seen that ggplot makes graphs by combining information on
  * Data
  * Mapping of parts of that data to aspects of the plot
  * A geometric object to represent the data

```r
ggplot(acacia, aes(x = CIRC, y = HEIGHT)) +
  geom_point()
```

* Many kinds of geometric object (type `geom_` and show completions)

* Each geom includes a statistical transformations
* So far we've only seen
    * `identity`: the raw form of the data or no transformation
* Transformations exist to make things like histograms, bar plots, etc.
* Occur as defaults in associated geoms

* To look at the number of acacia in each treatment use a bar plot
    * [`geom_bar()`](https://ggplot2.tidyverse.org/reference/geom_bar.html)

```r
ggplot(acacia, aes(x = TREATMENT)) +
  geom_bar()
```

* Uses the transformation `stat_count()`
    * Counts the number of rows for each treatment

* To look at the distribution of circumferences in the dataset use a histogram
    * [`geom_histogram()`](https://ggplot2.tidyverse.org/reference/geom_histogram.html)

```r
ggplot(acacia, aes(x = CIRC)) +
  geom_histogram()
```

* Uses `stat_bins()` for data transformation
    * Splits circumferences into bins and counts rows in each bin
* Set number of `bins` or `binwidth`

```r
ggplot(acacia, aes(x = CIRC)) +
  geom_histogram(bins = 15)
```

```r
ggplot(acacia, aes(x = CIRC)) +
  geom_histogram(binwidth = 5)
```

* If we want to change the color of our bars we use `fill` instead of `color`

```r
ggplot(acacia, aes(x = CIRC)) +
  geom_histogram(binwidth = 5, fill = "red")
```

* `color` changes the outline color
* `fill` changes the inside color

* These can be combined with all of the other `ggplot2` features we've learned

> Do Tasks 1-2 in [Acacia and ants histograms]({{ site.baseurl }}/exercises/Graphing-acacia-ants-histograms-R).

### Position

* geom's also come with a default position
* In many cases the position is `"identity"`, which just means the object is plotted in the position determined by the data, but not always
* Let's remake our histogram, but color the bars by the treatment

```r
ggplot(acacia, aes(x = CIRC, fill = TREATMENT)) +
  geom_histogram(binwidth = 5)
```

* You can see that the total height of the bars stayed the same
* That's because ggplot has just colored the pieces of each bar that correspond to each treatment
* It does this because the default `position` for `geom_histogram` is `"stack"`, which stacks the bars on top of one another and therefore makes a stacked histogram.
* If we want separate overlapping histograms then we need to change the position

```r
ggplot(acacia, aes(x = CIRC, fill = TREATMENT)) +
  geom_histogram(binwidth = 5, position = "identity")
```

* And then add some transparency so we can see all of the histograms

```r
ggplot(acacia, aes(x = CIRC, fill = TREATMENT)) +
  geom_histogram(binwidth = 5, position = "identity", alpha = 0.5)
```

> Do Tasks 3 in [Acacia and ants histograms]({{ site.baseurl }}/exercises/Graphing-acacia-ants-histograms-R).

### Layers

* So far we've only plotted one layer or geom at a time, but we can combine multiple layers in a single plot
    * `ggplot()` sets defaults for all layers
    * Can combine multiple layers using `+`
    * The first geom is plotted first and then additional geoms are layered on top

* Combine different kinds of layers
* Add a linear model

```r
ggplot(acacia, aes(x = CIRC, y = HEIGHT)) +
  geom_point() +
  geom_smooth(method = "lm")
```

* Both the `geom_point` layer and the `geom_smooth` layer use the defaults from
  `ggplot`
* Both use `acacia` for data and `x = CIRC, y = HEIGHT` for the aesthetic
* `geom_smooth` uses the statistical transformation `stat_smooth()` to produce a smoothed representation of the data

* Do this by treatment

```r
ggplot(acacia, aes(x = CIRC, y = HEIGHT, color = TREATMENT)) +
  geom_point() +
  geom_smooth(method = "lm")
```

* Because the color aesthetic is the default it is inherited by geom_smooth
* One set of points and one model for each treatment

> Do Task 1 of [Acacia and Ants Layers]({{ site.baseurl }}/exercises/Graphing-acacia-ants-layers-R).


### Changing values across layers

* We can also plot data from different columns or even data frames on the same graph
* To do this we need to better understand how layers and defaults work
* So far we've put all of the information on data and aesthetic mapping into `ggplot()`

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point() +
  geom_smooth(method = "lm")
```

* This sets the default data frame and aesthetic, which is then used by
  `geom_point()` and `geom_smooth()`
* Alternatively instead of setting the default we could just give these values
  directly to `geom_point()` and `geom_smooth()`

```r
ggplot() +
  geom_point(data = acacia,
             mapping = aes(x = CIRC, y = HEIGHT,
                           color = TREATMENT)) +
  geom_smooth(method = "lm")
```

* We can see that this information is no longer shared with other geoms since it
  is no longer the default, so we've asked for a smooth of nothing and so no smoother is shown

* Can use this to combine different aesthetics
* Make a single model across all treatments while still coloring points

```r
ggplot() +
  geom_point(data = acacia,
             mapping = aes(x = CIRC, y = HEIGHT,
                           color = TREATMENT)) +
  geom_smooth(data = acacia,
              mapping = aes(x = CIRC, y = HEIGHT))
```

* `color` is only set in the aesthethic for the point layer
* So the smooth layer is made across all x and y values

* *Check if this makes sense to everyone*

* This same sort of change can be used to plot different columns on the same
  plot by changing the values of x or y
* If we wanted to plot two different columns as Y we could change the value of y in the aesthetic
* If we wanted to use data from two different data frames we could change the value of data

* We can also keep all of the values that are shared as defaults if we want to

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point(mapping = aes(color = TREATMENT)) +
  geom_smooth(method = "lm")
```

* Do an exercise that uses this idea, but uses `geom_histogram()` twice to make two overlapping histograms from two different columns
* What are we going to change between the two uses of `geom_histogram()` to do this?

> Do Task 3 in [Acacia and Ants Layers]({{ site.baseurl }}/exercises/Graphing-acacia-ants-layers-R).


### Understanding defaults (optional if students struggling after exercise)

* Let's move some things around to help understand where to put different information data and mapping

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = AXIS1)) +
  geom_point() +
  geom_smooth(method = "lm")
```

* What happens if we move `data` and `mapping` to one layer

```r
ggplot() +
  geom_point(data = acacia, mapping = aes(x = CIRC, y = AXIS1)) +
  geom_smooth(method = "lm")
```

* What about the other layer

```r
ggplot() +
  geom_point() +
  geom_smooth(data = acacia, mapping = aes(x = CIRC, y = AXIS1), method = "lm")
```

* What if we move one to each layer (error)

```r
ggplot() +
  geom_point(data = acacia) +
  geom_smooth(mapping = aes(x = CIRC, y = AXIS1), method = "lm")
```

* So, each geom needs access to `data` and `mapping`
* If they are not in the geom then the geom uses the defaults `ggplot()`
* If we want different `data` or `mapping` for different layers then provide different values to different geoms

```r
ggplot(data = acacia, mapping = aes(x = CIRC)) +
  geom_point(mapping = aes(y = AXIS1), color = "black") +
  geom_point(mapping = aes(y = AXIS2), color = "grey")
```

### Grammar of graphics

* Uniquely describe any plot based on a defined set of information
* Leland Wilkinson
* Geometric object(s)
  * Data
  * Mapping
  * Statistical transformation
  * Position (allows you to shift objects, e.g., spread out overlapping data points)
* Facets
* Coordinates (coordinate systems other than cartesian, also allows zooming)

### Column names with special characters

* Some data includes special characters in column names
* Load data from one of our upcoming exercises

```r
life_history_data <- read_tsv("Mammal_lifehistories_v2.txt")
life_history_data
```

* If we type this R will thinks we mean "run the mass function with an input of g"

```r
filter(life_history_data, mass(g) > 100000)
```

* So, we enclose these column names in back ticks

```r
filter(life_history_data, `mass(g)` > 100000)
```

### Saving plots as new files

```r
ggsave("acacia_by_treatment.jpg")
```
* The type of the file is determined by the file extension

```r
ggsave("acacia_by_treatment.pdf")
```

* Lots of optional arguments including size

```r
ggsave("acacia_by_treatment.pdf", height = 5, width = 5)
```

> Assign the rest of the exercises.
