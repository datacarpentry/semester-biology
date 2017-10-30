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

Modify this code to accomplish each of the following tasks: 

1. Multiply each of the numbers 1 through 5 by 3, then print the result. 
2. Multiply each of the numbers 6 through 10 by 3, then print the result. 
3. Use the vector of the first five odd numbers produced by `seq(1, 9, by = 2)`
   to print the first five odd numbers squared one line at a time. Choose a
   descriptive variable to identify the index values, such as `for (odd in 
   odds)`.
4. Modify your `for` loop from task 3 to `paste()` and print a statement for 
   each odd number in the form "`odd` squared is `odd_squared`". The first line
   should be "1 squared is 1". 
5. Create a vector of a `seq()` of numbers from 5 to 50 by 5 and use it in a
   `for` loop to generate another vector of those numbers squared. Your `for`
   loop should look something like:

   ```
   output <- c()
   for (number in _____) {
     _____ <- _____^2
     output <- c(output, number_squared)
   }
   ```