---
layout: page
element: notes
title: Graphing using ggplot
language: R
---
 
> Get familiarized with [metadata](http://www.esapubs.org/archive/ecol/E095/064/metadata.php) - *Acacia drepanolobium* Surveys

### ggplot

* Very popular plotting package
* Good plots quickly
* Declarative - describe what you want not how to build it
* Contrasts w/Imperative - how to build it step by step
* Install `ggplot2` using `install.packages`

### Data

* Data on acacia size in an experiment in Kenya excluding large herbivores
* *Download both UHURU datasets into new project*
* Data is tab separated
* Includes information on if the plant is dead in the HEIGHT column

```
acacia <- read.csv("http://www.esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt", sep="\t", na.strings = c("dead"))
```

* *Show data and talk through treatments, sizes, and ants*
  
### Basics

```
library(ggplot2)
```

* `ggplot()` creates a base ggplot object that we can then add things to
* Like a blank canvas
* Optional arguments for information to be shared across different components
  of the plot including
  * default dataset - what data are we working with
  * set of mappings or 'Aesthetics' that describe which columns are used for
      different aspects of the plot

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT))
```

* This doesn't create a figure, it's just a blank canvas and some information on
  default values for data and mapping columns to pieces of the plot
* Add components of figures with layers
* Scatter plot showing branch circumference and height

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point()
```

* To change things about the layer pass arguments to the geom

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, color = "blue", alpha = 0.5)
```

* Add Labels (documentation for your graphs!)

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, color = "blue", alpha = 0.5) +
  labs(x = "Circumference [cm]", y = "Height [m]",
       title = "Acacia Survey at UHURU")
```

> Do Task 1 in [Acacia and ants]({{ site.baseurl }}/exercises/Graphing-acacia-ants-R).

### Grouping

* Group on a single graph
* Look at influence of experimental treatment

```
ggplot(acacia, aes(x = CIRC, y = HEIGHT, color = TREATMENT)) +
  geom_point(size = 3, alpha = 0.5)
```

* Facet specification

```
ggplot(acacia, aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, alpha = 0.5) +
  facet_wrap(~TREATMENT)
```

* Where are all the acacia in the open plots? (eaten?)

> Do Tasks 2-3 in [Acacia and ants]({{ site.baseurl }}/exercises/Graphing-acacia-ants-R).

### Rescaling axes

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point(size = 3, color = "blue", alpha = 0.5) +
  scale_y_log10() +
  scale_x_log10()
```

* Not changing the data itself, just the presentation of it

> Assign [Mass vs Metabolism]({{ site.baseurl }}/exercises/Graphing-mass-vs-metabolism-R) and Tasks 1-4 in [Adult vs Newborn Size]({{ site.baseurl }}/exercises/Graphing-adult-vs-newborn-size-R).

### Layers

* We've seen that ggplot makes graphs by combining information on
  * Data
  * Mapping of parts of that data to aspects of the plot
  * A geometric object to represent the data

```
ggplot(acacia, aes(x = CIRC, y = HEIGHT)) +
  geom_point()
```

* Many kinds of geometric object (type `geom_` and show completions)

* Usage
    * `ggplot()` sets defaults for layers
    * Can combine multiple layers using `+`
        * Order matters

* Combine different kinds of layers
* Add a linear model

```
ggplot(acacia, aes(x = CIRC, y = HEIGHT)) +
  geom_point() +
  geom_smooth(method = "lm")
```

* Both the `geom_point` layer and the `geom_smooth` layer use the defaults form
  `ggplot`
* Both use `acacia` for data and `x = CIRC, y = HEIGHT` for the aesthetic

* Do this by treatment

```
ggplot(acacia, aes(x = CIRC, y = HEIGHT, color = TREATMENT)) +
  geom_point() +
  geom_smooth(method = "lm")
