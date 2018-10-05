---
layout: exercise
topic: Making Choices
title: Simple If Statement
language: R
---

To determine if a file named `thesis_data.csv` exists in your working directory
you can use the code to get a list of available files and directories:

```
list.files()
```

1. Use the `%in%` operator to write a conditional statement that checks to see
   if `thesis_data.csv` is in this list.
2. Write an `if` statement that loads the file using `read.csv()` only if the
   file exists.
3. Add an `else` clause that prints "OMG MY THESIS DATA IS MISSING. NOOOO!!!!"
   if the file doesn't exist.
4. Make sure your actual thesis data is backed up.