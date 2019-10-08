---
layout: page
element: notes
title: Basic Debugging
language: R
time: 20 minutes
---

> * Copy and paste the example broken script into R

## Basic Manual Debugging Strategy

* How do we figure out what's wrong with a program?
    * Be a scientist.
        * Hypothesize about what is wrong.
        * Make one change that is expected to fix error.
        * Check if change worked/fixed error.
    * **Do not change something without a reason.**
    * Developing hypotheses (observe)
      * See where the code failed.
      * Read the error message.
      * Observe what the code is doing.
        * Look at the current state of the environment (snapshot of what's going on)
        * Talk through the code.
        * [Rubber duck programming](https://en.wikipedia.org/wiki/Rubber_duck_debugging)
    * Run the code line by line checking each step.

### Example

> * Creat a file with the following code in it
> * Run it
> * Work through debugging the code

```r
library(dplyr)
library(ggplot)

surveys <- read.csv('https://ndownloader.figshare.com/files/2292172')

do_counts_by_year <- surveys %>%
  filter(species == "DO") %>%
  group_by(year)
  summarize(count = n())

ggplot(do_counts_by_year, aes(x = year, y = count)) +
  geom_point() +
  geom_line() +
  labels(x = "Year", y = "Count")
```

### Debugged version of example

```r
library(dplyr)
library(ggplot2)

surveys <- read.csv('https://ndownloader.figshare.com/files/2292172')

do_counts_by_year <- surveys %>%
  filter(species_id == "DO") %>%
  group_by(year) %>%
  summarize(count = n())

ggplot(do_counts_by_year, aes(x = year, y = count)) +
  geom_point() +
  geom_line() +
  labs(x = "Year", y = "Count")
```