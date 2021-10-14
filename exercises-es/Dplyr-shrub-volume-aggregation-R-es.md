---
layout: exercise
topic: dplyr
title: Agregando volúmenes de arbustos
language: R
---

Este ejercicio es una continuación de [Shrub Volume Data Basics]({{ site.baseurl }}/exercises/Dplyr-shrub-volume-data-basics-R)
 
La Dra. Granger quiere un resumen de datos tanto para las plantas en su sitio de estudio como para sus experimentos.Verifique si el archivo shrub-volume-data.csv está en su espacio de trabajo (es posible que su instructor ya lo haya agregado). Si no, descárguelo.
 
 
Este código calcula la altura promedio de una planta en cada sitio:

```r
shrub_dims <- read.csv('shrub-volume-data.csv')
by_site <- group_by(shrub_dims, site)
avg_height <- summarize(by_site, avg_height = mean(height))
```
 
1.  Modifique el código para calcular e imprimir la altura promedio de una planta en cada experimento.
2.  Utilice `max ()` para determinar la altura máxima de una planta en cada sitio de estudio.
