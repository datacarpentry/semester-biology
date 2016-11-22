---
layout: exercise
topic: Loops
title: Basic Index
language: R
---

The following code prints the first five whole numbers one line at a time:

```
for (i in 1:4){
  print(i)
}
```

1. Modify the code to print five orders of magnitude (*from one to ten
   thousand*) one line at a time.
2. Modify the code to print ten orders of magnitude (*from one to one billion*)
   one line at a time.
3. Modify the code to print ten orders of magnitude (*from one thousandth to one
   thousand*) one line at a time.
4. Use the vector of the first five odd numbers produced by `seq(1, 9, by = 2)`
   to print the first five odd numbers squared one line at a time.