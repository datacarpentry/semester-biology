---
layout: exercise
topic: dplyr
title: Portal Data Review
language: R
---
Si `surveys.csv`, `species.csv` y `plots.csv` no están disponibles en su espacio de trabajo, descárguelos:

* [`surveys.csv`](https://ndownloader.figshare.com/files/2292172)
* [`species.csv`](https://ndownloader.figshare.com/files/3299483)
* [`plots.csv`](https://ndownloader.figshare.com/files/3299474)

Cárguelos en R usando `read.csv()`.

1. Cree un marco de datos con solo datos para `species_id` `DO`, con las columnas `year`, `month`, `day`, `species_id` y `weight`.
2. Cree un marco de datos con solo datos para las de especies con ID `PP` y `PB` y para los años a partir del 1995, con las columnas `year`, `species_id` y `hindfoot_length` sin valores nulos para `hindfoot_length` .
3. Cree un marco de datos con la `hindfoot_length` promedio para cada `species_id` en cada  `year` sin valores nulos.
4. Cree un marco de datos con `year`, `genus`, `species`, `weight` and `plot_type` para todos los casos en los que `genus` es `"Dipodomys"`.
5. Haga una gráfica de dispersión con `weight` en el eje x y `hindfoot_length` en el eje y. Use una escala `log10` en el eje x. Coloree los puntos por `species_id`. Rotule con buenos nombres los ejes.
6. Haga un histograma de pesos con una sub gráfica separada para cada `species_id`. No incluya especies sin pesos. Establezca el argumento `scales` en `"free_y"` para que los ejes Y puedan variar. Rotule con buenos nombres los ejes.
7. (Desafío) Haga una gráfica con histogramas de los pesos de tres especies, `PP`, `PB` y `DM`, coloreada por `species_id`, con una faceta diferente (subplot) para cada una de los tres `plot_type`'s: `Control`, `Long-term Krat Exclosure`, and `Short-term Krat Exclosure`. Incluya buenas etiquetas de eje y un título para la gráfica. Exporte su gráfica a un archivo `png`.