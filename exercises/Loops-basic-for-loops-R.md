---
layout: exercise
topic: Loops
title: Basic For Loops
language: R
---

1\. The code below prints the numbers 1 through 5 one line at a time. Modify it to print the numbers 2 through 16.

```r
for (i in 1:5){
  print(i)
}
```

2\. The code below prints the numbers 1 through 5 one line at a time. Modify it to print each of these numbers multiplied by 3.

```r
for (i in 1:5){
  print(i)
}
```

3\. Complete the code below so that it prints out the name of each bird one line at a time.

```r
birds = c('robin', 'woodpecker', 'blue jay', 'sparrow')
for (i in 1:length(_________)){
  print(birds[__])
}
```

4\. Complete the code below to calculate a mass for each volume in `volumes`, store them in a vector, and then print them out: 

```r
volumes = c(16.8, 26.2, 42.0, 6.2, 19)
masses <- vector(length = __________)
for (i in _____) {
  masses[__] <- 0.8 * volumes[i] ^ 1.6
}
masses
```
