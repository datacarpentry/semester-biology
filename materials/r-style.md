---
layout: page
element: notes
title: Programming Style Introduction
language: R
--- 

> This introduction is designed to be delivered before functions, loops, etc.
> are introduced. A more advanced version is available in
> [Programming Style Advanced]({{ site.baseurl }}/materials/R-style-adv).

### Basics

* Readability is important
* E.g.,

    My name is Ethan. I am 36 years old.

    MYnameIS          ETHAN................... I_AM_36 years
                 OLD

* Using the same style as others is helpful

### Whitespace

* Indentation what the brain reconizes, use it regardless of language (and braces)
* 2 space indents
* Spaces after commas and around operators

### Naming

* snake_case

### Long lines

* Lines < 80 characters long
* Use implied line continuation
    * If it's clear that a line isn't finished R will go on to the next line

```
site_data <- data.frame(
  site_id = c(1, 2, 3, 4),
  type = c('control', 'control', 'experiment', 'experiment')
)
```

* Read top to bottom
