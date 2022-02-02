---
layout: exercise
topic: Scientific
title: Tree Biomass Challenge
language: R
---
Estimar de la cantidad total de biomasa (*la masa total de todos los individuos*)
en los bosques es importante para comprender el  presupuesto mundial de carbono y cómo el planeta tierra responderá a los aumentos de emisiones de dióxido de carbono

Normalmente no medimos la masa de un árbol, pero tomamos una medida de la
diámetro o circunferencia del tronco y luego estimamos su masa.

Hay muchas ecuaciones para estimar la masa de un árbol a partir de su diámetro,
pero una buena opción es la ecuación:
    
Masa = 0.124 * Diámetro<sup>2.53</sup>

donde `Mass` se mide en kg de biomasa seca sobre suelo seca y
`Diámetro` está en cm

1\. Vamos a estimar la biomasa total de árboles en un area de 96
hectáreas en las Ghats occidentales en la India.

  * [Download the data]({{ site.baseurl }}/data/ramesh2010-macroplots.csv) y
    cargue los datos en R.
  * Escriba una función que tome un vector de diámetros de árboles como argumento y
   devuelve un vector de masas de árboles.
  * Cree un pipeline `dplyr` que
    * Agregue una nueva columna (usando `mutate` y la función que escribió) que contenga masas
      calculadas a partir de los diámetros
    * Agrupe el marco de datos en especies usando la columna `SpCode`
    * Y luego calcule la biomasa (es decir, `sum` de las masas) para cada especie
      (usando `summarize`)
    * Almacene el resultado como un marco de datos
  * Muestre el marco de datos resultante

2\. Haga un histograma de los valores de biomasa de las especies que acaba de calcular.

  * Use 10 intervalos (bins) en el histograma (usando el argumento `bins`)
  * Use una escala log10 para el eje x (usando `scale_x_log10`)
  * Cambie la etiqueta del eje x a `Biomass` y la etiqueta del eje y a `Number of Species` (usando `labs`)