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

* Using the same style as others is helpful

### Whitespace

* Indentation what the brain reconizes, use it regardless of language (and braces)
* 2 space indents

```
for (i in 1:10){
  do_things()
}
```

* Spaces after commas and around operators

```
range(x, x + 10)
```

### Naming

* snake_case

### Documentation & Comments

* Documentation
    * How to use code
    * Use Roxygen comments for functions
* Comments
    * Why & how code works
    * Only if it code is confusing to read

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
