---
layout: exercise
topic: Loops
title: Basic For Loops
language: R
---
1\. El siguiente código imprime los números del 1 al 5 una línea a la vez. Modifíquelo para imprimir los números del 2 al 16.

```r
for (i in 1:5){
  print(i)
}
```

2\. El siguiente código imprime los números del 1 al 5 una línea a la vez. Modifíquelo para imprimir cada uno de estos números multiplicado por 3.

```r
for (i in 1:5){
  print(i)
}
```

3\. Complete el código a continuación para que imprima el nombre de cada ave una línea a la vez.

```r
birds = c('robin', 'woodpecker', 'blue jay', 'sparrow')
for (i in 1:length(_________)){
  print(birds[__])
}
```

4\. Complete el código a continuación para que almacene un área para cada radio.

```r
radius <- c(1.3, 2.1, 3.5)
areas <- vector(_____ = "numeric", length = ______)
for (__ in 1:length(________)){
  areas[__] <- pi * radius[i] ^ 2
}
areas
```


5\. Complete el siguiente código para calcular un área para cada par de `lengths` y `widths`, almacene las áreas en un vector y, una vez calculadas, imprímalas:

```r
lengths = c(1.1, 2.2, 1.6)
widths = c(3.5, 2.4, 2.8)
areas <- vector(length = __________)
for (i in _____) {
  areas[__] <- lengths[__] * widths[__]
}
areas
```
