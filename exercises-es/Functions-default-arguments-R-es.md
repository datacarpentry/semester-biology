---
layout: exercise
topic: Functions
title: Default Arguments
language: R
translation: es
titulo: Argumentos por defecto
---
Este es un seguimiento de [Usar y modificar] ({{site.baseurl}} / ejercicios / Funciones-usar-y-modificar-R).

Permitir que `a` y` b` pasen como argumentos a `get_mass_from_length ()` hizo que la función fuera más flexible, pero para algunos tipos de dinosaurios no tenemos valores específicos de `a` y` b`, por lo que tenemos utilizar valores generales que se puedan aplicar a distintas especies.

Reescriba la función `get_mass_from length ()` de [Usar y modificar]({{site.baseurl}}/exercises-es/Funciones-usar-y-modificar-R) para que sus argumentos tengan valores predetefinidos de `a = 39.9` y `b = 2.6` (los valores promedio de [Seebacher 2001] (http://www.jstor.org/stable/4524171)).

1. Utilice esta función para estimar la masa de un Sauropoda (`a = 214.44`,` b = 1.46`) que
   mide 22 m de largo (configurando `a` y` b` al llamar a la función).
2. Utilice esta función para estimar la masa de un dinosaurio de un grupo taxonómico desconocido que mide 16 m de largo.
   Solo pase la función `length`, no pase` a` o `b`, para que se utilicen los valores predefinidos.