---
layout: exercise
topic: dplyr
title: Building data frames from vectors
language: R
---
Los siguientes vectores contienen datos individuales sobre el largo, ancho y alto de 10 tejos.
[* Taxus baccata *] (https://es.wikipedia.org/wiki/Taxus_baccata):
```
length <- c(2.2, 2.1, 2.7, 3.0, 3.1, 2.5, 1.9, 1.1, 3.5, 2.9)
width <- c(1.3, 2.2, 1.5, 4.5, 3.1, NA, 1.8, 0.5, 2.0, 2.7)
height <- c(9.6, 7.6, 2.2, 1.5, 4.0, 3.0, 4.5, 2.3, 7.5, 3.2)

Haga un marco de datos que contenga estos tres vectores como columnas junto con una columna `genus` que contenga el nombre *Taxus* en todas las filas y una columna `species` que contenga la palabra *baccata * en todas las filas.