---
layout: exercise
topic: Loops
title: Size Estimates By Name Loop
language: R
---
Esta es una continuación de [Size Estimates by Name]({{ site.baseurl }}/exercises/Making-choices-size-estimates-by-name-R).


Descargue e importe [data on dinosaur lengths with species names]({{ site.baseurl }}/data/dinosaur_lengths.csv).

Escriba una función `mass_from_length()` que use la ecuación `mass <- a * length^b` para estimar el tamaño de un dinosaurio a partir de su longitud.
Esta función debe tomar dos argumentos, `length` y `species`. Para cada una de las siguientes entradas para "species", utilice los valores dados de `a` y `b` para calcular lo siguiente:

* Para (for) `Stegosauria`:  `a = 10.95` y `b = 2.64` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* Para (for) `Theropoda`:  `a = 0.73` y `b = 3.63` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* Para (for)  `Sauropoda`:  `a` = `214.44` and `b = 1.46` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* Para (for) cualquier otro valor de `species`: `a = 25.37` y `b = 2.49`.

1. Utilice esta función y un bucle (loop) for para calcular la masa estimada de cada dinosaurio, almacene las masas en un vector y, luego de completar todos los cálculos, muestre los primeros elementos del vector utilizando `head()`.
2. Vuelva a agregar los resultados en el vector al marco de datos original. Muestra las primeras filas del marco de datos usando `head()`.
3. Calcule la masa media de cada 'species' utilizando 'dplyr'.

