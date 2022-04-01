---
layout: exercise
topic: Regular Expressions
title: Find the Rodents
language: R
translation: es
título: Expresiones regulares
---
Existe gran diversidad de fuentes de datos biológicos en el mundo moderno,
pero no todos los datos están bien estructurados. Para
un proyecto, usted necesita una lista de todas las especies de roedores
en el mundo. Encontrará una gran lista de roedores en [el primer
link] (http://en.wikipedia.org/wiki/List_of_rodents) en una búsqueda de Google
para *List of Rodents*.

Desafortunadamente, está en HTML y, en general, se considera que extraer de HTML
Es una pesadilla. Afortunadamente es un artículo de Wikipedia y
Wikipedia tiene una característica que nos permite ver el código fuente (wiki
markup) que se utiliza para construir el HTML. Esto es lo mismo que veríamos si hiciéramos clic en la pestaña `Edit` del artículo, pero mas accesible ya que es un
archivo de texto simple. Esto se puede hacer usando la URL general:

`http: //en.wikipedia.org/w/index.php? title = PAGETITLE & action = raw`

donde `PAGETITLE` se reemplaza con el título real de la página.

Descargue el wiki markup y escriba una corta secuencia de comandos (script) usando
expresiones que extraigan la lista de todos las denominaciones latinas (latin binomials) de la página.
Exporte esta lista como un archivo de texto, con una especie por línea, con género y especies separadas por una coma.

