---
layout: exercise
topic: Loops
title: Basic Index
language: R
---

The following code prints the first five whole numbers one line at a time:

```
for (i in 1:5){
  print(i)
}
```

1. Modify the code to print three times each of the numbers from 1 to 5 one line
   at a time.
2. Modify the code to print three times each of the numbers from 6 to 10 one
   line at a time.
3. Use the vector of the first five odd numbers produced by `seq(1, 9, by = 2)`
   to print the first five odd numbers squared one line at a time. *Use a
   descriptive variable to identify the index values such as `for (odd in 
   odds)`.*
4. Modify your odd numbers squared `for` loop to `paste()` and print a
   statement for each odd number in the form "`odd` squared is `odd_squared`".