```

* One set of points and one model for each treatment

> Do Task 4 in [Acacia and ants]({{ site.baseurl }}/exercises/Graphing-acacia-ants-R).

### Statistical transformations

* Geoms include statistical transformations
* So far we've seen
    * `identity`: the raw form of the data or no transformation
    * `smooth`: model line (e.g., `loess`, `lm`)
* Transformations also exist to make things like histograms, bar plots, etc.
* Occur as defaults in associated Geoms

* To look at the number of acacia in each treatment use a bar plot
    * [`geom_bar()`](http://docs.ggplot2.org/current/geom_bar.html)

```
ggplot(acacia, aes(x = TREATMENT)) +
  geom_bar()
```

* Uses the transformation `stat_count()`
    * Counts the number of rows for each treatment

* To look at the distribution of circumferences in the dataset use a histogram
    * [`geom_histogram()`](http://docs.ggplot2.org/current/geom_histogram.html)

```
ggplot(acacia, aes(x = CIRC)) +
  geom_histogram(fill = "red")
```

* Uses `stat_bins()` for data transformation
    * Splits circumferences into bins and counts rows in each bin
* Set number of `bins` or `binwidth`

```
ggplot(acacia, aes(x = CIRC)) +
  geom_histogram(fill = "red", bins = 15)
```

```
ggplot(acacia, aes(x = CIRC)) +
  geom_histogram(fill = "red", binwidth = 5)
```

* These can be combined with all of the other `ggplot2` features we've learned

> Do Tasks 1-2 in [Acacia and ants histograms]({{ site.baseurl }}/exercises/Graphing-acacia-ants-histograms-R).

### Changing values across layers

* We can also plot data from different columns or even data frames on the same graph
* To do this we need to better understand how layers and defaults work
* So far we've put all of the information on data and aesthetic mapping into `ggplot()`

```r
ggplot(data = acacia, mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point()
```

* This sets the default data frame and aesthetic, which is then used by
  `geom_point()`
* Alternatively instead of setting the default we could just give these values
  directly to `geom_point()`

```r
ggplot() +
  geom_point(data = acacia,
             mapping = aes(x = CIRC, y = HEIGHT,
                           color = TREATMENT))
```

* We can see that this information is no longer shared with other geoms since it
  is no longer the default

```r
ggplot() +
  geom_point(data = acacia,
             mapping = aes(x = CIRC, y = HEIGHT)) +
                           color = TREATMENT))
  geom_smooth()
```

* Can use this combine different aesthetics
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

> Do Task 3 in [Acacia and ants histograms]({{ site.baseurl }}/exercises/Graphing-acacia-ants-histograms-R).

### Grammar of graphics

* Geometric object(s)
  * Data
  * Mapping
  * Statistical transformation
  * Position (allows you to shift objects, e.g., spread out overlapping data points)
* Facets
* Coordinates (coordinate systems other than cartesian, also allows zooming)
* In combination uniquely describes any plot

### Saving plots as new files

```
ggsave(“acacia_by_treatment.jpg”)
```

* Lots of optional arguments
    * Location
    * Type
    * Size

```
ggsave(“figures/acacia_by_treatment.pdf”, height = 5, width = 5)
```

> Assign the rest of the exercises.


### Combining different datasets (time allowing)

* We can use this to plot data from different sources together
* Add tree size data for context
* Layers are plotted in the order they are added

* Use the `readr` package to read in this data
* It has a lot of issues and `readr` fixes many of them automatically

```r
library(readr)
trees <- read_tsv("data/TREE_SURVEYS.txt")
ggplot() +
  geom_point(data = trees,
             aes(x = CIRC, y = HEIGHT),
             color = "gray") +
  geom_point(data = acacia,
             aes(x = CIRC, y = HEIGHT),
             color = "red") +
  labs(x = "Circumference [cm]", y = "Height [m]")
```

* Each layer will default to `ggplot()` mappings unless modified
    * So, we don't have to specify the arguments that are the same

```
ggplot(mapping = aes(x = CIRC, y = HEIGHT)) +
  geom_point(data = trees, color = "gray") +
  geom_point(data = acacia, color = "red") +
  labs(x = "Circumference [cm]", y = "Height [m]")
```