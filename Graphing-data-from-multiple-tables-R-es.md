---
layout: exercise
topic: Graphing
title: Graphing Data From Multiple Tables
language: R


Un experimento en Kenia ha estado explorando la influencia de los grandes herbívoros en las plantas.

Verifique si `ACACIA_DREPANOLOBIUM_SURVEY.txt` y `TREE_SURVEYS.txt` están en su espacio de trabajo.
Si no, descarga [`ACACIA_DREPANOLOBIUM_SURVEY.txt`](http://www.esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt) y [`TREE_SURVEYS.txt`](https://ndownloader.figshare .com/files/5629536)
Instale el paquete `readr` y use `read_tsv` para leer los datos usando los siguientes comandos:

```r
library(readr)
acacia <- read.csv("ACACIA_DREPANOLOBIUM_SURVEY.txt", sep="\t", na.strings = c("dead"))
trees <- read_tsv("TREE_SURVEYS.txt")
```

Queremos comparar la relación entre circunferencia vs. altura en la acacia y con la relación entre circunferencia vs altura para para los árboles de la región. Estos datos se almacenan en dos tablas diferentes. Haga una gráfica con la relación entre 'CIRC' y 'HEIGHT' para los árboles como círculos grises en el fondo y la misma relación para la acacia como círculos rojos trazados encima de los círculos grises. Escale ambos ejes logarítmicamente. Incluye modelos lineales para ambos conjuntos de datos. Rotule de manera apropiada los ejes.