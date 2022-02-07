---
layout: exercise
topic: Functions
title: Built-in Functions
language: R
translation: es
titulo: Funciones predeterminadas
---
Una función predefinida es aquella ya incluida que puede ser utilizada sin la necesidad de descargarla en un paquete o librería. Algunos ejemplos incluyen:

* `abs ()` devuelve el valor absoluto de un número (por ejemplo, `abs (-2`))
* `round ()`, redondea un número (el primer argumento) a un número predefinido de lugares decimales (el segundo argumento) (por ejemplo, `round (12.1123, 2)`)
* `sqrt ()`, devuelve la raíz cuadrada de el número especificado(por ejemplo, `sqrt (4)`)
* `tolower ()`, convierte una cadena de caracteres a minúsculas (por ejemplo, `tolower (" HOLA ")`)
* `toupper ()`, convierte una cadena de caracteres a mayúsculas (por ejemplo, `toupper (" hola ")`)

Utilice estas funciones predefinidas para imprimir los siguientes elementos:

1. El valor absoluto de -15.5
2. 4.483847 redondeado a una cifra decimal
3. 3.8 redondeado al número entero más cercano. * No es necesario especificar el número de
   lugares decimales en este caso si no lo desea, ya que `round ()`
   esta predefinido a usar `0` si no se indica el segundo argumento. Use
   `help (round)` o `? round` para ver como se indica. *
4. "species" `en mayúsculas.
5. "SPECIES" `en minúsculas.
6. Asigne el valor de la raíz cuadrada de 2.6 a una variable. Luego, redondee la
   variable que ha creado a 2 cifra decimales y asígnela a otra
   variable. Imprime el valor redondeado.

* Desafío opcional *: haga lo mismo establecido en la tarea 6 (* inmediatamente arriba *), pero en lugar de
crear la variable intermedia, realice tanto la raíz cuadrada como el redondeo
en una sola línea poniendo la función `sqrt ()` dentro de la función `round ()`.