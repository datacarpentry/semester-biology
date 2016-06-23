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

surveys <- read.csv("surveys.csv")

ts_data <- surveys %>%
             group_by(species_id, year) %>%
             summarize(count = n(), biomass = sum(weight)) %>%

dm_ts_data <- filter(ts_data, species_id == "DM")
do_ts_data <- filter(ts_data, species_id == "DO")
```
				 
### Basics

* [`ggplot()`](http://docs.ggplot2.org/current/ggplot.html) arguments:
    * default dataset 
    * set of mappings
        * 'Aesthetics' from variables
    * `ggplot(dm_ts_data, aes(x = year, y = count))`
* `ggplot()` objects:
    * `p <- ggplot()`
* Layers:
    * Usage
        * `ggplot()` sets defaults for layers
        * Combine layers with `ggplot()` using `+`
        * Must have at least one layer to plot
        * Add additional layers, as necessary
            * Order matters
    * Geometric object
        * [`geom_line()`](http://docs.ggplot2.org/current/geom_path.html)
        * [`geom_bar()`](http://docs.ggplot2.org/current/geom_bar.html)
        * [`geom_point()`](http://docs.ggplot2.org/current/geom_point.html)
    * Statistical visualization
        * [`geom_boxplot()`](http://docs.ggplot2.org/current/geom_boxplot.html)
        * [`geom_smooth()`](http://docs.ggplot2.org/current/geom_smooth.html)
    * Dataset and aesthetic adjustments
        * [`scale_manual()`](http://docs.ggplot2.org/current/scale_manual.html)
        * [`lims()`](http://docs.ggplot2.org/current/lims.html)
        * [`labs()`](http://docs.ggplot2.org/current/labs.html)
        * [`guide_legend()`](http://docs.ggplot2.org/current/guide_legend.html)
        * [`theme()`](http://docs.ggplot2.org/current/theme.html), `theme_bw()`, `theme_classic()`
    * Grouping related data
        * Same plot
            * Assign grouping variables as default or layer `aes()`
                * `color`
                * `shape`
        * Multiple plots
            * [`facet_grid()`](http://docs.ggplot2.org/current/facet_grid.html)
            * [`facet_wrap()`](http://docs.ggplot2.org/current/facet_wrap.html)

### Plotting

* Simple line plot

```
ggplot(dm_ts_data, aes(x = year, y = count)) +
  geom_line()
```

* Line plot with statistics

```
ggplot(dm_ts_data, aes(x = year, y = count)) +
  geom_line() +
  geom_point() +
  geom_smooth(method = "lm")
```

* Plot multiple lines

```
ggplot(dm_ts_data, aes(x = year, y = count)) +
  geom_line() +
  geom_line(data = do_ts_data, aes(x = year, y = count), 
            color = "red")
```

* Rescale variables
    * One scale for each variable used
    * Scale common across layers

```
ggplot(dm_ts_data, aes(x = year, y = count)) +
  geom_line() +
  scale_y_log10()
```

* Group on a single graph

```
ggplot(ts_data, aes(x = year, y = count, color = species_id)) +
  geom_line()
```

* Facet specification

```
ggplot(ts_data, aes(x = year, y = count)) +
  geom_line() +
  facet_wrap(~species_id)
```

### Customizing plots

* Multiple layers

```
ggplot(ts_data, aes(x = year, y = count)) +
  geom_line() +
  geom_smooth(method = "lm") +
  facet_wrap(~species_id)
```

* Labels and theme

```
ggplot(ts_data, aes(x = year, y = count)) +
  geom_line(size = 1, color = "red") +
  geom_smooth(method = "lm") +
  facet_wrap(~species_id) +
  xlab("Year") +
  ylab("Number of Individuals") +
  ggtitle("Population Time-Series at Portal") +
  theme_bw(base_size = 12, base_family = "Helvetica")
```
