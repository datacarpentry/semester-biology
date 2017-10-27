---
layout: exercise
topic: Making Choices
title: Simple If Statement
language: R
---

To determine if a file named `thesis_data.csv` exists in your working directory
you can use the code:

```
file.exists('thesis_data.csv')
```

This code returns TRUE if the files exists and FALSE if it does not.

1. Write an `if` statement that loads the file using `read.csv()` only if the
   file exists.
2. Add an `else` clause that prints "OMG MY THESIS DATA IS MISSING. NOOOO!!!!"
   if the file doesn't exist.
