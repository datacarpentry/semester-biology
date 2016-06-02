---
layout: page
element: notes
title: Graphing using ggplot
language: R
---

```
library(dplyr)
library(ggplot2)

surveys <- read.csv("surveys.csv")

ts_data <- surveys %>%
             group_by(species_id, year) %>%
             summarize(count = n(), biomass = sum(weight)) %>%

dm_ts_data <- ts_data %>% filter(species_id == "DM")
```
				 
* a default dataset and set of mappings from variables to aesthetics

`ggplot(dm_ts_data, aes(x = year, y = count))`

* one or more layers with
    * one geometric object (line, point, bar)
    * one statistical transformation (nothing, smoother, boxplot)
    * (optionally) dataset & aesthetic

```
ggplot(dm_ts_data, aes(x = year, y = count)) +
  geom_line()
```

```
ggplot(dm_ts_data, aes(x = year, y = count)) +
  geom_line() +
  geom_point() +
  geom_smooth()
```

```
do_ts_data <- filter(ts_data, species_id == "DO")
ggplot(dm_ts_data, aes(x = year, y = count)) +
  geom_line() +
  geom_line(data = do_ts_data, aes(x = year, y = count), color = "red")
```

* one scale for each aesthetic mapping used, common across layers

```
ggplot(dm_ts_data, aes(x = year, y = count)) +
  geom_line() +
  scale_y_log10()
```

* the facet specification

```
ggplot(ts_data, aes(x = year, y = count)) +
  geom_line() +
  facet_wrap(~species_id)
```

We can also group on a single graph by setting color or points by group:

```
ggplot(ts_data, aes(x = year, y = count, color = species_id)) +
  geom_line()
```

## Adding multiple layers

```
ggplot(ts_data, aes(x = year, y = count)) +
  geom_line() +
  geom_smooth() +
  facet_wrap(~species_id)
```

## Customizing

```
ggplot(ts_data, aes(x = year, y = count)) +
  geom_line(size = 1, color = "red") +
  geom_smooth(method = "lm") +
  facet_wrap(~species_id) +
  xlab("Year") +
  ylab("Number of Individuals") +
  ggtitle("Population Time-Series at Portal")
```
  
