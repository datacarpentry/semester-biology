---
layout: exercise
topic: Loops
title: Size Estimates By Name Apply
language: R
---
Esta es una continuación de [Size Estimates by Name]({{ site.baseurl }}/exercises/Making-choices-size-estimates-by-name-R).

Descargue los [data on dinosaur lengths with species names]({{ site.baseurl }}/data/dinosaur_lengths.csv) e impórtelos usando `read.csv()`.

Escriba una función `get_mass_from_length_by_name()` que use la ecuación `mass <- a * length^b` para estimar el tamaño de un dinosaurio a partir de su longitud. Esta función debe tomar dos argumentos, la `length` y el nombre del grupo de dinosaurios. Dentro de esta función, use las declaraciones `if`/`else if`/`else` para verificar si el nombre es uno de los siguientes valores y, de ser así, establezca `a` y `b` en los valores apropiados.

* *Stegosauria*:  `a = 10.95` and `b = 2.64` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Theropoda*:  `a = 0.73` and `b = 3.63` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Sauropoda*:  `a = 214.44` and `b = 1.46` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).

Si el nombre no es ninguno de estos valores, defina `a = NA` y `b = NA`.

1. Usa esta función y `mapply()` para calcular la masa estimada de cada dinosaurio. Deberá pasar los datos a `mapply()` como vectores o columnas individuales, no como el marco de datos completo.

2. Usando `dplyr`, agregue una nueva columna `masses` al marco de datos (usando `rowwise()`, `mutate()` y la función que ha creado) e imprima el resultado en la consola.

3. Usando `ggplot`, haga un histograma de masas de dinosaurios con una subplot para cada especie (usando `facet_wrap()`).
