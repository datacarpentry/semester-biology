---
layout: exercise
topic: dplyr
title: Shrub Volume Data Basics
language: R
---
La Dra. Granger está interesada en estudiar los factores que controlan el tamaño y el
almacenamiento de carbono de arbustos. La Dra. ha realizado un experimento para observar el efecto
de tres tratamientos diferentes sobre el volumen de los arbustos en cuatro ubicaciones diferentes. Ella ha colocado el archivo de datos en la web para que lo descargue:

* [Shrub dimensions data]({{ site.baseurl }}/data/shrub-volume-data.csv)

Descargue esto en su carpeta `data` e importelo usando `read.csv ()`, familiarícese con los datos y use `dplyr` para completar las siguientes tareas.

1. Seleccione los datos de la columna `length` e imprímalos (usando `select`).
2. Seleccione los datos de las columnas `site` y `experiment` e imprímalos (usando `select`).
3. Agregue una nueva columna llamada `área` que contenga el área del arbusto, que es el largo por el ancho (usando `mutate`).
4. Ordene los datos por `length` (usando `arrange`).
5. Filtre los datos para incluir solo plantas con `height` mayores de 5 (usando `filter`).
6. Filtre los datos para incluir solo plantas con `height` mayores de 4 y `width` mayores de 2 (usando `,` o `&` para incluir dos condiciones).
7. Filtre (`filter`) los datos para incluir solo plantas del Experimento 1 o Experimento 3 (usando `|` para "o").
8. Filtre (`filter`) los datos para eliminar filas con valores nulos en la columna `height` (usando `!is.na`)
9. Cree un nuevo marco de datos llamado `shrub_volumes` que incluya todos los datos originales y una nueva columna que contenga los volúmenes (`length` * `width` * `height`) y muéstrelos.