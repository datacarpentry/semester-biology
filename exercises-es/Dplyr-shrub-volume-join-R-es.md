---
layout: exercise
topic: dplyr
title: Shrub Volume Join
language: R
---
En adición a la tabla de datos principal de dimensiones de arbustos, la Dra. Granger tiene dos tablas de datos adicionales.
La primera describe la manipulación de cada experimento.
La segunda contiene información sobre los diferentes sitios de estudio.
Verifique si los archivos espacio de trabajo (es posible que su instructor ya los haya agregado).
De lo contrario, descargue los [datos de experimentos] ({{site.baseurl}} / data / shrub-volume-experiment.csv) y los [datos de sitios] ({{site.baseurl}} / data / shrub-volume-sites. csv).

1. Importe la tabla de datos de los experimentos. Luego, use  `inner_join` combinando la tabla de datos de experimentos con la tabla de datos de dimensiones de arbustos, con el fin de añadir una columna llamada `manipulación` a la tabla de datos de dimensiones de arbustos.

2. Importe la tabla de sitios de estudio. Luego combínela con la tabla que contiene los datos de dimensiones de arbustos y los datos de experimentos. El producto final debe contener las tres tablas en una.
 
