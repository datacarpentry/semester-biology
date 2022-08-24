---

layout: exercise
topic: Graphing
title: Acacia and Ants Histograms
language: R
---

Un experimento en Kenia ha estado explorando la influencia de los grandes herbívoros en las plantas.

Verifique si `ACACIA_DREPANOLOBIUM_SURVEY.txt` está en su espacio de trabajo.
Si no, [descárgalo](http://www.esapubs.org/archive/ecol/E095/064/ACACIA_DREPANOLOBIUM_SURVEY.txt).Impórtelos a R usando el siguiente comando:

```r
acacia <- read.csv("data/ACACIA_DREPANOLOBIUM_SURVEY.txt", sep="\t", na.strings = c("dead"))
```

1. Haga un diagrama de barra del número de acacias con cada especie de hormiga mutualista (usando la columna 'ANT').
2. Haga un histograma de la altura de la acacia (usando la columna `ALTURA`). Etiqueta
   el eje x "Height (m)" y el eje y "Number of Acacia".
3. Haga una gráfica que muestre los histogramas de `AXIS1` y `AXIS2`. Debido a la estructura de
   los datos, deberá agregar una segunda capa, geom_histogram(), que
   especifique una nueva estética. Para que sea posible ver ambos conjuntos de barras
   deberá hacerlos transparentes con el argumento opcional alfa = 0.3.
   Establezca el color para `AXIS1` en "red" y `AXIS2` en "black" usando el argumento `fill`. Etiquete el eje x como "Canopy Diameter(m)" y el eje y como "Number of Acacia".
4. Use `facet_wrap()` para hacer la misma gráfica que (3) pero con una subgráfica para cada
   tratamiento. Establezca el número de intervalos (bins) en el histograma como 10.
