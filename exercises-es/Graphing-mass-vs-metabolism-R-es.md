---
layout: exercise
topic: Graphing
title: Mass vs Metabolism
language: R
---
La relación entre el tamaño corporal de un organismo y su índice metabólico es una de las áreas más estudiadas y aún más controversiales de la fisiología de organismos. Queremos graficar esta relación en el [Artiodactyla](http://en.wikipedia.org/wiki/Even-toed_ungulate) usando un subconjunto de datos de una amplia compilación de datos de tamaño corporal ([Savage et al.
2004](https://doi.org/10.1111/j.0269-8463.2004.00856.x)). Puede copiar y pegar este marco de datos en su programa:

```
size_mr_data <- data.frame(
  body_mass = c(32000, 37800, 347000, 4200, 196500, 100000,
    4290, 32000, 65000, 69125, 9600, 133300, 150000, 407000,
    115000, 67000,325000, 21500, 58588, 65320, 85000, 135000,
    20500, 1613, 1618),
  metabolic_rate = c(49.984, 51.981, 306.770, 10.075, 230.073, 
    148.949, 11.966, 46.414, 123.287, 106.663, 20.619, 180.150, 
    200.830, 224.779, 148.940, 112.430, 286.847, 46.347,
    142.863, 106.670, 119.660, 104.150, 33.165, 4.900, 4.865),
  family = c("Antilocapridae", "Antilocapridae", "Bovidae",
    "Bovidae", "Bovidae", "Bovidae", "Bovidae", "Bovidae",
    "Bovidae", "Bovidae", "Bovidae", "Bovidae", "Bovidae",
    "Camelidae", "Camelidae", "Canidae", "Cervidae",
    "Cervidae", "Cervidae", "Cervidae", "Cervidae", "Suidae",
    "Tayassuidae", "Tragulidae", "Tragulidae"))
```

Haga las siguientes gráficas y rotule los ejes apropiadamente.

1. Una gráfica de masa corporal vs. indice metabólico
2.  Una gráfica de la masa corporal vs. indice metabólico con ejes escalados como log10
    (esto estira el eje, pero mantiene los números en la escala original), y
    el tamaño de punto 3.
3. La misma gráfica que (2), pero con las diferentes familias indicadas por color.
4. La misma gráfica que (2), pero con las diferentes familias, cada una en su propia
   subgráfica.
