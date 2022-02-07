---
layout: exercise
topic: Graphing
title: Adult vs Newborn Size
language: R
---
Los organismos grandes tienen descendencia más grande. Queremos explorar la forma de este
relación en los mamíferos.

Verifique si `Mammal_lifehistories_v2.txt` está en su directorio de trabajo.
Si no [descárgalo](http://esapubs.org/archive/ecol/E084/093/Mammal_lifehistories_v2.txt)
de la web. Estos datos están delimitados por [Tab], por lo que querrá
usar `sep = "\t"` como argumento opcional cuando llame a `read.csv()`. El `\t` un carácter de tabulación en R (y la mayoría de los otros lenguajes de programación).

Cuando importe los datos, habrán algunas líneas en blanco adicionales al final de el documento. Deshágase de ellas usando el argumento opcional `read.csv()` donde `nrows = 1440` para importar solo las primeras 1440 filas.

Los datos que faltan en este archivo se especifican mediante `-999` y `-999.00`. Especifique en R que
estos son valores nulos usando el argumento opcional `read.csv()`, donde `na.strings = c("-999", "-999.00")`. Esto evitará que sean graficados.

1. Grafique la masa del adulto vs. la masa del recién nacido. Rotule los ejes de manera más clara que
  meramente usando los nombres de las columnas.
2. Parece haber un patrón regular aquí, pero definitivamente no es
   lineal. Veamos si transformar los datos a escala logarítmica lo aclara. Grafique masa adulta
   vs. masa del recién nacido, con ambos ejes escalados logarítmicamente. Rotule los ejes.
3. Esto parece un patrón bastante regular, por lo que se pregunta si varía entre
  entre grupos. Grafique la masa de adultos vs. la masa de recién nacidos, con ambos ejes escalados
   logarítmicamente, y los puntos de datos coloreados por orden. Rotule los ejes.
4. Colorear los puntos fue útil, pero hay muchos puntos y es difícil ver lo que está pasando con todos los órdenes. Utilice `facet_wrap` para crear una subgráfica para cada orden.
5. Ahora visualicemos las relaciones entre las variables usando un modelo lineal simple. Cree una nueva gráfica como la grafica del ejercicio (4), pero usando `geom_smooth` para ajustar un modelo lineal a cada orden. Puede hacer esto usando el argumento opcional `method = "lm"` en `geom_smooth`.
