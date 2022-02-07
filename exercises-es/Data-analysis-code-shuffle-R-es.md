---
layout: exercise
topic: Data Analysis
title: Code Shuffle
language: R
---

Nos interesa conocer la variación mensual de la precipitación en
Gainesville, Florida. Usaremos algunos datos de la
[NOAA National Climatic Data Center](http://www.ncdc.noaa.gov/).

Cada fila del [archivo de datos](https://datacarpentry.org/semester-biology/data/gainesville-precip.csv) es un año (de 1961 a 2013) y cada columna es un mes
(enero - diciembre).

Reorganice el siguiente programa para que:

- Importe los datos
- Calcule la precipitación promedio en cada mes a lo largo de los años.
- Grafique los promedios mensuales como un diagrama de línea simple

Finalmente, agregue un comentario sobre el código que describa lo que hace. El comentario
el carácter en R es `#`.

Está bien si no sabe exactamente cómo funcionan los detalles del programa en este momento.
punto, solo necesita descifrar el orden correcto de las líneas con referencia a cuándo
se definen las variables y cuándo se utilizan.

```
plot(monthly_mean_ppt, type = "l", xlab = "Month", ylab = "Mean Precipitation")
monthly_mean_ppt <- colMeans(ppt_data)
ppt_data <- read.csv("https://datacarpentry.org/semester-biology/data/gainesville-precip.csv", header = FALSE)
```