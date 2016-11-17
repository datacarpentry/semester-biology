---
layout: page
element: notes
title: Graphing using ggplot
language: R
---
 
> Set up R console:

```
library(dplyr)
library(ggplot2)

acacia <- read.csv("http://www.esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt", sep="\t")
```

> Get familiarized with [metadata](http://www.esapubs.org/archive/ecol/E095/064/metadata.php) - Acacia drepanolobium Surveys
				 
### Basics

* [`ggplot()`](http://docs.ggplot2.org/current/ggplot.html) arguments:
    * default dataset 
    * set of mappings
        * 'Aesthetics' from variables
    * `ggplot(acacia, aes(x = CIRC, y = AXIS1))`
* Add components of figures with layers
    * [`geom_point()`](http://docs.ggplot2.org/current/geom_point.html)

* Simple scatter plot showing branch circumference and canopy width

```
ggplot(acacia, aes(x = CIRC, y = AXIS1)) + 
  geom_point()
```

* Rescale variables with mapping

```
ggplot(acacia, aes(x = CIRC, y = log10(AXIS1))) +
  geom_point()
```

* Rescale variables with layer
    * [`scale_continuous()`](http://docs.ggplot2.org/current/scale_continuous.html)

```
ggplot(acacia, aes(x = CIRC, y = AXIS1)) +
  geom_point() +
  scale_y_log10()
```

* Labels and theme

```
ggplot(acacia, aes(x = CIRC, y = AXIS1)) +
  geom_point(size = 3, color = "red") +
  scale_y_log10() +
  labs(x = "Circumference [cm]", y = "Canopy Width [m]",
       title = "Acacia Survey at UHURU") +
  annotation_logticks(sides = "l") +
  theme_bw()
```

> Do [Exercise 2 - Mass vs Metabolism]({{ site.baseurl }}/exercises/Graphing-mass-vs-metabolism-R).

### Grouping

* Group on a single graph

```
ggplot(acacia, aes(x = CIRC, y = AXIS1, color = ANT)) +
  geom_point()
```

* Facet specification

```
ggplot(acacia, aes(x = CIRC, y = AXIS1)) +
  geom_point() +
  facet_wrap(~ANT)
```

> Do Tasks 1-4 in [Exercise 3 - Adult vs Newborn Size]({{ site.baseurl }}/exercises/Graphing-adult-vs-newborn-size-R).

### Layers

* Usage
    * `ggplot()` sets defaults for layers
    * Combine layers with `ggplot()` using `+`
    * Must have at least one layer to plot
    * Add additional layers, as necessary
        * Order matters

* Combining different kinds of layers

```
ant_acacia <- filter(acacia, ANT %in% c("CM", "CS", "TP"))
ggplot(ant_acacia, aes(x = CIRC, y = AXIS1)) +
  geom_point() +
  geom_smooth(method = "lm") +
  facet_wrap(~ANT)
```

* Combining different data sources

```
ggplot(acacia, aes(x = CIRC, y = AXIS1)) +
  geom_point() +
  geom_point(data = acacia, aes(x = year, y = AXIS2), color = "red") +
  labs(x = "Circumference [cm]", y = "Canopy Width [m]")
```

* Each layer will default to `ggplot()` mappings unless modified
    * So, we don't have to specify the arguments that are the same

```
ggplot(acacia, aes(x = CIRC, y = AXIS1)) +
  geom_point() +
  geom_point(aes(y = AXIS2), color = "red") +
  labs(x = "Circumference [cm]", y = "Canopy Width [m]")
```

> Do Task 5 in [Exercise 3 - Adult vs Newborn Size]({{ site.baseurl }}/exercises/Graphing-adult-vs-newborn-size-R).

### Statistical transformations

* Geoms include statistical transformations
* So far we've seen
    * `identity`: the raw form of the data or no transformation
    * `smooth`: model line (e.g., `loess`, `lm`)
* Transformations also exist to make things like histograms, bar plots, etc.
* Occur as defaults in associated Geoms

* To look at the abundances of different ant associations in the dataset, use a
bar plot
    * [`geom_bar()`](http://docs.ggplot2.org/current/geom_bar.html)

```
ggplot(acacia, aes(x = ANT)) + 
  geom_bar()
```

* Uses the transformation `stat_count()`
    * Counts the number of rows for each species

* To look at the distribution of circumferences in the dataset use a histogram
    * [`geom_histogram()`](http://docs.ggplot2.org/current/geom_histogram.html)

```
ggplot(acacia, aes(x = CIRC)) +
  geom_histogram()
```

* Uses `stat_bins()` for data transformation
    * Splits circumferences into bins and counts rows in each bin
* Uses `bins` argument to split data into groups
    * Defaults to `bins = 30` if not specified in function call

* These can be combined with all of the other `ggplot2` features we've learned

```
ggplot(acacia, aes(x = CIRC, fill = ANT)) +
  geom_histogram(bins = 15) +
  scale_x_log10() +
  annotation_logticks(sides = "b") +
  facet_wrap(~TREATMENT) +
  labs(x = "Circumference", y = "Number of Individuals") +
  theme_bw(base_size = 16)
```

### Additional information

* Geometric object
    * [`geom_point()`](http://docs.ggplot2.org/current/geom_point.html)
    * [`geom_line()`](http://docs.ggplot2.org/current/geom_path.html)
* Statistical visualization
    * [`geom_smooth()`](http://docs.ggplot2.org/current/geom_smooth.html)
    * [`geom_bar()`](http://docs.ggplot2.org/current/geom_bar.html)
    * [`geom_histogram()`](http://docs.ggplot2.org/current/geom_histogram.html)
    * [`geom_boxplot()`](http://docs.ggplot2.org/current/geom_boxplot.html)
* Dataset and aesthetic adjustments
    * [`scale_continuous()`](http://docs.ggplot2.org/current/scale_continuous.html)
    * [`scale_manual()`](http://docs.ggplot2.org/current/scale_manual.html)
    * [`lims()`](http://docs.ggplot2.org/current/lims.html)
    * [`labs()`](http://docs.ggplot2.org/current/labs.html)
    * [`guide_legend()`](http://docs.ggplot2.org/current/guide_legend.html)
    * [`theme()`](http://docs.ggplot2.org/current/theme.html), `theme_bw()`, `theme_classic()`
* Grouping related data
    * Same plot
        * Assign grouping variables as default or layer `aes()`
            * `group`
            * `color`
            * `shape`
    * Multiple plots
        * [`facet_grid()`](http://docs.ggplot2.org/current/facet_grid.html)
        * [`facet_wrap()`](http://docs.ggplot2.org/current/facet_wrap.html)
