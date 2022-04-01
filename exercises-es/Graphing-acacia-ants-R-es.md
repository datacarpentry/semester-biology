---
layout: exercise
topic: Graphing
title: Acacia and Ants
language: R
---
Investigadores en Kenia han estado explorando cómo los grandes herbívoros afectan las plantas.

Verifique si `ACACIA_DREPANOLOBIUM_SURVEY.txt` está en su espacio de trabajo.
Si no, [descárgalo](http://www.esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt).
Impórtelos a R usando el siguiente comando:

```r
acacia <- read.csv("ACACIA_DREPANOLOBIUM_SURVEY.txt", sep="\t", na.strings = c("dead"))
```

1. Haga un diagrama de dispersión con 'CIRC' en el eje X y 'AXIS1' (el dosel máximo
   ancho) en el eje Y. Etiquete el eje X como "Circumference" y el eje y "Canopy
   Diameter".
2. Haga la misma gráfica que (1), pero con ambos ejes en escala logarítmica (usando `scale_x_log10` y `scale_y_log10`).
3. La misma gráfica que (1), pero con puntos coloreados según la columna "HORMIGA" (la especie de hormiga simbionte que vive con la acacia)
4. La misma gráfica que (3)), pero en lugar de diferentes colores muestre diferentes especies de hormigas (valores de `ANT`), cada una en una subgráfica separada.
5. La misma gráfica que (4) pero agregue un modelo simple de los datos con `geom_smooth`.
