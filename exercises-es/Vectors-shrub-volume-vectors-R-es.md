---
layout: exercise
topic: Vectors
title: Shrub Volume Vectors
language: R
translation: es
título: Vectores de volumen de arbustos
---
Los siguientes vectores contienen datos individuales sobre el largo, ancho y alto de 10 tejos.
[* Taxus baccata *] (https://es.wikipedia.org/wiki/Taxus_baccata):
```
length <- c(2.2, 2.1, 2.7, 3.0, 3.1, 2.5, 1.9, 1.1, 3.5, 2.9)
width <- c(1.3, 2.2, 1.5, 4.5, 3.1, NA, 1.8, 0.5, 2.0, 2.7)
height <- c(9.6, 7.6, 2.2, 1.5, 4.0, 3.0, 4.5, 2.3, 7.5, 3.2)
```

Copie estos vectores en un script de R y lleve acabo las siguientes premisas:

1. El volumen de cada arbusto (largo x ancho x alto).
   * Almacenar estos volúmenes en una variable facilitará  futuros cálculos *.
2. La suma del volumen de todos los arbustos (use la función predeterminada `sum()`).
3. Un vector que contenga la altura de los arbustos con longitudes > 2.5.
4. Un vector que contenga la altura de los arbustos con alturas > 5.
5. Un vector que contenga la altura de los primeros 5 arbustos (use la función predeterminada`[]`).
6. Un vector que contenga los volúmenes de los primeros 3 arbustos (use `[]`).

*Desafío opcional*: Cree un vector que contenga los volúmenes de los últimos 5 arbustos. El código debe devolver los últimos 5 valores independientemente de la longitud del vector (i.e., devolverá los últimos 5 valores si aunque el vector contenga 10, 20 o 50 arbustos).
