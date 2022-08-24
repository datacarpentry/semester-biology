---
layout: exercise
topic: dplyr
title: Portal Data Aggregation
language: R
---
Descargue una copia de la [Tabla de datos de estudios de la base de datos educativa de Portal] (https://ndownloader.figshare.com/files/2292172)
e impórtela a R usando la función `read.csv ()`.

1. Utilice las funciones `group_by ()` y `summary ()` para obtener un conteo del número de individuos por cada species ID (ID de especie).
2. Utilice las funciones `group_by ()` y `summary ()` para obtener un conteo de la cantidad de individuos por cada ID de especie por cada año.
3. Utilice las funciones `filter ()`, `group_by ()` y `summary ()` para obtener la masa promedio de la especie DO por cada año.
