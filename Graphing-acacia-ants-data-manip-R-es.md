---
layout: exercise
topic: Graphing
title: Acacia and Ants Data Manipulation
language: R
---
Un experimento en Kenia ha estado explorando la influencia de los grandes herbívoros en las plantas.

Verifique si `TREE_SURVEYS.txt` está en su espacio de trabajo.
Si no, [download `TREE_SURVEYS.txt`](https://ndownloader.figshare.com/files/5629536).
Use `read_tsv` del paquete `readr` para leer los datos usando el siguiente comando:

```r
trees <- read_tsv("TREE_SURVEYS.txt")
```

1. Actualice el marco de datos `trees` con una nueva columna llamada `canopy_area` que contenga
   el área de dosel estimada calculada como: el valor en la columna `AXIS_1`
   multiplicado por el valor de la columna `AXIS_2`.
   Muestre la salida del marco de datos `trees` con solo las columnas `SURVEY`, `YEAR`, `SITE` y `canopy_area`.

2. Haga un diagrama de dispersión con `canopy_area` en el eje de X y `HEIGHT` en el eje de Y. Coloree los puntos por `TREATMENT` y grafique los puntos para cada valor en
   la columna `SPECIES` en una subgráfica separada. Rotule el eje X como "Canopy Area
   (m)" y el eje y "Height (m)". Haga que el tamaño del punto sea 2.
3. La gráfica del ejercicio (2) contiene un valor atípico. 50 por 50 metros es un tamaño exagerado para una Acacia real, así que filtre los datos para eliminar cualquier valor de `AXIS_1`
   y `AXIS_2` mayor de 20 y actualize el marco de datos. Luego rehaga la gráfica.
4. Usando los datos sin el valor atípico (es decir, los datos generados en (3)),
   averigué cómo ha ido cambiando la abundancia de cada especie a lo largo del tiempo.
   Use `group_by`, `summarize` y `n` para crear un marco de datos con `YEAR`,
   'SPECIES', y una columna de 'abundance' que tiene el número de individuos en
   cada especie en cada año. Imprima este marco de datos.
5. Usando los datos que generó el marco de datos en (4), haga una gráfica de líneas con puntos (usando `geom_line` además de `geom_point`) con `YEAR` en el eje de X y `abundance` en el eje de Y con una subgráfica por especie. Para que pueda ver claramente cada tendencia, deje que la escala para
   el eje y varíe entre gráficas agregando `scales = "free_y"` como un argumento opcional a `facet_wrap`.