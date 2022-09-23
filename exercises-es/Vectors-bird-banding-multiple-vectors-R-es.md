---
layout: exercise
topic: Vectors
title: Bird Banding Multiple Vectors
language: R
translation: es
título: Anillamiento de aves, múltiples vectores
---
El número de aves anilladas en unos sitios de muestreo ha sido contado por
su equipo de campo e ingresado en el siguiente vector. Los conteos se ingresan en el orden pertinente al sitio de muestreo, es decir, la posición 1 del vector corresponde a los pájaros contados en el sitio de conteo 1.
Un segundo vector contiene información sobre la cantidad de árboles en cada sitio de muestreo.
Corte y pegue el vector en su
tarea y responda las siguientes preguntas usando funciones predeterminadas. Imprima el resultado a la pantalla.

```r
number_of_birds <- c(28, 32, 1, 0, 10, 22, 30, NA, 145, 27, 
36, 25, 9, 38, 21, 12, 122, 87, 36, 3, 0, 5, 55, 62, 98, 32, 
900, 33, 14, 39, 56, 81, 29, 38, 1, 0, 143, 37, 98, 77, 92, 
83, 34, 98, 40, 45, 51, 17, 22, 37, 48, NA, 91, 73, 54, 46,
102, 273, 600, 10, 11)
number_of_trees <- c(10, 12, 2, 3, 10, 8, 19, 19, 14, 3, 
4, 5, 8, 4, 8, 1, 12, 10, 3, 1, 2, 3, 5, 6, 8, 2, 
90, 3, 4, 3, 6, 8, NA, 4, 0, 1, 14, 3, 10, NA, 9, 
8, 4, 8, 4, 4, 5, 1, 2, 3, 5, 4, 10, 7, 5, 8,
10, 30, 26, 1, 6)
```

1. ¿Cuántos sitios de muestreo hay?
2. ¿Cuántas aves se contaron en el sitio de muestreo 26?
3. ¿Cuál es el mayor número de aves contadas?
4. ¿Cuál es el número promedio de aves contadas?
5. ¿Cuál es el número total de árboles contados en todos los sitios de muestreo?
6. ¿Cuál es el menor número de árboles contados?
7. Produzca un vector que contenga los conteos de aves en sitios de muestreo con al menos 10 árboles.
8. Produzca un vector que contenga el número de árboles contados en sitios de muestreo con al menos 10 árboles.
9. Combine los vectores `number_of_birds` y` number_of_trees` en un dataframe (marco de datos) como columnas. Incluya una tercera columna de año, llamada `year`, con el año 2012 en cada fila, finalmente incluya una cuarta columna de sitio de conteo, llamada `site`, que contenga los números del 1 al 61.
