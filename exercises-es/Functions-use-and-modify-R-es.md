---
layout: exercise
topic: Functions
title: Use and Modify
language: R
translation: es
titulo: Usando y modificando funciones
---
La longitud de un organismo suele estar altamente correlacionada con su masa corporal. Esto es útil ya que nos permite estimar la masa de un organismo aun cuando solo conocemos su longitud. Esta relación generalmente toma la forma:

> mass = a * length^b

Donde los parámetros "a" y "b" varían entre grupos. Este método alométrico es
utilizado regularmente para estimar la masa corporal de los dinosaurios, ya que solo se han preservado sus huesos.

La siguiente función estima la masa de un organismo en kilogramos como función de su
longitud en metros para unos parametors a y b en particular, los de * Theropoda *
(donde "a" se ha estimado como "0.73" y "b" se ha calculado como "3.63";
[Seebacher 2001] (http://www.jstor.org/stable/4524171)).

```r
get_mass_from_length_theropoda <- function(length){
  mass <- 0.73 * length ^ 3.63
  return(mass)
}
```

1. Utilice esta función para imprimir la masa de un Spinosaurus de 16 m de largo basándose en su esqueleto reensamblado.
2. Cree una nueva versión de esta función llamada `get_mass_from_length ()` que reciba `length`,` a` y `b` como argumentos y use el siguiente código para estimar la masa ` mass <- a * length ^ b` .
Utilice esta función para estimar la masa de un Sauropoda (`a = 214.44`,` b = 1.46`) que mide 26 m de largo.