---
layout: page
element: notes
title: Programming Style Introduction
language: R
--- 

### Basics

* Readability is important
* E.g.,

    My name is Ethan. I am 36 years old.

    MYnameIS          ETHAN................... I_AM_36 years
                 OLD

* Follow basic rules that make things readable
* Using the same style consistently
* Use the same style as others
* Style Guide

### Whitespace

* Indentation what the brain recognizes, use it regardless of language (and braces)
* 2 space indents

```
stuff <- data %>%
filter() %>%
select()
things <- 2
```

```
stuff <- data %>%
  filter() %>%
  select()
things <- 2
```

* Spaces after commas and around operators

```
range(x, x + 10)
```

### Naming

* snake_case
* Descriptive: `estimate_biomass`
* Not too long: `estimate_biomass_using_hanson_method`
* Use whole words for accessibility

### Long lines

* Lines < 80 characters long
* Add an indicator for this in RStudio
    * Tools -> Global Options -> Code -> Display -> Show Margin
* Use implied line continuation
    * If it's clear that a line isn't finished R will go on to the next line

```
site_data <- data.frame(
  site_id = c(1, 2, 3, 4),
  type = c('control', 'control', 'experiment', 'experiment')
)
```

* Read top to bottom
