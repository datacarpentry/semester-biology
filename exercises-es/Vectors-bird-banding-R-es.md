---
layout: exercise
topic: Vectors
title: Bird Banding
language: R
translation: es
título: Anillamiento de aves
---
El número de aves anilladas en unos sitios de muestreo ha sido contado por
su equipo de campo e ingresado en el siguiente vector. Los conteos se ingresan en el orden pertinente al sitio de muestreo, es decir, la posición 1 del vector corresponde a los pájaros contados en el sitio de conteo 1. Corte y pegue el vector en su
tarea y responda las siguientes preguntas usando funciones predeterminadas. Imprima el resultado a la pantalla. Algunas funciones de R que serán útiles incluyen `length()`,
`max()`, `min()`, `sum()`, `mean()` y `[]`.

```
number_of_birds <- c(28, 32, 1, 0, 10, 22, 30, 19, 145, 27, 
36, 25, 9, 38, 21, 12, 122, 87, 36, 3, 0, 5, 55, 62, 98, 32, 
900, 33, 14, 39, 56, 81, 29, 38, 1, 0, 143, 37, 98, 77, 92, 
83, 34, 98, 40, 45, 51, 17, 22, 37, 48, 38, 91, 73, 54, 46,
102, 273, 600, 10, 11)
```
1. ¿Cuántos sitios de muestreo hay?
2. ¿Cuántas aves se contaron en el sitio de muestreo 42?
3. ¿Cuál es el número total de aves contadas en todos los sitios de muestreo?
4. ¿Cuál es el menor número de aves contadas?
5. ¿Cuál es el mayor número de aves contadas?
6. ¿Cuál es el número promedio de aves contadas?
7. ¿Cuántas aves se contaron en el último sitio? Haga que la computadora elija el
   último sitio automáticamente, no ingrese manualmente la posición.
   ¿Conoce de alguna función que le devuelva la posición del último valor?
   (dado que las posiciones comienzan en 1, la posición del último valor en un vector es
   igual que su longitud).
