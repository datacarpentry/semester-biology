---
layout: exercise
topic: dplyr
title: Portal Data dplyr Review
language: R
---
Si `survey.csv`,` species.csv` y `plots.csv` no están disponibles en su espacio de trabajo, descárguelos:

* [`surveys.csv`](https://ndownloader.figshare.com/files/2292172)
* [`species.csv`](https://ndownloader.figshare.com/files/3299483)
* [`plots.csv`](https://ndownloader.figshare.com/files/3299474)

Cárguelos a R usando `read.csv ()`.

Queremos hacer un análisis que compare el tamaño de los individuos en las parcelas de `Control` con el tamaño de los individuos en las parcelas `Long-term Krat Exclosures`. Cree un marco de datos con `year`,` genus`, `species`, `weight` y `plot_type` para todos los casos donde el
el tipo de parcela sea `Control` o `Long-term Krat Exclosures`. Solo incluya
casos en los que `Taxa` es "Rodent". Elimine cualquier registro que no contenga un valor de `weight`.