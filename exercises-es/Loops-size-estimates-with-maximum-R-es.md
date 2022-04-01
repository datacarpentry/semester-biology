---
layout: exercise
topic: Loops
title: Size Estimates With Maximum
language: R
---
Esta es una continuación de la Parte 1 [Size Estimates Vectorized]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R).

Cree una nueva versión de la función `mass_from_length_theropoda()` de la Parte 1 de [Size Estimates Vectorized]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R) llamada `mass_from_length_max()`. Esta función solo debe calcular una masa si el valor de `length` pasado a la función es menor que 20. Si `length` es mayor que 20, debe devuelver `NA` en su lugar. Use `sapply()` y esta nueva función para estimar la masa de los datos de `theropoda_lengths` de [Size Estimates Vectorized]({{ site.baseurl }}/exercises/Loops-size-estimates-vectorized-R).