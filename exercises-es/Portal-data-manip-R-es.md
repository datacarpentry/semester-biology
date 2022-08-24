---
layout: exercise
topic: dplyr
title: Portal Data Manipulation
language: R
---

Download a copy of the
[Portal Teaching Database surveys table](https://ndownloader.figshare.com/files/2292172) (*If you are using RStudio Cloud in a class it may have already been added to your workspace for you*)
and load it into R using `read.csv()`.

***Do not use pipes for this exercise.***

1. Use `select()` to create a new data frame with just the `year`, `month`,
   `day`, and `species_id` columns in that order.
2. Use `mutate()`, `select()`, and `filter()` with `!is.na()` to create a new
   data frame with
   the `year`, `species_id`, and weight **in kilograms** of each individual,
   with no null weights. The weight in the table is given in grams so you will
   need to create a new column for weight in kilograms by dividing the weight column by 1000.
3. Use the `filter()` function to get all of the rows in the data frame for the
   species ID `SH`.
---
diseño: ejercicio
tema: dplyr
título: Manipulación de datos del portal
idioma: R
---

Descargue una copia de [Portal Teaching Database surveys table](https://ndownloader.figshare.com/files/2292172) (*Si está utilizando RStudio Cloud, es posible que los datos hayan sido agregados a su espacio de trabajo*)
y cárguela en R usando `read.csv()`.

***No use pipes para este ejercicio.***

1. Use `select()` para crear un nuevo marco de datos que contenga estas columnas en el siguiente orden: `year`, `month`, `day` y `species_id`.
2. Utilice `mutate()`, `select()` y `filter()` con `!is.na()` para crear un nuevo
   marco de datos con `year`, `species_id` y el peso **en kilogramos** de cada individuo,
   sin valores nulos. El peso,`weight` se da en gramos, por lo que
   necesita crear una nueva columna para el peso en kilogramos dividiendo la columna de `weight` por 1000.
3. Use la función `filter()` para obtener todas las filas en el marco de datos para
   ID de especie: `SH`.