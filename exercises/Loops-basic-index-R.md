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
2. Use the vector `odds <- seq(1, 9, by = 2)` and a loop to square these numbers
   and print them one at a time. Choose a descriptive variable to identify the 
   index values, such as `for (odd in odds)`.
3. Instead of printing the values produced by this for loop, store them in a new
   vector named `output`. The following code provides a template for doing this: 

   ```
   output <- c()
   for (odd in _____) {
     _____ <- _____^2
     output <- c(output, odds_squared)
   }
   ```
