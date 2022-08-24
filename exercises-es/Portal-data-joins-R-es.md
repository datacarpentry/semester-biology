---
layout: exercise
topic: dplyr
title: Portal Data Joins
language: R
---
Si `survey.csv`,` species.csv` y `plots.csv` no están disponibles en su espacio de trabajo, descárguelos:

* [`survey.csv`] (https://ndownloader.figshare.com/files/2292172)
* [`species.csv`] (https://ndownloader.figshare.com/files/3299483)
* [`plots.csv`] (https://ndownloader.figshare.com/files/3299474)

Cárguelos en R usando `read.csv ()`.

1. Use `inner_join ()`  para crear una tabla de datos que contenga la información tanto de la tabla de datos de encuestas como de la tabla de datos de `especies`.
2. Use `inner_join ()` dos veces para crear una tabla de datos que contenga la información de las tres tablas de datos.
3. Use `inner_join ()` y `filter ()` para obtener un marco de datos (data frame) con la información de la tabla de datos de `surveys` (estudios) y la tabla de datos de `plots` (parcela) donde `plot_type` (tipo de parcela) es `Control`.