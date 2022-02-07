---
layout: exercise
topic: dplyr
title: Portal Data Manipulation Pipes
language: R
---

Descargue una copia de
[Portal Teaching Database surveys table](https://ndownloader.figshare.com/files/2292172)
y cárguela en R usando `read.csv()`.

Use pipes (`%>%`) para combinar las siguientes operaciones y manipular los datos.

1. Utilice `mutate()`, `select()` y `filter()` con `is.na()` para crear un nuevo marco de datos con
   el `year `, `species_id` y el peso **en kilogramos** de cada individuo, retirando los valores de peso nulos.
2. Use `filter()` y `select()` para obtener las columnas: `year`, `month`, `day` y `species_id` para todas las filas del marco de datos donde `species_id` es `SH`.