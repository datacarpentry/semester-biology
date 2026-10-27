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

2\. Write a for loop that loops over the following vector and prints out the mass in kilograms (`mass_kg = mass_lb / 2.2`)

```r
mass_lbs <- c(2.2, 3.5, 9.6, 1.2)
```

3\. Write a for loop that loops over the following vector of temperatures in Celsius and prints out each temperature in Fahrenheit (`temp_f = temp_c * 9 / 5 + 32`)

```r
temps_c <- c(12.5, 18.1, 22.3, 9.8, 15.0)
```

4\. Complete the code below so that it prints out the name of each bird one line at a time.

```r
birds = c('robin', 'woodpecker', 'blue jay', 'sparrow')
for (i in 1:length(_________)){
  print(birds[__])
}
```

5\. Complete the code below so that it stores one area for each radius.

```r
radius <- c(1.3, 2.1, 3.5)
areas <- vector(_____ = "numeric", length = ______)
for (__ in 1:length(________)){
  areas[__] <- pi * radius[i] ^ 2
}
areas
```

6\. Complete the code below so that it stores the upper case version of each species name (using `toupper()`) and then displays the vector after the loop.

```r
species <- c('Dipodomys merriami', 'Chaetodipus penicillatus', 'Neotoma albigula')
species_upper <- vector(mode = "_________", length = ________)
for (i in 1:length(_______)){
  species_upper[__] <- toupper(species[__])
}
species_upper
```

7\. Write a for loop that loops over the following vector and stores the height in meters (height_m = height_ft / 3.28) in a new vector.

```r
height_ft <- c(5.1, 6.3, 5.7, 5.4)
```

8\. Complete the code below to calculate an area for each pair of `lengths` and `widths`, store the areas in a vector, and after they are all calculated print them out: 

```r
lengths = c(1.1, 2.2, 1.6)
widths = c(3.5, 2.4, 2.8)
areas <- vector(length = __________)
for (i in _____) {
  areas[__] <- lengths[__] * widths[__]
}
areas
```

9\. Write a for loop that uses the following vectors to calculate the density of animals in each plot (`density = count / area`), stores the densities in a vector, and after the loop displays the vector.

```r
counts <- c(12, 25, 7, 18)
areas <- c(2.5, 4.0, 1.2, 3.6)
```
