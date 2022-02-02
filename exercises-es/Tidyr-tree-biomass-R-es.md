---
layout: exercise
topic: Tidyr
title: Tree Biomass
language: R
---
Estimar de la cantidad total de biomasa (*la masa total de todos los individuos*)
en los bosques es importante para comprender el  presupuesto mundial de carbono y cómo el planeta tierra responderá a los aumentos de emisiones de dióxido de carbono. Medir la masa de árboles enteros es complicado y requiere que los arboles se destruyan.
Afortunadamente, podemos estimar la masa de un árbol en función de su diámetro.

Hay muchas ecuaciones para estimar la masa de un árbol a partir de su diámetro,
pero una buena opción es la ecuación:
    
Masa = 0.124 * Diámetro<sup>2.53</sup>

donde `Mass` se mide en kg de biomasa seca sobre suelo seca y
`Diámetro` está en cm
[DAP](https://en.wikipedia.org/wiki/Diameter_at_breast_height)
([Brown 1997](http://www.fao.org/docrep/W4095E/W4095E00.htm)).

Vamos a estimar la biomasa total de árboles en un area de 96
hectáreas en las Ghats occidentales en la India.
[Los datos sin procesar](https://retriever.readthedocs.io/en/latest/).
Desafortunadamente, los datos estan almacenados en una de base de datos con una estructura pobre y
usar todos los troncos de los árboles sería difícil sin ordenar (tidying) primero los datos.

1. Utilice `tidyr` para `gather()` los datos sin procesar en filas para cada tronco medido.
2. Escriba una función que tome un vector de diámetros de árboles como argumento y
   devuelve un vector de masas de árboles.
3. Los troncos se miden en circunferencia (*o circunferencia*) en lugar de diámetro.
   Escriba una función que tome un vector de circunferencias como argumento
   y devuelve un vector de diámetros (*circunferencia = pi \* diámetro*).
4. Use las dos funciones que escribió para estimar la biomasa total (*es decir,
   la suma de las masas*) de los árboles en este conjunto de datos, imprima el resultado en el pantalla.
5. Separe,`separate()`, el `SpCode` en `GenusCode` y `SpEpCode` y
   estime la biomasa total por género en una tabla. *Técnicamente el
   código de cuatro letras no identifica de forma única todos los géneros en el
   conjunto de datos, pero asumiremos que lo hace para el propósito de este
   ejercicio.*
   