---
layout: exercise
topic: Expressions and Variables
title: Modify the Code
language: R
translation: es
título: Modificando código
---
El siguiente código estima la productividad primaria neta total (NPP; PPB en español) por día
para dos sitios. Lo hace multiplicando los gramos de carbono producidos en un
solo metro cuadrado por día por el área total del sitio. Luego imprime el
NPP diaria para cada sitio.

```r
site1_g_carbon_m2_day <- 5
site2_g_carbon_m2_day <- 2.3
site1_area_m2 <- 200
site2_area_m2 <- 450
site1_npp_day <- site1_g_carbon_m2_day * site1_area_m2
site2_npp_day <- site2_g_carbon_m2_day * site2_area_m2
site1_npp_day
site2_npp_day
```
Copie este código en su tarea. Luego agregue lineas de código que realicen los siguientes pasos e imprima el código después de la
valores de NPP diarios (los que actualmente imprime el código):

1. La suma de NPP diaria total para los dos sitios de estudio.
2. La diferencia entre NPP diaria para los dos sitios de estudio. Queremos
    La diferencia absoluta, así que use la función abs () para asegurarse de que
    el número es positivo.
3. El total de NPP durante un año para los dos sitios de estudio combinados (la suma de los
    valores diarios totaled de NPP de la parte (1) multiplicados por 365).