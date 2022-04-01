---
layout: exercise
topic: Functions
title: String Data
language: R
translation: es
titulo: Cadenas de datos
translation: es
---
Este es un seguimiento de [Strings from Data] ({{site.baseurl}}/exercises-es/Strings-strings-from-data-R /).

Un colega ha elaborado un archivo con una secuencia de ADN en cada línea. Descargue
[el archivo] ({{site.baseurl}} / data / dna-sequence-1.txt) y cárguelo en R usando
`read.csv ()`. El archivo no tiene encabezado.

Escribe una función para calcular el contenido de GC. El contenido de GC es el porcentaje de bases
que son G o C como porcentaje del total de pares de bases. Su función debería
tomar una secuencia de ADN como entrada y devolver el contenido de GC de esa secuencia. Imprima
el resultado de cada secuencia.

* Antes de conocer acerca de funciones, hubiéramos tenido que tomar cada secuencia de ADN una a una y luego volver a escribir o copiar y pegar el mismo código para analizar cada una. ¿No es esto mejor? *

* Es posible que haya notado que [for Loop] ({{site.baseurl}} / ejercicios / Functions-for-loop-R /) imprime los resultados de manera diferente. `read.csv ()` importa los datos como un `data.frame ()`, esto en contraste con los vector numéricos del ejercicio anterior. *