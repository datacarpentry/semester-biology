---
layout: exercise
topic: Loops
title: Size Estimates Vectorized
language: R
---

Esta es una continuación de [Usar y modificar]({{ site.baseurl }}/exercises/Functions-use-and-modify-R).

1. Escriba una función llamada `mass_from_length_theropoda()` que tome `length` como argumento para obtener una estimación de los valores de masa del dinosaurio *Theropoda*. Use la ecuación `masa <- 0.73 * length^3.63`. Copie los siguientes datos en R y pase el vector completo a su función para calcular la masa estimada de cada dinosaurio.

`Theropoda_lengths <- c (17,8013631070471, 20,3764452071665, 14,0743486294308, 25,65782386974, 26,0952008049675, 20,3111541103134, 17,5663244372533, 11,2563431277577, 20,081903202614, 18,6071626441984, 18,0991894513166, 23,0659685685892, 20,5798853467837, 25,6179254233558, 24,3714331573996, 26,2847248252537, 25,4753783544473, 20,4642089867304, 16,0738256364701, 20,3494171706583, 19,854399305869, 17,7889814608919, 14,8016421998303, 19,6840911485379, 19,4685885050906, 24,4807784966691, 13,3359960054899, 21,5065994598917, 18,4640304608411, 19,5861532398676, 27,084751999756, 18,9609366301798, 22,4829168046521, 11,7325716149514, 18,3758846100456, 15,537504851634, 13,4848751773738, 7,68561192214935, 25,5963348603783, 16,588285389794) `

2. Cree una nueva versión de la función llamada `mass_from_length()` que use la ecuación `mass <- 0.73 * length^3.63` y tome `length`, `a` y `b` como argumentos. En los argumentos de la función, establezca los valores predeterminados para `a` en `0.73` y `b` en `3.63`. Si ejecuta esta función solo con los datos de longitud de la Parte 1, debería obtener el mismo resultado que la Parte 1. Copie los datos a continuación en R y llame a su función usando el vector de longitudes de la Parte 1 (arriba) y estos vectores de valores de `a` y `b` para estimar la masa de los dinosaurios usando diferentes valores de `a` y `b`.


`a_Values ​​<- C (0.759, 0.751, 0.74, 0.746, 0.759, 0.746, 0.759, 0.751, 0.749, 0.751, 0.738, 0.768, 0.736, 0.749, 0.746, 0.744, 0.746, 0.744, 0.749, 0.751, 0.749, 0.751, 0.749, 0.751, 0.744, 0.751, 0.744, 0.754, 0.744, 0.754, 0.774, 0.754, 0.774, 0.751, 0.763, 0.749, 0.763, 0.749, 0,741, 0,754, 0,746, 0,755, 0,764, 0,758, 0,76, 0,748, 0,745, 0,756, 0,739, 0,733, 0,757, 0,747, 0,741, 0,752, 0,752, 0,748)`

`b_values ​​<- c (3.627, 3.633, 3.626, 3.633, 3.627, 3.633, 3.627, 3.629, 3.632, 3.628, 3.633, 3.627, 3.621, 3.63, 3.631, 3.632, 3.628, 3.626, 3.639, 3.626, 3.635, 3.629, 3.635, 3.629, 3.642, 3.632, 3.633, 3.629, 3.62, 3.619, 3.638, 3.627, 3.621, 3.628, 3.628, 3.635, 3.624, 3.621, 3.621, 3.632, 3.627, 3.624, 3.634, 3.621)`

3. Cree un marco de datos para estos datos usando `dino_data <- data.frame(theropoda_lengths, a_values, b_values)`. Use `dplyr` para agregar una nueva columna `masses` a este marco de datos (usando `mutate()` y su función) e imprima el resultado en la consola.
