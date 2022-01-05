---
layout: exercise
topic: Functions
title: for Loop
language: R
translation: es
titulo: for Loop
---
Esta tarea es continuación de [Funciones anidadas]({{site.baseurl}}/exercises-es/Funciones-combinando-funciones-R).

1. Ahora que ha impresionado a la abuela, es hora de ser científicos serios.
    Tome el siguiente vector de longitudes de estegosaurio

```
 lengths <- c(10.1, 9.5, 11.2, 9.8, 10.4, 12.0, 11.5, 9.5,
9.8, 10.0, 10.7, 10.2, 11.9, 9.7, 11.2, 11.8, 10.7)
```

y estime la masa en kilogramos para cada una de las longitudes del vector usando el bucle (loop) `for`, usando su función para estimar masa, `a = 10.95` y` b = 2.64`. Imprima el
resultados en orden.

2. Esta es una buena manera de aprender a usar un bucle (loop) "for", pero gracias a la vectorización
en R también podemos pasar todo el vector `lengths` a nuestra función. Pase el vector a la función y estime la masa para cada longitud e imprima el resultado.