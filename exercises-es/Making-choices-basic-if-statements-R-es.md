---
layout: exercise
topic: Making Choices
title: Basic If Statements
language: R
---
1\. Complete (es decir, copie en su código y modifiquelo) la siguiente declaración `if`
   de manera que que si `age_class ` es igual a "sapling", el valor de Y sea: `y <- 10`.

```r
age_class = "sapling"
if (){
  
}
y
```

2\. Complete la siguiente declaración `if` de manera que si `age_class ` es igual a
   "sapling"  el valor de Y sea:  `y <- 10` y si `age_class ` es igual a "seedling"
    el valor de Y sea:  `y <- 5`.

```r
age_class = "seedling"
if (){
  
}
y
```

3\. Complete la siguiente declaración `if` de manera que si `age_class ` es igual a
   "sapling" establece `y <- 10` y si `age_class ` es igual a "seedling"
    el valor de Y sea:  `y <- 5` y si `clase_de_edad` es otra cosa, entonces el valor de Y sea: 
   `y <- 0`.


```r
age_class = "adult"
if (){
  
}
y
```

4\. Convierta su declaración condicional de (3) en una función que tome
   `age_class ` como argumento y devuelva `y`. Llame esta función 5 veces, una vez
   con cada uno de los siguientes valores de `age_class `: "sapling", "seedling",
   "adult", "mature", "established".
