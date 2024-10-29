---
layout: exercise
topic: Loops
title: Basic For Loops
language: R
---

1\. The code below prints the numbers 1 through 5 one line at a time. Modify it to print each of these numbers multiplied by 3.

```r
numbers <- c(1, 2, 3, 4, 5)
for (number in numbers){
  print(number)
}
```

2\. Write a for loop that loops over the following vector and prints out the mass in kilograms (`mass_kg = 2.2 * mass_lb`)

```r
mass_lbs <- c(2.2, 3.5, 9.6, 1.2)
```

3\. Complete the code below so that it prints out the name of each bird one line at a time.

```r
birds = c('robin', 'woodpecker', 'blue jay', 'sparrow')
for (i in 1:length(_________)){
  print(birds[__])
}
```

4\. Complete the code below so that it stores one area for each radius.

```r
radius <- c(1.3, 2.1, 3.5)
areas <- vector(_____ = "numeric", length = ______)
for (__ in 1:length(________)){
  areas[__] <- pi * radius[i] ^ 2
}
areas
```

5\. Write a for loop that loops over the following vector and stores the height in meters (height_m = height_ft / 3.28) in a new vector. After the for loop make sure to display the vector to the console by running the vectors name on its own line.

```r
height_ft <- c(5.1, 6.3, 5.7, 5.4)
```

6\. Complete the code below to calculate an area for each pair of `lengths` and `widths`, store the areas in a vector, and after they are all calculated print them out: 

```r
lengths = c(1.1, 2.2, 1.6)
widths = c(3.5, 2.4, 2.8)
areas <- vector(length = __________)
for (i in _____) {
  areas[__] <- lengths[__] * widths[__]
}
areas
```
