---
layout: exercise
topic: Making Choices
title: Size Estimates by Name
language: R
---
Esta es una continuación de [Use and Modify]({{ site.baseurl }}/exercises/Functions-use-and-modify-R).

Para que sea aún más fácil trabajar con las funciones de estimación del tamaño de los dinosaurios,
usted ha decidido crear una función que le permita especificar el nombre del grupo de dinosaurios a que le desea estimar el tamaño y luego hacer que la función elija automáticamente los parámetros correctos.

Cree una nueva función `get_mass_from_length_by_name()` que tome dos argumentos,
la `length` y el nombre del grupo de dinosaurios. Dentro de esta función use
declaraciones `if`/`else if`/`else` para verificar si el nombre es uno de los
siguientes valores y, si es así, establezca `a` y `b` en los valores apropiados.

* *Estegosauria*: `a` = `10,95` y `b` = `2,64` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Theropoda*: `a` = `0.73` y `b` = `3.63` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).
* *Sauropoda*: `a` = `214.44` y `b` = `1.46` ([Seebacher 2001](http://www.jstor.org/stable/4524171)).

Si el nombre no es ninguno de estos valores, establezca `a` y `b` en `NA`.

Una vez que la función haya asignado `a` y `b`, debe ejecutar `get_mass_from_length()`
con los valores adecuados y devolver la masa estimada.

Ejecute la función para:

1. Un *Stegosauria* de 10 metros de largo.
2. Un *Theropoda* que mide 8 metros de largo.
3. Un *Sauropoda* de 12 metros de largo.
4. Un *Ankylosauria* de 13 metros de largo.

*Reto (**opcional**)*: Si el nombre no es uno de los valores que tienen `a` y `b` imprima un mensaje de que no sabe cómo convertir ese grupo que incluya el nombre de ese grupo en un mensaje como "No known estimation for Ankylosauria". (La función `paste()` será útil aquí). Hacer esto con éxito modificará su respuesta a (4), lo cual está bien

*Reto (**opcional**)*: Cambie su función para que use dos
valores de `a` y `b` para *Stegosauria*. Cuando *Stegosauria* sea mayor que 8
metros de largo su funciona debe usar la ecuación anterior. Cuando tenga menos de 8 metros de largo su función debe usar `a` =
`8.5` y `b` = `2.8`. Ejecute la función para un *Stegosauria* de 6 metros
longitud.